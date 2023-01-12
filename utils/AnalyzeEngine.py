import os
import pandas as pd
from utils.FileExt import FileExt as fe

class AnalyzeEngine:
    @staticmethod
    def totalreturn(filename='', filetype='.txt'):
        path = 'logs/'
        log_lines = []
        log_lines1 = []
        fullname = path + filename + filetype
        if os.path.exists(fullname):
            f = open(fullname, 'r')
            lines = f.readlines()
            line_count = len(lines)
            i = 1

            while i <= line_count:
                line_text = lines[i].rstrip()
                line_text_items = line_text.split(' ')
                lst = []
                [lst.append(_) for _ in line_text_items if len(_) != 0]
                lst.remove('close')
                lst = list(map(float, lst))
                log_lines.append(lst)
                i += 3

            f.close()

        for _ in log_lines:
            if len(_) == 2:
                lst = _
                log_lines.remove(_)
                lst.insert(1, lst[0])
                log_lines.append(lst)


        for _ in log_lines:
            # fast < slow
            if _[0] < _[1]:
                log_lines1.append(_)


        f = fe()
        f.delete(filename=filename, filetype='.xlsx', path='analyzed/')
        df: pd.DataFrame = pd.DataFrame(log_lines1, columns=['fast', 'slow', 'retval'])

        df = df.sort_values(by=['retval'], ascending=False)
        df.to_excel("analyzed/{}.xlsx".format(filename), index=False)
