# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Sun Nov 24 12:31:14 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeB = QtGui.QToolButton(self.centralwidget)
        self.homeB.setMinimumSize(QtCore.QSize(45, 40))
        self.homeB.setMaximumSize(QtCore.QSize(45, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/Home_icon_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeB.setIcon(icon1)
        self.homeB.setIconSize(QtCore.QSize(30, 30))
        self.homeB.setAutoRaise(True)
        self.homeB.setObjectName("homeB")
        self.verticalLayout.addWidget(self.homeB)
        self.editorB = QtGui.QToolButton(self.centralwidget)
        self.editorB.setEnabled(False)
        self.editorB.setMinimumSize(QtCore.QSize(45, 40))
        self.editorB.setMaximumSize(QtCore.QSize(45, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/edit_property-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editorB.setIcon(icon2)
        self.editorB.setIconSize(QtCore.QSize(28, 28))
        self.editorB.setAutoRaise(True)
        self.editorB.setObjectName("editorB")
        self.verticalLayout.addWidget(self.editorB)
        self.toolButton_3 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_3.setMinimumSize(QtCore.QSize(45, 40))
        self.toolButton_3.setMaximumSize(QtCore.QSize(45, 40))
        self.toolButton_3.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout.addWidget(self.toolButton_3)
        self.settingsB = QtGui.QToolButton(self.centralwidget)
        self.settingsB.setMinimumSize(QtCore.QSize(45, 40))
        self.settingsB.setMaximumSize(QtCore.QSize(45, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/saydamTema/derle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsB.setIcon(icon3)
        self.settingsB.setIconSize(QtCore.QSize(35, 35))
        self.settingsB.setAutoRaise(True)
        self.settingsB.setObjectName("settingsB")
        self.verticalLayout.addWidget(self.settingsB)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.runB = QtGui.QToolButton(self.centralwidget)
        self.runB.setEnabled(False)
        self.runB.setMinimumSize(QtCore.QSize(45, 40))
        self.runB.setMaximumSize(QtCore.QSize(45, 40))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/saydamTema/dene.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runB.setIcon(icon4)
        self.runB.setIconSize(QtCore.QSize(35, 35))
        self.runB.setAutoRaise(True)
        self.runB.setObjectName("runB")
        self.verticalLayout.addWidget(self.runB)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.mainTab = QtGui.QTabWidget(self.centralwidget)
        self.mainTab.setTabPosition(QtGui.QTabWidget.South)
        self.mainTab.setTabShape(QtGui.QTabWidget.Triangular)
        self.mainTab.setDocumentMode(False)
        self.mainTab.setObjectName("mainTab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rb1 = QtGui.QRadioButton(self.tab)
        self.rb1.setChecked(True)
        self.rb1.setObjectName("rb1")
        self.verticalLayout_2.addWidget(self.rb1)
        self.rb2 = QtGui.QRadioButton(self.tab)
        self.rb2.setObjectName("rb2")
        self.verticalLayout_2.addWidget(self.rb2)
        self.rb3 = QtGui.QRadioButton(self.tab)
        self.rb3.setObjectName("rb3")
        self.verticalLayout_2.addWidget(self.rb3)
        self.rb4 = QtGui.QRadioButton(self.tab)
        self.rb4.setObjectName("rb4")
        self.verticalLayout_2.addWidget(self.rb4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 2, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 3, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 2)
        spacerItem6 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 6, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 6, 1, 1)
        self.lastB = QtGui.QCommandLinkButton(self.tab)
        self.lastB.setMinimumSize(QtCore.QSize(140, 35))
        self.lastB.setMaximumSize(QtCore.QSize(140, 35))
        self.lastB.setObjectName("lastB")
        self.gridLayout.addWidget(self.lastB, 4, 8, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 9, 1, 1)
        self.createB = QtGui.QPushButton(self.tab)
        self.createB.setMinimumSize(QtCore.QSize(110, 30))
        self.createB.setMaximumSize(QtCore.QSize(110, 30))
        self.createB.setObjectName("createB")
        self.gridLayout.addWidget(self.createB, 4, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 4, 7, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 5, 8, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 4, 2, 1)
        self.openB = QtGui.QPushButton(self.tab)
        self.openB.setMinimumSize(QtCore.QSize(100, 30))
        self.openB.setMaximumSize(QtCore.QSize(100, 30))
        self.openB.setObjectName("openB")
        self.gridLayout.addWidget(self.openB, 4, 5, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 5, 1, 1, 1)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 2, 1, 7)
        self.mainTab.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtGui.QSplitter(self.tab_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tw = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw.sizePolicy().hasHeightForWidth())
        self.tw.setSizePolicy(sizePolicy)
        self.tw.setMinimumSize(QtCore.QSize(0, 0))
        self.tw.setDocumentMode(True)
        self.tw.setTabsClosable(True)
        self.tw.setMovable(True)
        self.tw.setObjectName("tw")
        self.trw = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trw.sizePolicy().hasHeightForWidth())
        self.trw.setSizePolicy(sizePolicy)
        self.trw.setMaximumSize(QtCore.QSize(300, 16777215))
        self.trw.setObjectName("trw")
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        self.mainTab.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.mainTab.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.mainTab, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Hammer IDE", None, QtGui.QApplication.UnicodeUTF8))
        self.homeB.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.editorB.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsB.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.runB.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.rb1.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Basit bir python komut dosyası oluşturur.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rb1.setText(QtGui.QApplication.translate("MainWindow", "Python kaynak dosyası", None, QtGui.QApplication.UnicodeUTF8))
        self.rb2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Basit bir python komut dosyası (sınıf kullanarak) oluşturur. Sınıf ismini bir sonraki adımda belirleyebilirsiniz.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rb2.setText(QtGui.QApplication.translate("MainWindow", "Python sınıfı", None, QtGui.QApplication.UnicodeUTF8))
        self.rb3.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Basit bir PySide uygulaması oluşturur. Pencere türünü bir sonraki adımda belirleyebilirsiniz.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rb3.setText(QtGui.QApplication.translate("MainWindow", "PySide", None, QtGui.QApplication.UnicodeUTF8))
        self.rb4.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Basit bir PySide uygulaması (sınıf kullanarak) oluşturur. Sınıf adını ve pencere türünü bir sonraki adımda belirleyebilirsiniz.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.rb4.setText(QtGui.QApplication.translate("MainWindow", "PySide sınıfı", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#434343;\">Hızlı Başlangıç</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lastB.setText(QtGui.QApplication.translate("MainWindow", "Son Projeyi Aç", None, QtGui.QApplication.UnicodeUTF8))
        self.createB.setText(QtGui.QApplication.translate("MainWindow", "Proje Oluştur", None, QtGui.QApplication.UnicodeUTF8))
        self.openB.setText(QtGui.QApplication.translate("MainWindow", "Proje Aç", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.trw.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Projeler", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Python", None, QtGui.QApplication.UnicodeUTF8))

