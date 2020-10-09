from PyQt5 import QtWidgets as QtW
from GUI.Search import Ui_MainWindow
from GUI.Web import Ui_WebForm
from Webs import TV


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_WebForm()
        self.ui.setupUi(self)

    def get_search_web_data(self, search):
        self.ui.pushButtonSearch.setEnabled(False)
        self.ui.lineEditSearch.setEnabled(False)
        self.ui.pushButtonAdd.setEnabled(False)
        self.ui.lineEditSearch.setText(search)
        browse = TV.Search(search)
        started = browse.start()
        if started:
            results = browse.results




if __name__ == "__main__":
    import sys

    app = QtW.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
