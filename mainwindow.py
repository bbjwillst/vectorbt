import sys
from PyQt6.QtWidgets import (QLabel, QLineEdit, QPushButton, QGridLayout, QApplication, QDialog)
from vectorbt.data.base import DataT

from utils.CollectEngine import CollectEngine as ce
from utils.AnalyzeEngine import AnalyzeEngine as ae
from strategies.strategy import Strategy as st
from utils import FileExt


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # ID
        self.id = QLabel('代码')
        self.idEdit = QLineEdit()

        # NAME
        self.name = QLabel('名称')
        self.nameEdit = QLineEdit()

        # QUERY
        self.qryName = '查询'
        self.qryBtn = QPushButton(self.qryName)
        self.qryBtn.clicked.connect(self.qryBtn_clicked)

        # DRAW
        self.drawName = '绘图'
        self.drawBtn = QPushButton(self.drawName)
        self.drawBtn.clicked.connect(self.drawBtn_clicked)

        # DELETE
        self.dltName = '删除'
        self.dltBtn = QPushButton(self.dltName)
        self.dltBtn.clicked.connect(self.dltBtn_clicked)

        # WINDOW
        self.setWindowTitle('VectorBT')
        self.resize(300, 200)

        self.initui()

    def initui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.id, 1, 0)
        grid.addWidget(self.idEdit, 1, 1)
        grid.addWidget(self.name, 2, 0)
        grid.addWidget(self.nameEdit, 2, 1)
        grid.addWidget(self.qryBtn, 3, 0)
        grid.addWidget(self.drawBtn, 3, 1)
        grid.addWidget(self.dltBtn, 3, 2)

        self.setLayout(grid)

    def qryBtn_clicked(self):
        """
        1. Retrieve data using tushare
        2. Analyze data by SMA/MACD
        3. Return the highest value
        :return:
        """
        stock_id = self.idEdit.text()
        ce.Stocks.getfulldatabystockid(stock_id)
        st.SMA(stock_id)
        ae.totalreturn(stock_id)
        # print(f"查询【{stock_id}】成功!")

    def drawBtn_clicked(self):
        stock_id = self.idEdit.text()
        df: DataT = ce.Stocks.getohlcvdatabystockid(stock_id)
        df.plot()

    def dltBtn_clicked(self):
        fe = FileExt.FileExt()
        fe.deleteallfiles()
        print("删除成功!")


def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
