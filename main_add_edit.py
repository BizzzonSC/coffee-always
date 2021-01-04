import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.pushButton_2.clicked.connect(self.hhh)
        self.pushButton.clicked.connect(self.hhh1)

    def hhh(self):
        e1 = self.lineEdit.text()
        e2 = self.lineEdit_2.text()
        e3 = self.lineEdit_3.text()
        e4 = self.lineEdit_4.text()
        e5 = self.lineEdit_5.text()
        e6 = self.lineEdit_6.text()
        e7 = self.lineEdit_7.text()
        if e1 != '' and e2 != '' and e3 != '' and e4 != '' and e5 != '' and e6 != '' and e7 != '':
            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            print(e1, e2, e3, e4, e5, e6, e7)
            cur.execute("""INSERT INTO Coffe('id', 'name of the variety', 'degree of roasting', 'Type', 'description of taste', 'price', 'volume of packaging') VALUES ((?), (?), (?), (?), (?), (?), (?))""", [e1, e2, e3, e7, e6, e5, e4])
        else:
            self.pushButton_2.setText(("Добавить (Не заполнено)"))

    def hhh1(self):
        e = self.lineEdit_15.text()
        e1 = self.lineEdit_8.text()
        e2 = self.lineEdit_9.text()
        e3 = self.lineEdit_10.text()
        e4 = self.lineEdit_11.text()
        e5 = self.lineEdit_12.text()
        e6 = self.lineEdit_13.text()
        e7 = self.lineEdit_14.text()
        if e1 != '' and e2 != '' and e3 != '' and e4 != '' and e5 != '' and e6 != '' and e7 != '':
            con = sqlite3.connect('coffe.sqlite')
            cur = con.cursor()
            print(e1, e2, e3, e4, e5, e6, e7)
            cur.execute("""UPDATE Coffe SET 'id' = (?), 'name of the variety' = (?), 'degree of roasting' = (?), 'Type' = (?), 'description of taste' = (?), 'price' = (?), 'volume of packaging' = (?) WHERE 'id' = (?)""", [e1, e2, e3, e7, e6, e5, e4, e])
        else:
            self.pushButton.setText(("Изменить (Не заполнено)"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())