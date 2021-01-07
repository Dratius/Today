from PyQt5 import QtWidgets as QtW

class TvException(Exception):
    """
    docstring
    """
    def __init__(self, title: str, message: str) -> None:
        super().__init__()
        self.title = title
        self.message = message

    def display_error(self):
        critical = QtW.QMessageBox()

        # TODO: Stop repetitious error messages
        critical.setIcon(QtW.QMessageBox.Critical)
        critical.setText(self.message)
        critical.setWindowTitle(self.title)
        critical.setStandardButtons(critical.Ok | critical.Cancel)
        critical.setDefaultButton(QtW.QMessageBox.Ok)
        critical.setEscapeButton(QtW.QMessageBox.Cancel)
        critical.exec_()