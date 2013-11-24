__author__ = 'Muharrem Tayyip Yel'
__version__ = 0.1

import os

os.system('pyside-uic ui/main.ui > ui_main.py')
print('devtools: ui dosyası çevirildi...')

with open('ui_main.py', 'r', encoding = 'utf-8') as f:
    read = f.read()

with open('ui_main.py', 'w', encoding = 'utf-8') as f:
    write = read.replace('../images/', './images/')
    f.write(write)
    
print('devtools: simge dizinleri ayarlandı.')
