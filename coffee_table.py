import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

        reader = self.cur.execute(f"""SELECT * FROM Coffee""").fetchall()

        reader.sort(key=lambda x: x[1].isalpha())

        title = ['ID', 'Название сорта', 'Степень обжарки', 'Тип', 'Описание вкуса', 'Цена', 'Объем']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)

        for i in reader:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(7):
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, j, QTableWidgetItem(str(i[j])))
        self.tableWidget.resizeColumnsToContents()

        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())