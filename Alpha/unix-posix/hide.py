#!/usr/bin/env python3

__author__ = 'Muharrem Tayyip Yel'
__version__ = 0.1

import devtools # For Development

import os
import sys
import imp
import codes
import styles
import messages as msgs
from getpass import getuser
from functools import partial
from time import strftime, gmtime

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        if os.name != 'posix':
            self.warning(self, 'Uyarı!', msgs.e1, '')
            sys.exit(0)
        
        self.editors = []
        self.project = '' 
        self.openprojects = []
        self.currentproject = ''
        self.username = getuser()
        self.userdir = os.path.expanduser("~")

        #self.test()
        self.mainTab.tabBar().hide()
        
        home = partial(self.show_tab, 0)
        editor = partial(self.show_tab, 1)
        
        self.homeB.clicked.connect(home)
        self.editorB.clicked.connect(editor)
        self.createB.clicked.connect(self.create_project_dialog)
        self.openB.clicked.connect(self.open_project_dialog)

    def test(self):
        pass
        
    def show_tab(self, index):
        self.mainTab.setCurrentIndex(index)
             
    def openw(self, file, write):
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(write)
        
    def openr(self, file, readlines):
        with open(file, 'r', encoding = 'utf-8') as f:
            read = f.readlines() if readlines else f.read()
            return read
    
    def log(self, tag, exception, information):
        file = strftime('%Y-%m-%d %H:%M:%S', gmtime())
        log = 'Hata %s: ' %(tag) + exception + '\n\nBilgi: ' + information
        with open('./logs/' + file, 'w', encoding = 'utf-8') as f:
            f.write(log)
            
    def warning(self, parent, title, message, buttons):
        msgBox = QMessageBox(parent)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setIcon(msgBox.Warning)
        for b in buttons:
            msgBox.addButton(b[0], b[1])
        
        msgBox.show()
        ret = msgBox.exec_()
        return ret
        
    ''' 
    def contextMenuEvent(self, event): # FIXME
        menu = QMenu("Popup Submenu", self)
        act = QAction('Deneme', self)
        menu.addAction(act)
        menu.exec_(event.globalPos())
    '''
            
    def editor_skills(self): # FIXME
        print('...', end = ' ')
        for e in self.editors:
            pass  

    def open_project_dialog(self):
        file = QFileDialog.getOpenFileName(self, 'Proje Aç', self.userdir,
                                           'Hammer IDE Projeleri (*.hammer)',
                                           '', QFileDialog.Options())
        if file[0]:
            self.project = file[0]
            self.open_project()

    def open_project(self):
        self.currentproject = imp.load_source(self.project, self.project)
        if self.project in self.openprojects:
            self.editorB.setEnabled(True)
            self.mainTab.setCurrentIndex(1)
            message = '<b>{}</b> adlı proje zaten açık'
            message = message.format(self.currentproject.project_name)
            QMessageBox.critical(self, 'Hata!', message)
            return

        dir = self.project[:self.project.rfind('/')] + '/'
        
        item = QTreeWidgetItem(self.trw)
        item.setText(0, self.currentproject.project_name)
        item.setIcon(0, QIcon('./images/icon.png'))
        for file in self.currentproject.files: # FIXME
            child = QTreeWidgetItem()
            child.setText(0, file)
            icon = 'icon.png' if os.path.isfile(dir + file) else 'folder.png'
            child.setIcon(0, QIcon('./images/' + icon))
            item.addChild(child)

        for file in self.currentproject.open_files:
            tab = QWidget()
            self.tw.addTab(tab, file)
            te = QTextEdit(tab)
            gl = QGridLayout(tab)
            gl.addWidget(te, 0, 0)
            self.editors.append(te)
            te.textChanged.connect(self.editor_skills)
            te.setLineWrapMode(QTextEdit.NoWrap)
            te.setStyleSheet(styles.editor)
            te.setText(self.openr(dir + file, False))
            
        self.openprojects.append(self.project)
        
        self.editorB.setEnabled(True)
        self.mainTab.setCurrentIndex(1)
        self.trw.setItemExpanded(item, True)
        
    def create_project_dialog(self):
        loader = QUiLoader()
        f = QFile('./ui/createproject.ui')
        f.open(QFile.ReadOnly)
        f.close()
        pro = loader.load(f, self)
        pro.lbl2_2.hide()
        pro.instL.hide()
        
        if self.rb1.isChecked():
            pro.lbl2.hide()
            pro.lbl3.hide()
            pro.classL.hide()
            pro.wtBox.hide()
        elif self.rb2.isChecked():
            pro.lbl3.hide()
            pro.wtBox.hide()
            pro.lbl2_2.show()
            pro.instL.show()
        elif self.rb3.isChecked():
            pro.lbl2.hide()
            pro.classL.hide()
            
        pro.adjustSize()
        
        def set_dir():
            opt = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
            directory = QFileDialog.getExistingDirectory(pro, 'Proje Dizini',
                                                         pro.dirL.text(), opt)
            if directory:
                pro.dirL.setText(directory)
                
        def check_state():
            try:
                dirr = pro.dirL.text()
                os.stat(dirr)
                if os.path.isfile(dirr):
                    raise FileNotFoundError
                pro.dirL.setStyleSheet('color: rgb(0, 0, 0)')
                pro.createB.setEnabled(True)
            except FileNotFoundError:
                pro.dirL.setStyleSheet('color: rgb(255, 0, 0)')
                pro.createB.setEnabled(False)
        
        def create_project():
            n1 = pro.sourceL.text() # script name
            n2 = pro.nameL.text() # project name
            d = pro.dirL.text() # project directory
            s = pro.sourceL.text() # script name
            c = pro.classL.text() # class name
            i = pro.instL.text() # instantiation
            w = pro.wtBox.currentText() # window type
            p = pro.versionB.currentText() # version
            v, py3 = ['', False] if p.endswith('2') else ['3', True]
            u = self.username # user name
            dir = d + '/' + n2
            script = dir + '/' + n1 + '.py'
            
            if not n2.isalnum():
                self.warning(pro, 'Hatalı Proje Adı',
                             msgs.w1.format('Proje adı'), '')
                return
            elif not n1.isalnum():
                self.warning(pro, 'Hatalı Kaynak Dosyası Adı',
                             msgs.w1.format('Kaynak dosyası adı'), '')
                return

            n1 += '.py'
            
            try: # [mkdir]
                os.mkdir(dir)
            except FileExistsError:
                print('Dosya var...')
            except PermissionError:
                self.warning(pro, 'Hata!', msgs.e2, '')
                return  
            except Exception as err:
                self.warning(pro, 'Hata!', msgs.e3, '')
                inf = msgs.i1.format(n2, d, c, i, w, pro.sourceL.text())
                self.log('mkdir', str(err), msgs.i1.format(n2, d, c, i, w, s))
                return         

            if self.rb1.isChecked():
                code = codes.python.format(v, u)
            elif self.rb2.isChecked() and i == '':
                code = codes.python_class.format(v, u, c)
            elif self.rb2.isChecked():
                code = codes.python_class_inst.format(v, u, c, i, i)
            elif self.rb3.isChecked():
                code = codes.pyside.format(v, u, w)
            else:
                code = codes.pyside_class.format(v, u, c, w, c, c)
                    
            self.openw(script, code)
            self.project = dir + '/' + n2 + '.hammer'
            self.openw(self.project, codes.hide_pro.format(n2, py3, n1, n1))
            self.open_project()
            pro.close()
            
        pro.dirL.textChanged.connect(check_state)
        pro.createB.clicked.connect(create_project)
        pro.dirB.clicked.connect(set_dir)
        pro.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())
