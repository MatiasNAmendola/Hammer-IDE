__author__ = 'Muharrem Tayyip Yel'
__version__ = 0.1

python = """#!/usr/bin/env python{}

__author__ = "{}"

"""

python_class = """#!/usr/bin/env python{}

__author__ = "{}"
__version__ = 0.1

class {}(object):
    def __init__(self):
        pass
"""

python_class_inst = """#!/usr/bin/env python{}

__author__ = "{}"
__version__ = 0.1

class {}({}):
    def __init__(self):
        {}.__init__(self)
        pass
"""

pyside = """#!/usr/bin/env python{}

__author__ = "{}"
__version__ = 0.1

import sys

from PySide import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.{}()


window.show()
sys.exit(app.exec_()) 
"""

pyside_class = """#!/usr/bin/env python{}

__author__ = "{}"
__version__ = 0.1

import sys

from PySide import QtGui

class {}(QtGui.{}):
    def __init__(self, parent=None):
        super({}, self).__init__(parent)
        pass
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = {}()
    window.show()
    sys.exit(app.exec_())
"""

hide_pro = """# Hammer IDE Project File

project_name = "{}"
python3 = {}
files = ["{}"]
open_files = ["{}"]
"""
