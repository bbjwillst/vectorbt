import os
from utils.GlobalPaths import g_analyzed_path, g_data_path, g_log_path


class FileExt:
    def __init__(self):
        self.analyzedFile = {'path': g_analyzed_path, 'ext': '.xlsx'}
        self.dataFile = {'path': g_data_path, 'ext': '.csv'}
        self.logFile = {'path': g_log_path, 'ext': '.txt'}

    def delete(self, filename='', filetype='.csv', path='datas/'):
        fullname = path + filename + filetype
        if os.path.exists(fullname):
            os.remove(fullname)

    def deleteallfiles(self):
        # analyzed directory
        for root, dirs, files in os.walk(self.analyzedFile['path']):
            for file in files:
                fullpath = root+file
                if os.path.exists(fullpath):
                    os.remove(fullpath)

        # data directory
        for root, dirs, files in os.walk(self.dataFile['path']):
            for file in files:
                fullpath = root+file
                if os.path.exists(fullpath):
                    os.remove(fullpath)

        # log directory
        for root, dirs, files in os.walk(self.logFile['path']):
            for file in files:
                fullpath = root+file
                if os.path.exists(fullpath):
                    os.remove(fullpath)