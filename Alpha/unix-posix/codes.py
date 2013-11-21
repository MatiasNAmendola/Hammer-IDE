__author__ = 'Muharrem Tayyip Yel'
__version__ = 0.1

python_script = """#!/usr/bin/env python3

__author__ = "{}"

"""

python_class = """#!/usr/bin/env python3

__author__ = "{}"
__version__ = 0.1

class {}:
    def __init__(self):
        pass
"""

pyside = """#!/usr/bin/env python3

__author__ = "{}"
__version__ = 0.1

import sys

from PySide import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.{}()


window.show()
sys.exit(app.exec_()) 
"""

pyside_class = """#!/usr/bin/env python3

__author__ = "{}"
__version__ = 0.1

import sys

from PySide import QtGui

class {}:
"""
# more..
