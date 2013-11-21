#!/usr/bin/env python3

__author__ = 'Muharrem Tayyip Yel'
__verison__ = 1.0

import devtools # For Development

import os
import sys
import codes
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
            QMessageBox.warning(self, 'Uyarı!',
            'Bu sürüm işletim sisteminiz ile uyumlu değil!')
            sys.exit(0)
        
        self.mainTab.tabBar().hide()
        
        home = partial(self.show_tab, 0)
        editor = partial(self.show_tab, 1)
        
        self.homeB.clicked.connect(home)
        self.editorB.clicked.connect(editor)
        
        self.createB.clicked.connect(self.create_project_dialog)
        
        
    def show_tab(self, index):
        self.mainTab.setCurrentIndex(index)
        
    def log(self, exception, information):
        file = strftime('%Y-%m-%d %H:%M:%S', gmtime())
        log = exception + information
        with open('./logs/' + file, 'w', encoding = 'utf-8') as f:
            f.write(log)
        
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
            directory = QFileDialog.getExistingDirectory(pro,
                'Proje Dizini', pro.dirL.text(), opt)
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
            err = '<b>{} alfanümerik olmalıdır.</b><br><br>*alfanümerik: ' + \
            'işaretler ve boşluk dışındaki karakterleri içerir.'
            if not pro.nameL.text().isalnum():
                QMessageBox.warning(pro, 'Hatalı Proje Adı', 
                err.format('Proje adı'))
                return
                
            elif not pro.sourceL.text().isalnum():
                QMessageBox.warning(pro, 'Hatalı Kaynak Dosyası Adı', 
                err.format('Kaynak dosyası adı'))
                return
            
            dir = pro.dirL.text() + '/' + pro.nameL.text()
            try: # [mkdir]
                os.mkdir(dir)
                
            except FileExistsError:
                print('Dosya var...')
            
            except PermissionError:
                QMessageBox.warning(pro, 'Hata!', 'Proje dosyası ' + \
                'oluşturulamıyor. Lütfen erişim izni olan bir dizin seçin.')
                return  
              
            except Exception as err:
                QMessageBox.warning(pro, 'Hata!', 'Bilinmeyen hata! Teknik'+\
                ' destek için: <b>menü çubuğu -> yardım -> sorun bildir</b>'+\
                ' yolunu izleyin.')
                inf = ('Proje ismi:', pro.nameL.text(), '\nProje Dizini:',
                pro.dirL.text(), '\nSınıf ismi:', pro.classL.text(),
                '\nPencere Türü:', pro.wtBox.currentText(), 
                '\nKomut Dosyası:', pro.sourceL.text())
                
                self.log('Hata [mkdir]: ' + str(err),
                '\n\nBilgi: {}'.format(inf))
                return         
            
            u = getuser() # user name
            c = pro.classL.text() # class name
            i = pro.instL.text() # Instantiation
            w = pro.wtBox.currentText() # window type
            file = dir + '/' + pro.sourceL.text()+'.py'
            with open(file, 'w', encoding = 'utf-8') as f:
                if self.rb1.isChecked():
                    code = codes.python.format(u)
                elif self.rb2.isChecked() and i == '':
                    code = codes.python_class.format(u, c)
                elif self.rb2.isChecked():
                    code = codes.python_class_inst.format(u, c, i, i)
                elif self.rb3.isChecked():
                    code = codes.pyside.format(u, w)
                else:
                    code = codes.pyside_class.format(u, c, w, c, c)
                    
                f.write(code)
            
            pro.close()
            
        
        pro.dirL.textChanged.connect(check_state)
        pro.createB.clicked.connect(create_project)
        pro.dirB.clicked.connect(set_dir)
        pro.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
