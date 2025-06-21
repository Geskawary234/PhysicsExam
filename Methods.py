import sys
from os import path

def resource_path(relative_path):
    """ Get absolute path to resource (compatible with PyInstaller) """
    if hasattr(sys, '_MEIPASS'):
        return path.join(sys._MEIPASS, relative_path)
    return path.join(path.abspath("."), relative_path)
