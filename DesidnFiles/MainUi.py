# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ayieko/Projects And Research/Python Projects/Github-Desktop/DesidnFiles/MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(290, 59, 661, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 561, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(30, 210, 561, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 291, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.openRepoInEditorBtn = QtWidgets.QPushButton(self.frame)
        self.openRepoInEditorBtn.setGeometry(QtCore.QRect(320, 30, 231, 31))
        self.openRepoInEditorBtn.setObjectName("openRepoInEditorBtn")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(30, 310, 561, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 391, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.showInExplorerBtn = QtWidgets.QPushButton(self.frame_2)
        self.showInExplorerBtn.setGeometry(QtCore.QRect(419, 30, 131, 31))
        self.showInExplorerBtn.setObjectName("showInExplorerBtn")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(30, 410, 561, 101))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 10, 391, 81))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.viewOnGitBtn = QtWidgets.QPushButton(self.frame_3)
        self.viewOnGitBtn.setGeometry(QtCore.QRect(420, 30, 131, 31))
        self.viewOnGitBtn.setObjectName("viewOnGitBtn")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_4 = QtWidgets.QFrame(self.page_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 661, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget = QtWidgets.QWidget(self.frame_4)
        self.widget.setGeometry(QtCore.QRect(0, 31, 661, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.histUserLabel = QtWidgets.QLabel(self.widget)
        self.histUserLabel.setMinimumSize(QtCore.QSize(110, 30))
        self.histUserLabel.setObjectName("histUserLabel")
        self.horizontalLayout.addWidget(self.histUserLabel)
        self.histhashLabel = QtWidgets.QLabel(self.widget)
        self.histhashLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.histhashLabel.setObjectName("histhashLabel")
        self.horizontalLayout.addWidget(self.histhashLabel)
        self.histchandedFilesLable = QtWidgets.QLabel(self.widget)
        self.histchandedFilesLable.setMinimumSize(QtCore.QSize(110, 30))
        self.histchandedFilesLable.setObjectName("histchandedFilesLable")
        self.horizontalLayout.addWidget(self.histchandedFilesLable)
        self.histhideWhiteCheck = QtWidgets.QCheckBox(self.widget)
        self.histhideWhiteCheck.setMinimumSize(QtCore.QSize(152, 30))
        self.histhideWhiteCheck.setObjectName("histhideWhiteCheck")
        self.horizontalLayout.addWidget(self.histhideWhiteCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget1 = QtWidgets.QWidget(self.frame_4)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 661, 32))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.histCommitMessgLabel = QtWidgets.QLabel(self.widget1)
        self.histCommitMessgLabel.setMinimumSize(QtCore.QSize(240, 30))
        self.histCommitMessgLabel.setObjectName("histCommitMessgLabel")
        self.horizontalLayout_2.addWidget(self.histCommitMessgLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.splitter = QtWidgets.QSplitter(self.page_3)
        self.splitter.setGeometry(QtCore.QRect(0, 70, 661, 521))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.histFileslistWidget = QtWidgets.QListWidget(self.splitter)
        self.histFileslistWidget.setMinimumSize(QtCore.QSize(20, 521))
        self.histFileslistWidget.setObjectName("histFileslistWidget")
        item = QtWidgets.QListWidgetItem()
        self.histFileslistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.histFileslistWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.histFileslistWidget.addItem(item)
        self.diffText = QtWidgets.QTextEdit(self.splitter)
        self.diffText.setMinimumSize(QtCore.QSize(412, 521))
        self.diffText.setObjectName("diffText")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 281, 652))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CurrentRepoCombo = QtWidgets.QComboBox(self.widget2)
        self.CurrentRepoCombo.setMinimumSize(QtCore.QSize(50, 50))
        self.CurrentRepoCombo.setCurrentText("antony\\nalen")
        self.CurrentRepoCombo.setMinimumContentsLength(1)
        self.CurrentRepoCombo.setObjectName("CurrentRepoCombo")
        self.CurrentRepoCombo.addItem("")
        self.CurrentRepoCombo.addItem("")
        self.CurrentRepoCombo.addItem("")
        self.verticalLayout.addWidget(self.CurrentRepoCombo)
        self.MainTabWidget = QtWidgets.QTabWidget(self.widget2)
        self.MainTabWidget.setMinimumSize(QtCore.QSize(50, 381))
        self.MainTabWidget.setObjectName("MainTabWidget")
        self.changes_tab = QtWidgets.QWidget()
        self.changes_tab.setObjectName("changes_tab")
        self.MainTabWidget.addTab(self.changes_tab, "")
        self.history_tab = QtWidgets.QWidget()
        self.history_tab.setObjectName("history_tab")
        self.MainTabWidget.addTab(self.history_tab, "")
        self.verticalLayout.addWidget(self.MainTabWidget)
        self.summaryEnt = QtWidgets.QLineEdit(self.widget2)
        self.summaryEnt.setMinimumSize(QtCore.QSize(50, 33))
        self.summaryEnt.setObjectName("summaryEnt")
        self.verticalLayout.addWidget(self.summaryEnt)
        self.DescriptionTextEdit = QtWidgets.QTextEdit(self.widget2)
        self.DescriptionTextEdit.setMinimumSize(QtCore.QSize(50, 131))
        self.DescriptionTextEdit.setObjectName("DescriptionTextEdit")
        self.verticalLayout.addWidget(self.DescriptionTextEdit)
        self.commitBtn = QtWidgets.QPushButton(self.widget2)
        self.commitBtn.setMinimumSize(QtCore.QSize(50, 31))
        self.commitBtn.setObjectName("commitBtn")
        self.verticalLayout.addWidget(self.commitBtn)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(290, 0, 571, 52))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget3)
        self.pushButton.setMinimumSize(QtCore.QSize(280, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(281, 51))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(280, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(281, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget5 = QtWidgets.QWidget(self.centralwidget)
        self.widget5.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget5.setObjectName("widget5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menuFile)
        self.menuAdd.setObjectName("menuAdd")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuRepository = QtWidgets.QMenu(self.menubar)
        self.menuRepository.setObjectName("menuRepository")
        MainWindow.setMenuBar(self.menubar)
        self.actionClone_repository = QtWidgets.QAction(MainWindow)
        self.actionClone_repository.setObjectName("actionClone_repository")
        self.actionCreate_new_Repository = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_Repository.setObjectName("actionCreate_new_Repository")
        self.actionAdd_existing_repository = QtWidgets.QAction(MainWindow)
        self.actionAdd_existing_repository.setObjectName("actionAdd_existing_repository")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAdd.addAction(self.actionClone_repository)
        self.menuAdd.addAction(self.actionCreate_new_Repository)
        self.menuAdd.addAction(self.actionAdd_existing_repository)
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuRepository.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.CurrentRepoCombo.setCurrentIndex(0)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">No Local Changes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">There are no uncommited changes in this repository. Here are some </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">friendly suggestions for what to do next.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Open the repository in your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">default external editor.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Select your editor in Options menu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.openRepoInEditorBtn.setText(_translate("MainWindow", "Open in Visual Studio Code"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">View the files of your repository in Explorer</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Open repo in explorer</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.showInExplorerBtn.setText(_translate("MainWindow", "Show in Explorer"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Open the repository page on GitHub</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the GitHub Page of the Repo on your browser.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.viewOnGitBtn.setText(_translate("MainWindow", "View On GitHub"))
        self.histUserLabel.setText(_translate("MainWindow", "Login user"))
        self.histhashLabel.setText(_translate("MainWindow", "Hash"))
        self.histchandedFilesLable.setText(_translate("MainWindow", "x changed Files"))
        self.histhideWhiteCheck.setText(_translate("MainWindow", "Hide white spaces"))
        self.histCommitMessgLabel.setText(_translate("MainWindow", "Commit message..."))
        __sortingEnabled = self.histFileslistWidget.isSortingEnabled()
        self.histFileslistWidget.setSortingEnabled(False)
        item = self.histFileslistWidget.item(0)
        item.setText(_translate("MainWindow", "Golo "))
        item = self.histFileslistWidget.item(1)
        item.setText(_translate("MainWindow", "Molo"))
        item = self.histFileslistWidget.item(2)
        item.setText(_translate("MainWindow", "Sholo"))
        self.histFileslistWidget.setSortingEnabled(__sortingEnabled)
        self.CurrentRepoCombo.setItemText(0, _translate("MainWindow", "antony\\nalen"))
        self.CurrentRepoCombo.setItemText(1, _translate("MainWindow", "ale"))
        self.CurrentRepoCombo.setItemText(2, _translate("MainWindow", "chosen"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.changes_tab), _translate("MainWindow", "Changes"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.history_tab), _translate("MainWindow", "History"))
        self.summaryEnt.setPlaceholderText(_translate("MainWindow", "Summary (requred)"))
        self.DescriptionTextEdit.setPlaceholderText(_translate("MainWindow", "Description"))
        self.commitBtn.setText(_translate("MainWindow", "Commit to {brunch}"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuRepository.setTitle(_translate("MainWindow", "Repository"))
        self.actionClone_repository.setText(_translate("MainWindow", "Clone repository"))
        self.actionCreate_new_Repository.setText(_translate("MainWindow", "Create new Repository"))
        self.actionAdd_existing_repository.setText(_translate("MainWindow", "Add existing repository"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))