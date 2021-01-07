from PyQt5 import QtWidgets as QtW, QtCore
from PyQt5.QtCore import pyqtSignal
from GUI.Search import Ui_MainWindow
from GUI.Web import Ui_WebForm
from Webs.TvShow import Show
from Webs.Tv.DataManager import Storage
from Webs import TV
import TvExceptions


class MainWindow(QtW.QMainWindow):
    """docstring for TodaySearch"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.web = Web()
        self.ui.setupUi(self)

        self.ui.webSearch.returnPressed.connect(self.web_search)

    def web_search(self):
        self.web.get_search_web_data(self.ui.webSearch.text())
        self.web.show()


class Web(QtW.QWidget):
    """docstring for Web"""
    tvSignal = pyqtSignal(str, bool)
    tvSignal2 = pyqtSignal(Show, bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_WebForm()
        self.ui.setupUi(self)
        self.tvBrowser = TvBrowser()
        self.tvShows = []

        self.ui.pushButtonSearch.clicked.connect(self.search)
        self.ui.lineEditSearch.returnPressed.connect(self.search)
        self.ui.comboBoxResults.currentIndexChanged.connect(self.summary)
        self.ui.pushButtonAdd.clicked.connect(self.add_show)

    def search(self):
        """
        docstring
        """
        self.get_search_web_data(self.ui.lineEditSearch.text())

    def get_search_web_data(self, search):
        self.ui.pushButtonSearch.setEnabled(False)
        self.ui.lineEditSearch.setEnabled(False)
        self.ui.pushButtonAdd.setEnabled(False)
        self.ui.lineEditSearch.setText(search)
        self.tvSignal.connect(self.tvBrowser.source_data)
        self.tvSignal.emit(search, False)
        self.tvBrowser.start()
        self.tvBrowser.tvSignal.connect(self.handle_results)

    def handle_results(self, results, started):
        self.tvShows = list(results.values())
        if not started:
            self.ui.comboBoxResults.clear()
            self.ui.pushButtonSearch.setEnabled(True)
            self.ui.lineEditSearch.setEnabled(True)
        else:
            self.ui.pushButtonAdd.setEnabled(True)
            show: Show
            for show in self.tvShows:
                self.ui.comboBoxResults.addItem(show.Title)

    def summary(self, index):
        show: Show
        show = self.tvShows[index]
        self.ui.DescriptionBrowser.setText(show.Description)

    def add_show(self):
        show = self.tvShows[self.ui.comboBoxResults.currentIndex()]
        self.tvSignal2.connect(self.tvBrowser.source_data)
        self.tvSignal2.emit(show, True)
        self.tvBrowser.start()
        self.tvBrowser.tvSignal.connect(self.database)

    def database(self):
        pass


class TvBrowser(QtCore.QThread):
    tvSignal = pyqtSignal(dict, bool)

    def __init__(self):
        super(TvBrowser, self).__init__()
        self.search = ""
        self.fetch = False
        self.browse = None

    def source_data(self, source, get: bool):
        self.search = source
        self.fetch = get

    def run(self):
        if self.fetch:
            self.browse.fetch_show_data(self.search)
            self.tvSignal.emit({}, True)
        else:
            started = False
            self.browse = TV.Search(self.search)

            try:
                started = self.browse.start()
            except TvExceptions.TvException as response:
                response.display_error()

            results = self.browse.results
            self.tvSignal.emit(results, started)


if __name__ == "__main__":
    import sys

    app = QtW.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
