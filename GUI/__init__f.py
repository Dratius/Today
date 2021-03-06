# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import pyqtSignal


def UUID():
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Classes"
                                                   r"\Wow6432Node\TypeLib") \
            as location:
        for i in range(0, winreg.QueryInfoKey(location)[0]):
            try:
                sub = winreg.EnumKey(location, i)
                res = winreg.OpenKey(location, sub)
                subs = winreg.EnumKey(res, 0)
                result = winreg.OpenKey(res, subs)
                if winreg.QueryValue(result, "") == "IDMan 1.0 Type Library":
                    return sub
            except OSError:
                continue


def close():
    sys.exit()


def Settings(theme=False):
    # TODO: Change into a QSetting enable
    default = {'Theme': []}
    default['Theme'].append({"Dark": False})
    if not os.path.exists('settings.json'):
        with open('settings.json', 'w+') as handle:
            json.dump(default, handle)
    else:
        with open('settings.json', 'r') as read:
            reads = json.load(read)
            valid = reads['Theme'][0]['Dark']
        if not valid == theme:
            with open('settings.json', 'w+') as handle:
                default['Theme'][0]['Dark'] = theme
                json.dump(default, handle)


def Theme():
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as read:
            reads = json.load(read)
            valid = reads['Theme'][0]['Dark']
        if valid is True:
            Dark_Theme()
        else:
            Light_Theme()


def iDM():
    setting = QtCore.QSettings()
    key = setting.value('settings/UUID', 'None')
    if key != 'None' and key is not None:
        return key
    else:
        setting.setValue('settings/UUID', UUID())
        setting.sync()
        return UUID()


def Dark_Theme():
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 138, 218))
    app.setPalette(palette)
    Settings(True)


def Light_Theme():
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(237, 237, 237))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(237, 237, 237))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(237, 237, 237))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 138, 218))
    app.setPalette(palette)
    Settings(False)


# GUI CODE
class Ui_MainWindow(QtWidgets.QDialog):
    sig = pyqtSignal(int, str)
    sig1 = pyqtSignal(int)

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.available = []
        self.web_dialog = Ui_Web()
        self.preferences_dialog = Ui_Dialog()
        self.actionCheck_for_updates = QtWidgets.QAction(MainWindow)
        self.actionCalendar = QtWidgets.QDockWidget(MainWindow)
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.calendarWidget = QtWidgets.QCalendarWidget(
            self.dockWidgetContents)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.dockWidget = QtWidgets.QDockWidget("Calendar", MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuThemes = QtWidgets.QMenu(self.menuWindows)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.page_2 = QtWidgets.QWidget()
        self.page = QtWidgets.QWidget()
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.model = QtCore.QStringListModel()
        self.completer = QtWidgets.QCompleter(self.available, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.item_1 = QtWidgets.QTreeWidgetItem(self.item_0)
        self.settings = QtCore.QSettings("ER4OR", "Today")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.database = DatabaseThread()

    def setupUi(self, Window):
        Window.setObjectName("MainWindow")
        Window.resize(self.settings.value("Size", QtCore.QSize(1036, 391)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/images/orange.jpg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout.setObjectName("gridLayout")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 1, 1, 1)
        self.label_2.setObjectName("label_2")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_2, 8, 2, 1, 1)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 12, 2, 1, 1)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 21, 0, 1, 1)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 9, 1, 1, 1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setEnabled(False)
        self.gridLayout.addWidget(self.spinBox_4, 11, 2, 1, 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 9, 2, 1, 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setEnabled(False)
        self.gridLayout.addWidget(self.spinBox_3, 11, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(7)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("intValue", 65)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 0, 1, 1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 19, 0, 1, 1)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 13, 1, 1, 2)
        self.radioButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 15, 1, 1, 1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 15, 2, 1, 1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 12, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 21, 1, 1, 2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 7, 0, 9, 1)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(4)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 2)
        Window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile.setObjectName("menuFile")
        self.menuThemes.setObjectName("menuThemes")
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp.setObjectName("menuHelp")
        self.menuWindows.setObjectName("menuWindows")
        Window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionManual.setObjectName("actionManual")
        self.actionAbout.setObjectName("actionAbout")
        self.actionVersion.setObjectName("actionVersion")
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionCalendar.setObjectName("actionCalendar")
        self.actionCheck_for_updates.setEnabled(False)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCheck_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionVersion)
        self.menuWindows.addAction(self.dockWidget.toggleViewAction())
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.menuThemes.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.actionLight.setObjectName("actionLight")
        self.actionDark.setObjectName("actionDark")
        self.menuThemes.addSeparator()
        self.menuThemes.addAction(self.actionDark)
        self.menuThemes.addAction(self.actionLight)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.VLine)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.item_1.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.item_1.setForeground(0, brush)
        self.item_1.setToolTip(1, "")
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.gridLayout.addWidget(self.treeWidget, 4, 1, 1, 2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 16, 1, 1, 1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 16, 2, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        MainWindow.setTabOrder(self.treeWidget, self.lineEdit)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.settings.beginGroup("main_window")
        self.fetchShowData()

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("MainWindow", "TodaytvSeries"))
        self.label.setText(_translate("MainWindow", "Season"))
        self.label_2.setText(_translate("MainWindow", "Episode"))
        self.radioButton_5.setText(
            _translate("MainWindow", "From And To Specifics"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html>"
                                                            "<head/><body><p>"
                                                            "Search The Web"
                                                            "</p></body>"
                                                            "</html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.lcdNumber.setToolTip(_translate("MainWindow", "<html>"
                                                           "<head/><body><p>"
                                                           "Time Till Next "
                                                           "Release</p></body>"
                                                           "</html>"))
        self.spinBox_3.setPrefix(_translate("MainWindow", "Season "))
        self.spinBox_4.setPrefix(_translate("MainWindow", "Episode "))
        self.label_4.setText(_translate("MainWindow", "Web Search Bar"))
        self.radioButton_3.setText(
            _translate("MainWindow", "From Specific Episode ("
                                     "current season ONLY)"))
        self.radioButton.setText(
            _translate("MainWindow", "From Specific Season"))
        self.radioButton_2.setText(
            _translate("MainWindow", "From a Specific Point in the "
                                     "Series"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.radioButton_4.setText(
            _translate("MainWindow", "One Specific Episode"))
        self.pushButton.setText(_translate("MainWindow", "Send to IDM"))
        self.textBrowser.setToolTip(
            _translate("MainWindow", "Current Episode"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuWindows.setTitle(_translate("MainWindow", "&Windows"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut("Ctrl+N")
        self.actionNew.setStatusTip('Add File')
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(close)
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAbout.setText(_translate("MainWindow", "About Developer"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionQuit_2.setText(_translate("MainWindow", "Open"))
        self.actionCheck_for_updates.setText(
            _translate("MainWindow", "Check for updates."))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionDark.triggered.connect(Dark_Theme)
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionLight.triggered.connect(Light_Theme)
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "Web Search"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow",
                                                           "Season/Episode"))
        self.treeWidget.headerItem().setText(1,
                                             _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow",
                                                           "Added to List"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow",
                                                           "Available"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow",
                                                              "Season 2"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("MainWindow",
                                                              "5/13"))
        self.treeWidget.topLevelItem(0).setText(3,
                                                _translate("MainWindow", "7"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate(
            "MainWindow", "Episode 1"))
        self.item_1.setToolTip(0, _translate("MainWindow", "rrr"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate(
            "MainWindow", "Sep"))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate(
            "MainWindow", "Yes"))
        self.treeWidget.topLevelItem(0).child(0).setText(3, _translate(
            "MainWindow", "Yes"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow",
                                                              "Season 1"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow",
                                                              "ooi"))
        self.treeWidget.topLevelItem(1).setText(2, _translate("MainWindow",
                                                              "10/10"))
        self.treeWidget.topLevelItem(1).setText(3,
                                                _translate("MainWindow", "10"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "Extras"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.actionPreferences.triggered.connect(lambda: self.preferences())
        self.lineEdit_2.returnPressed.connect(lambda: self.web())
        self.radioButton.clicked.connect(lambda: self.check())
        self.radioButton_2.clicked.connect(lambda: self.check())
        self.radioButton_3.clicked.connect(lambda: self.check())
        self.radioButton_4.clicked.connect(lambda: self.check())
        self.radioButton_5.clicked.connect(lambda: self.check())

    # FEATURES

    def preferences(self):
        self.preferences_dialog.setupUi()
        Dialog.exec_()

    def web(self):
        search = self.lineEdit_2.text()
        self.web_dialog.setup_ui(Web)
        self.web_dialog.get_search_web_data(search)
        Web.exec_()

    def check(self):
        if self.radioButton_5.isChecked():
            self.spinBox_4.setEnabled(True)
            self.spinBox_3.setEnabled(True)
        else:
            self.spinBox_4.setEnabled(False)
            self.spinBox_3.setEnabled(False)

    def fetchShowData(self):
        self.sig1.connect(self.database.source_data4)
        self.sig1.emit(4)
        self.database.start()
        self.database.sig.connect(self.UseShowData)

    def UseShowData(self, available):
        self.model.setStringList(available)
        self.completer.setModel(self.model)
        self.lineEdit.setCompleter(self.completer)


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.tab_2 = QtWidgets.QWidget()
        self.tab = QtWidgets.QWidget()
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.toolButton_2 = QtWidgets.QToolButton(self.tab)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.label = QtWidgets.QLabel(self.tab)
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.settings = QtCore.QSettings()

    def setupUi(self):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 314)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.setObjectName("tabWidget")
        self.tab.setObjectName("tab")
        self.gridLayout.setObjectName("gridLayout")
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.lineEdit.setMaximumSize(QtCore.QSize(13777215, 16777215))
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 2, 3, 1, 1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 2, 1, 1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.label_6.setMaximumSize(QtCore.QSize(50, 50))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 2, 1, 1)
        self.label_2.setMaximumSize(QtCore.QSize(140, 50))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))

        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 7, 2, 1, 1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.label.setText(_translate("Dialog", "Cookie"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "Password"))
        self.label_6.setText(_translate("Dialog", "Referrer"))
        self.label_4.setText(_translate("Dialog", "User"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.label_2.setText(_translate("Dialog", "IDM Save Directory"))
        self.label_3.setText(_translate("Dialog", "IDM UUID"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label_7.setText(_translate("Dialog", "Post Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("Dialog", "IDM Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("Dialog", "Advanced"))
        self.toolButton.clicked.connect(lambda: self.browse("Save Location"))
        self.lineEdit.setText(self.settings.value('settings/Cookie'))
        self.lineEdit_2.setText(iDM())
        self.lineEdit_3.setText(self.settings.value('settings/Location'))
        self.lineEdit_4.setText(self.settings.value('settings/User'))
        self.lineEdit_5.setText(self.settings.value('settings/Password'))
        self.lineEdit_6.setText(self.settings.value('settings/Referrer'))
        self.lineEdit_7.setText(self.settings.value('settings/PostData'))
        self.lineEdit.returnPressed.connect(
            lambda: self.lineEdit.setText(self.lineEdit.text()))
        self.pushButton.clicked.connect(lambda: self.save())

    # FEATURES

    def browse(self, saver):
        option1 = QtWidgets.QFileDialog.DontResolveSymlinks
        option2 = QtWidgets.QFileDialog.ShowDirsOnly
        options = option1 | option2
        display_line = self.lineEdit_3.text()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, saver,
                                                               display_line,
                                                               options=options)
        if directory:
            self.lineEdit_3.setText(directory)

    def save(self):
        self.settings.setValue('settings/Location', self.lineEdit_3.text())
        self.settings.setValue('settings/Cookie', self.lineEdit.text())
        self.settings.setValue('settings/User', self.lineEdit_4.text())
        self.settings.setValue('settings/Password', self.lineEdit_5.text())
        self.settings.setValue('settings/Referrer', self.lineEdit_6.text())
        self.settings.setValue('settings/PostData', self.lineEdit_7.text())
        self.settings.sync()


class Ui_Web(QtWidgets.QDialog):
    sig1 = pyqtSignal(int, str)
    sig2 = pyqtSignal(str, str)
    sig3 = pyqtSignal(int, dict)
    sig4 = pyqtSignal(int, list, list, list, str)

    def __init__(self, parent=None):
        super(Ui_Web, self).__init__(parent)
        self.seriesInfo = StorageInfo()
        self.thread1 = StorageData()
        self.database = DatabaseThread()
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.comboBox = QtWidgets.QComboBox(Web)
        self.gridLayout = QtWidgets.QGridLayout(Web)
        self.scrollArea = QtWidgets.QScrollArea(Web)
        self.textBrowser = QtWidgets.QTextBrowser(
            self.scrollAreaWidgetContents_2)
        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_2)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.lineEdit = QtWidgets.QLineEdit(Web)
        self.pushButton_2 = QtWidgets.QPushButton(Web)
        self.spinBox = QtWidgets.QSpinBox(Web)
        self.pushButton = QtWidgets.QPushButton(Web)
        self.show = ''
        self.results = {}

    def setup_ui(self, webs):
        webs.setObjectName("Web")
        webs.resize(548, 253)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(size_policy)
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(size_policy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 528, 178))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(size_policy)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setMidLineWidth(3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 2, 1, 1)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(size_policy)
        self.spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBox.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 2, 1, 1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setInputMask("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.pushButton.setEnabled(False)
        self.retranslateUi(webs)
        QtCore.QMetaObject.connectSlotsByName(webs)

    def retranslateUi(self, Webs):
        _translate = QtCore.QCoreApplication.translate
        Webs.setWindowTitle(_translate("Web", "Web"))
        self.textBrowser.setDocumentTitle(_translate("Web", "Description"))
        self.pushButton_2.setText(_translate("Web", "Search"))
        self.lineEdit.setPlaceholderText(_translate("Web", "Web Search"))
        self.pushButton.setText(_translate("Web", "ADD SHOW"))
        self.pushButton_2.clicked.connect(
            lambda: self.get_search_web_data(self.lineEdit.text()))
        self.lineEdit.returnPressed.connect(
            lambda: self.get_search_web_data(self.lineEdit.text()))
        self.comboBox.currentIndexChanged.connect(self.add_summary)
        self.pushButton.clicked.connect(lambda: self.add_show_metadata())

    # FEATURES

    # Searches and Fetches Query Information Data
    def get_search_web_data(self, search):
        self.pushButton_2.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText(search)
        self.sig1.connect(self.seriesInfo.source_data)
        self.sig1.emit(self.spinBox.value(), search)
        self.seriesInfo.start()
        self.seriesInfo.tvSignal.connect(self.handle_thread_result)

    def handle_thread_result(self, result: dict, error: str, i: int):
        if i == 0:
            self.display_error(error)
        elif i == 1:
            self.handle_duplicates(result)

    def handle_duplicates(self, data):
        self.sig3.connect(self.database.get_available_shows)
        self.sig3.emit(data)
        self.database.start()
        self.database.sig2.connect(self.add_to_combobox)
        self.pushButton.setEnabled(True)

    def display_error(self, error):
        critical = QtWidgets.QMessageBox()
        self.comboBox.clear()

        # TODO: Stop repetitious error messages
        critical.setIcon(QtWidgets.QMessageBox.Critical)
        critical.setText(f" SERVER DOWN, can't maintain connection.\n"
                         f"\n"
                         f"Site Might be under maintenance or blocked ip "
                         f"or\n "
                         f"unavailable internet connection..\n"
                         f"\n"
                         f"\n"
                         f"For more Info on Error:\n"
                         f"{error}")
        critical.setWindowTitle("TIMEOUT ERROR!!!!")
        critical.setStandardButtons(critical.Ok | critical.Cancel)
        critical.setDefaultButton(QtWidgets.QMessageBox.Ok)
        critical.setEscapeButton(QtWidgets.QMessageBox.Cancel)
        critical.exec_()

    # Combobox Data
    def add_to_combobox(self, items, results):
        self.results = results
        for title in items:
            self.comboBox.addItem(title)

        self.pushButton_2.setEnabled(True)
        self.lineEdit.setEnabled(True)

    def add_summary(self, index):
        for i in self.results:
            if self.results[i]['index'] == index:
                self.textBrowser.setText(self.results[i]['summary'])

    # Fetches Show Download Links
    def add_show_metadata(self):
        self.pushButton.setEnabled(False)
        self.textBrowser.clear()
        self.sig1.connect(self.database.add_metadata)
        self.sig1.emit(2, self.comboBox.currentText())
        self.database.start()
        self.database.sig1.connect(self.getShowData)

    def getShowData(self, link):
        self.sig2.connect(self.thread1.source_data)
        self.sig2.emit(link, self.comboBox.currentText())
        self.thread1.start()
        self.thread1.sign.connect(self.addShowData)
        self.comboBox.clear()

    def addShowData(self, title, result, error, i):
        critical = QtWidgets.QMessageBox()

        if i == 0:
            critical.setIcon(QtWidgets.QMessageBox.Critical)
            critical.setText()
            critical.setWindowTitle("TIMEOUT ERROR!!!!")
            critical.setStandardButtons(critical.Ok | critical.Cancel)
            critical.setDefaultButton(QtWidgets.QMessageBox.Ok)
            critical.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            critical.exec_()

            self.database.delete_last_row()
            self.database.start()

        elif i == 3:
            self.sig4.connect(self.database.source_data3)
            self.sig4.emit(i, result, title)
            self.database.start()


# BACKGROUND PROCESSING FOR FASTER RESULTS "Reduces Lags"
class StorageInfo(QtCore.QThread):
    """StorageInfo:
    This is a background process thread for the phase one fetch,
    Searches data on TodayTvSeries and tv maze for additional data
    then extracts relevant data from both sites then it
    Emits Result data signal from a dict format for processing
    """
    limits: int
    search: str
    tvSignal = pyqtSignal(dict, str, int)

    def __init__(self):
        super(StorageInfo, self).__init__()
        self.search = ""
        self.limits = 0

    def source_data(self, limit: int, source: str):
        self.search = source
        self.limits = limit

    def run(self):
        error = ''
        soup = ""
        results = {}
        has_error = False
        tv_maze = "http://api.tvmaze.com/"
        today_tv = "http://www.todaytvseries2.com/"

        try:
            tv_series_html = requests.get(
                f"{today_tv}search-series?searchword="
                f"{self.search}&searchphrase=all&limit={self.limits}"
            )
            soup = BeautifulSoup(tv_series_html.text, "html.parser")
            online = tv_series_html.ok

        except Exception as exc:
            online = False
            error = str(exc)
            has_error = True

        if online:
            tags = soup.select('.uk-article-titletag a')

            for tag in tags:
                title = tag.get('title')
                link = today_tv + tag.get('href')

                try:
                    tv_maze_search = requests.get(
                        tv_maze + "search/shows?q=" + title
                    )
                    api_results = json.loads(tv_maze_search.text)

                    if len(api_results) > 0:
                        # TODO: kill assumption on first_result var

                        first_result = api_results[0]['show']
                        results.update({
                            title: {'Link': link,
                                    'summary': first_result['summary'],
                                    'Maze_Name': first_result['name'],
                                    'status': first_result['status'],
                                    'schedule': first_result['schedule'],
                                    'ID': first_result['id'],
                                    'index': -1
                                    }})

                except Exception as exc:
                    has_error = True
                    error = str(exc)
                    break

        if has_error:
            self.tvSignal.emit(results, error, 0)
        else:
            self.tvSignal.emit(results, error, 1)


class StorageData(QtCore.QThread):
    """StorageData:
    This is a background process thread for the phase two fetch,
    this process fetches from TodayTvSeries and stores the individual show
    data (episodes, quality, size) into a dict"""

    sign = pyqtSignal(str, dict, str, int)

    def __init__(self):
        super(StorageData, self).__init__()
        self.Link = ''
        self.Title = ''

    def source_data(self, link, title):
        self.Link = link
        self.Title = title

    def run(self):
        error = ''
        soup = ''
        has_error = False
        title_pattern = re.compile(r"(S\d\d)(E\d\d)+")
        quality_pattern = re.compile(r"480p|720p|1080p")
        result = {'Season 0': {}, 'Extras': {}}

        try:
            html = requests.get(self.Link)
            soup = BeautifulSoup(html.text, 'html.parser')
            online = html.ok
        except Exception as e:
            online = False
            has_error = True
            error = str(e)

        if online:
            show_data = soup.select('.row2')
            prev_episode = ''
            current_season = 0
            active_season = ''
            for row in show_data:
                curr_episode = row.select(".cell2")[0].getText()
                quality = row.select(".cell4")[0].getText()
                size = row.select(".cell3")[0].getText()
                link = row.select('.cell4 .hvr-icon-sink-away')[0].get("href")
                title_match = title_pattern.search(curr_episode)
                quality_match = quality_pattern.search(quality)

                if curr_episode == prev_episode:
                    if title_match is None:
                        result["Extras"][curr_episode]["Links"][
                            quality[quality_match.start():]] = [size, link]
                        continue
                    else:
                        result[f"Season {current_season}"][curr_episode[3:]][
                            'Links'][quality[quality_match.start():]] = [size,
                                                                         link]
                        continue
                else:
                    prev_episode = curr_episode

                if title_match is None:
                    if quality_match is None:
                        result["Extras"].update({curr_episode: [size, link]})
                    else:
                        result["Extras"].update({curr_episode: {"Links": {
                            quality[quality_match.start():]: [size, link]}}})
                else:
                    current_season = int(title_match.group(1)[1:])

                    if 'Season 0' in result:
                        result[f"Season {current_season}"] = result.pop(
                            'Season 0')

                    if active_season == current_season:
                        if quality_match is None:
                            result[f"Season {current_season}"].update(
                                {curr_episode[3:]: [size, link]})
                            continue
                        else:
                            result[f"Season {current_season}"].update({
                                curr_episode[3:]: {"Links": {
                                    quality[quality_match.start():]: [size,
                                                                      link]}}})
                            continue

                    if quality_match is None:
                        result.update({f"Season {current_season}": {
                            curr_episode[3:]: [size, link]}})
                        active_season = current_season
                    else:
                        result.update({f"Season {current_season}": {
                            curr_episode[3:]: {"Links": {
                                quality[quality_match.start():]: [size,
                                                                  link]}}}})

        if has_error:
            self.sign.emit(self.Title, result, error, 3)
        else:
            self.sign.emit('', result, error, 0)


class DatabaseThread(QtCore.QThread):
    """docstring for databaseThread"""
    sig = pyqtSignal(list)
    sig1 = pyqtSignal(str)
    sig2 = pyqtSignal(list, dict)

    def __init__(self):
        super(DatabaseThread, self).__init__()
        self.AddMetadata = False
        self.FilterShows = False
        self.Storages = {}
        self.Number = 0
        self.Storage = ''
        self.ShowData = {}
        self.Title = ""

    def get_available_shows(self, result, get = True):
        self.Storages = result
        self.FilterShows = get

    def add_metadata(self, show):
        self.Storage = show

    def source_data3(self, number, result, title):
        self.Title = title
        self.ShowData = result
        self.Number = number

    def source_data4(self, number):
        self.Number = number

    def delete_last_row(self):
        self.Number = 5

    def run(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        resulted = QtSql.QSqlQueryModel()
        query = QtSql.QSqlQuery()
        db.setUserName("ER40R")
        db.setPassword("230798")
        db.setDatabaseName("TodayTvSeries.db")
        db.open("ER40R", "230798")
        log = open('log.txt', 'a')

        if self.FilterShows:
            index = 0
            items = []
            for Show in self.Storages:
                query.exec_(
                    'SELECT tv.[Maze ID] FROM  TvMaze tv WHERE tv.Name = "{}";'
                        .format(Show)
                )
                while query.next():
                    available = query.value(0)
                    if not available or self.Storages[Show]["ID"]:
                        items.append(Show)
                        self.Storages[Show]['index'] = index
                        index += 1
            db.close()
            self.sig2.emit(items, self.Storages)

        elif self.Number == 2:
            link = ''
            for Show in self.Storages:
                if Show == self.Storage:

                    query.exec_('''CREATE TABLE IF NOT EXISTS TodayTvSeries (
                                    ID                 INTEGER,
                                    Name               VARCHAR,
                                    Link               VARCHAR UNIQUE,
                                    [Database Episode] VARCHAR DEFAULT S0E0,
                                    PRIMARY KEY (
                                        ID
                                    )
                                    );''')

                    query.exec_(''' CREATE TABLE IF NOT EXISTS TvMaze (
                                        ID             INTEGER,
                                        Name           VARCHAR,
                                        [Last Episode] VARCHAR,
                                        Schedule       TIME,
                                        Description    VARCHAR,
                                        Image          VARCHAR,
                                        Running        BOOLEAN,
                                        Day            VARCHAR,
                                        [Maze ID]      INTEGER,
                                        PRIMARY KEY (
                                            ID
                                        )
                                    );''')

                    if self.Storages[Show]["status"] == "Running":
                        running = True
                    else:
                        running = False
                    link = self.Storages[Show]['Link']
                    schedule = self.Storages[Show]['schedule']['time']
                    description = self.Storages[Show]['summary']
                    day = self.Storages[Show]['schedule']['days'][0]
                    maze_id = self.Storages[Show]['ID']
                    name = self.Storages[Show]['Maze_Name']

                    query.prepare('''INSERT INTO TodayTvSeries (
                                                                    Name,
                                                                    Link
                                                                )
                                                                VALUES (
                                                                    :Name,
                                                                    :Link
                                                                );''')

                    query.bindValue(":Name", Show)
                    query.bindValue(":Link", link)
                    query.exec_()

                    print(f'inserted {Show} and {link} on todaytvseries \n',
                          file=log)

                    query.prepare('''INSERT INTO TvMaze (
                                                            Name,
                                                            [Last Episode],
                                                            Schedule,
                                                            Description,
                                                            Image,
                                                            [Local Image],
                                                            Running,
                                                            Day,
                                                            [Maze ID]
                                                        )
                                                        VALUES (
                                                            :Name,
                                                            :Last_Episode,
                                                            :Schedule,
                                                            :Description,
                                                            :Image,
                                                            :Local_Image,
                                                            :Running,
                                                            :Day,
                                                            :Maze_ID
                                                        );''')

                    query.bindValue(":Name", name)
                    query.bindValue(":Last_Episode", "0")
                    query.bindValue(":Schedule", schedule)
                    query.bindValue(":Description", description)
                    query.bindValue(":Image", "0")
                    query.bindValue(":Local_Image", "0")
                    query.bindValue(":Running", running)
                    query.bindValue(":Day", day)
                    query.bindValue(":Maze_ID", maze_id)
                    query.exec_()

                    print(f'inserted {name}, {schedule}, {description},'
                          f' {running}, {day} and {maze_id} on TvMaze'
                          f' \n', file=log)
                    break
            db.commit()
            db.close()
            self.sig1.emit(link)

        elif self.Number == 3:
            default = "0"

            series = """CREATE TABLE IF NOT EXISTS {} (
                            ID      INTEGER,
                            Season  INTEGER    NOT NULL,
                            Episode INTEGER    NOT NULL,
                            Size    VARCHAR    NOT NULL,
                            [480p]  VARCHAR    NOT NULL
                                            UNIQUE,
                            PRIMARY KEY (
                                ID
                            )
                        );""".format(self.Title)

            extras = """CREATE TABLE IF NOT EXISTS Extras (
                            ID      INTEGER,
                            Name    VARCHAR    NOT NULL,
                            Size    VARCHAR    NOT NULL,
                            [480p]  VARCHAR    NOT NULL
                                            UNIQUE,
                            PRIMARY KEY (
                                ID
                            )
                        );"""

            other_links = """CREATE TABLE IF NOT EXISTS Links (
                                ID      INTEGER,
                                Quality VARCHAR    NOT NULL,
                                Size    VARCHAR    NOT NULL,
                                Link    VARCHAR    NOT NULL
                                                UNIQUE,
                                PRIMARY KEY (
                                    ID
                                )
                            );"""

            query.exec_(series)
            query.exec_(extras)
            query.exec_(other_links)

            for Show in self.ShowData:
                if Show == 'Extras':
                    for i, Extra in enumerate(Show):
                        xtra_key = list(Extra.keys())

                        query.prepare('''INSERT INTO Extras (
                                                            Name,
                                                            Size,
                                                            [480p]
                                                        )
                                                        VALUES (
                                                            :Name,
                                                            :Size,
                                                            :Quality
                                                        );''')

                        query.bindValue(":Name", xtra_key[i])
                        xtra = Extra.get(xtra_key[i])
                        xtra_link = []

                        if isinstance(xtra, list):
                            query.bindValue(":Size", xtra[0])
                            query.bindValue(":Quality", xtra[1])

                        else:
                            for link in xtra['Links']:
                                query.bindValue(":Size", link[0])
                                query.bindValue(":Quality", link[1])
                        else:
                            xtra_link.append(xtra["Links"])


                query.prepare('''INSERT INTO {} (
                                                   Episode,
                                                   Size,
                                                   Link
                                                )
                                                VALUES (
                                                   :Episode,
                                                   :Size,
                                                   :Link
                                                );'''.format(self.Title))

                query.bindValue(":Episode", number.getText())
                query.bindValue(":Size", mb.getText())
                query.bindValue(":Link", urls.get('href'))
                query.exec_()

                default = number.getText()

            if not os.path.exists('ShowData.json'):
                with open('ShowData.json', 'w+') as handle:
                    json.dump(self.Storages, handle)

            query.prepare(f'''UPDATE TodayTvSeries
                                 SET [Database Episode] = :Database_Episode
                               WHERE Name = "{self.Title}";''')

            query.bindValue(":Database_Episode", default)
            query.exec_()

            db.commit()
            db.close()

        elif self.Number == 4:
            resulted.setQuery('SELECT tv.Name FROM TodayTvSeries tv')
            available = []
            i = 0

            while resulted.record(i).value("Name") is not None:
                available.append(resulted.record(i).value("Name"))
                i += 1

            db.close()
            self.tvSignal.emit(available)

        elif self.Number == 5:
            query.exec_('DELETE FROM TodayTvSeries WHERE ID = MAX(ID)')
            query.exec_('DELETE FROM TvMaze WHERE ID = MAX(ID)')
            db.commit()
            db.close()


if __name__ == "__main__":
    import sys
    import json
    import re
    import os
    import winreg
    import requests
    from bs4 import BeautifulSoup

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    QtCore.QCoreApplication.setOrganizationName("ER40R")
    QtCore.QCoreApplication.setOrganizationDomain("dratius.com")
    QtCore.QCoreApplication.setApplicationName("Today_tv_series")
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    Web = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    Theme()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
