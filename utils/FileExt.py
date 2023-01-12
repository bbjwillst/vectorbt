import os
import linecache

class FileExt:
    def __init__(self):
        pass

    def delete(self, filename='', filetype='.csv', path='datas/'):
        fullname = path + filename + filetype
        if os.path.exists(fullname):
            os.remove(fullname)
