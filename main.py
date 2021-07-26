# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.group = QtWidgets.QWidget()
        self.group.setObjectName("group")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.group)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.add_group = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_group.setObjectName("add_group")
        self.verticalLayout.addWidget(self.add_group)
        self.del_group = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.del_group.setObjectName("del_group")
        self.verticalLayout.addWidget(self.del_group)
        self.tabWidget.addTab(self.group, "")
        self.students = QtWidgets.QWidget()
        self.students.setObjectName("students")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.students)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.add_group_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.add_group_2.setObjectName("add_group_2")
        self.verticalLayout_2.addWidget(self.add_group_2)
        self.del_group_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.del_group_2.setObjectName("del_group_2")
        self.verticalLayout_2.addWidget(self.del_group_2)
        self.tabWidget.addTab(self.students, "")
        self.object = QtWidgets.QWidget()
        self.object.setObjectName("object")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.object)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 791, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.add_group_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.add_group_3.setObjectName("add_group_3")
        self.verticalLayout_3.addWidget(self.add_group_3)
        self.del_group_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.del_group_3.setObjectName("del_group_3")
        self.verticalLayout_3.addWidget(self.del_group_3)
        self.tabWidget.addTab(self.object, "")
        self.change = QtWidgets.QWidget()
        self.change.setObjectName("change")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.change)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 791, 311))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_4)
        self.add_group_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.add_group_4.setObjectName("add_group_4")
        self.verticalLayout_4.addWidget(self.add_group_4)
        self.tabWidget.addTab(self.change, "")
        self.reprimands = QtWidgets.QWidget()
        self.reprimands.setObjectName("reprimands")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.reprimands)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 791, 311))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.verticalLayoutWidget_5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget_5)
        self.tabWidget.addTab(self.reprimands, "")
        self.candidates = QtWidgets.QWidget()
        self.candidates.setObjectName("candidates")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.candidates)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 791, 311))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.verticalLayoutWidget_6)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_6)
        self.tabWidget.addTab(self.candidates, "")
        self.finder = QtWidgets.QLineEdit(self.centralwidget)
        self.finder.setGeometry(QtCore.QRect(820, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finder.setFont(font)
        self.finder.setObjectName("finder")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(850, 30, 141, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 180, 231, 81))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учёт результатов сдачи экзаменов студентами"))
        self.add_group.setText(_translate("MainWindow", "Добавить группу"))
        self.del_group.setText(_translate("MainWindow", "Удалить группу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.group), _translate("MainWindow", "Группа"))
        self.add_group_2.setText(_translate("MainWindow", "Добавить студента"))
        self.del_group_2.setText(_translate("MainWindow", "Удалить студента"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.students), _translate("MainWindow", "Студенты"))
        self.add_group_3.setText(_translate("MainWindow", "Добавить предмет"))
        self.del_group_3.setText(_translate("MainWindow", "Удалить предмет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.object), _translate("MainWindow", "Предметы"))
        self.add_group_4.setText(_translate("MainWindow", "Добавить сдачу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change), _translate("MainWindow", "Сдачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reprimands), _translate("MainWindow", "Выговоры"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.candidates),
                                  _translate("MainWindow", "Кандидаты на отчисление"))
        self.finder.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">Найти студента:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Закрыть"))
        self.action_5.setText(_translate("MainWindow", "Выйти"))


class Dialog(QWidget):  # класс для открытия окон изменения данных
    def __init__(self):
        super().__init__()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_deleted_db = False

        """прописываем действия для кнопок открыть и закрыть бд"""
        self.action.triggered.connect(
            lambda: self.clicked(QFileDialog.getOpenFileName(self, 'Выбрать базу данных', '')[0]))
        self.action_3.triggered.connect(lambda: self.delete_db())

        """привязываем функционал к кнопкам"""

        """кнопки добавления/удаления групп"""
        self.add_group.clicked.connect(self.add_func)
        self.del_group.clicked.connect(self.delete_func)

        """кнопки добавления/удаления студентов"""
        self.add_group_2.clicked.connect(self.add_func2)
        self.del_group_2.clicked.connect(self.delete_func2)

        """кнопки добавления/удаления предметов"""
        self.add_group_3.clicked.connect(self.add_func3)
        self.del_group_3.clicked.connect(self.delete_func3)

        """кнопка добавления сдачи"""
        self.add_group_4.clicked.connect(self.add_func4)

        self.pushButton.clicked.connect(self.find_student)

        # значит таблица кликабельна (можно нажать на граппу и удалить её)
        self.tableWidget.cellClicked.connect(self.cellClick)

        # подключаемся к бд и заполняем таблицу данными из базы
        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, group_name FROM 'group'"

        # выполнили запрос, теперь будет заполнять таблицу с группами
        self.table_groups = self.cur.execute(self.sql).fetchall()

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.table_groups))
        self.tableWidget.setColumnWidth(0, 370)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название группы"])

        # заполняем таблицу с группами в фицле построчно
        for s, c in enumerate(self.table_groups):
            self.tableWidget.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget.setItem(s, 1, QTableWidgetItem(str(c[1])))

        # указываем, что таблица со студентами тоже кликабельна
        self.tableWidget_2.cellClicked.connect(self.cellClick)

        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, group_name, credits FROM 'students_info'"

        self.table_stud = self.cur.execute(self.sql).fetchall()
        # получили данные из базы о студентах, теперь заполняем построчно таблицу
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(len(self.table_stud))
        self.tableWidget_2.setColumnWidth(0, 70)
        self.tableWidget_2.setColumnWidth(1, 160)
        self.tableWidget_2.setColumnWidth(2, 230)
        self.tableWidget_2.setColumnWidth(3, 310)
        self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Имя", 'Группа', 'Выговоры (шт.)'])

        for s, c in enumerate(self.table_stud):
            self.tableWidget_2.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_2.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_2.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_2.setItem(s, 3, QTableWidgetItem(str(c[3])))

        self.tableWidget_3.cellClicked.connect(self.cellClick)
        # таблица с предметами - тоже кликабельна
        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, subject_name FROM 'subjects'"

        self.table_sub = self.cur.execute(self.sql).fetchall()
        # заполняем таблицу с предметами из базы данных
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(len(self.table_sub))
        self.tableWidget_3.setColumnWidth(0, 370)
        self.tableWidget_3.setColumnWidth(1, 400)
        self.tableWidget_3.setHorizontalHeaderLabels(["ID", "Предмет"])

        for s, c in enumerate(self.table_sub):
            self.tableWidget_3.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_3.setItem(s, 1, QTableWidgetItem(str(c[1])))
        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, subject_name, mark FROM 'passing'"

        self.table_passing = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу со сдачами, она также кликабельна
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(len(self.table_passing))
        self.tableWidget_4.setColumnWidth(0, 200)
        self.tableWidget_4.setColumnWidth(1, 200)
        self.tableWidget_4.setColumnWidth(2, 200)
        self.tableWidget_4.setColumnWidth(3, 170)
        self.tableWidget_4.setHorizontalHeaderLabels(["ID", "Студент", "Предмет", "Оценка"])

        for s, c in enumerate(self.table_passing):
            self.tableWidget_4.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_4.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_4.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_4.setItem(s, 3, QTableWidgetItem(str(c[3])))
        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, credits FROM 'students_info'"

        self.table_r = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу с выговорами
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setColumnWidth(0, 250)
        self.tableWidget_5.setColumnWidth(1, 270)
        self.tableWidget_5.setColumnWidth(2, 250)
        self.tableWidget_5.setHorizontalHeaderLabels(["ID", "Студент", "Долгов (шт.)"])
        lst = self.table_r.copy()

        c_ = 0
        for s, c in enumerate(lst):
            if c[2] > 3 and c[2] <= 5:
                c_ += 1
        self.tableWidget_5.setRowCount(c_)

        r = -1
        for s, c in enumerate(lst):
            if c[2] > 3 and c[2] <= 5:
                r += 1
                self.tableWidget_5.setItem(r, 0, QTableWidgetItem(str(c[0])))
                self.tableWidget_5.setItem(r, 1, QTableWidgetItem(str(c[1])))
                self.tableWidget_5.setItem(r, 2, QTableWidgetItem(str(c[2])))

        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, credits FROM 'students_info'"

        self.table_d = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу с кандидатами на отчисление

        lst = self.table_d.copy()
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setHorizontalHeaderLabels(["ID", "Студент", "Долгов (шт.)"])

        count_r = 0
        for s, c in enumerate(lst):
            if c[2] > 5:
                count_r += 1

        self.tableWidget_6.setRowCount(count_r)
        self.tableWidget_6.setColumnWidth(0, 120)
        self.tableWidget_6.setColumnWidth(1, 400)
        self.tableWidget_6.setColumnWidth(2, 250)

        row = -1
        for s, c in enumerate(lst):
            if c[2] > 5:
                row += 1
                self.tableWidget_6.setItem(row, 0, QTableWidgetItem(str(c[0])))
                self.tableWidget_6.setItem(row, 1, QTableWidgetItem(str(c[1])))
                self.tableWidget_6.setItem(row, 2, QTableWidgetItem(str(c[2])))

    def delete_db(self):
        self.flag_deleted_db = True
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_6.setRowCount(0)

    def clicked(self, filename):
        self.flag_deleted_db = False
        """после выбора бд, заполяем все поля в программе"""
        # подключаемся к бд и заполняем таблицу данными из базы
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, group_name FROM 'group'"

        # выполнили запрос, теперь будет заполнять таблицу с группами
        self.table_groups = self.cur.execute(self.sql).fetchall()

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.table_groups))
        self.tableWidget.setColumnWidth(0, 370)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название группы"])

        # заполняем таблицу с группами в фицле построчно
        for s, c in enumerate(self.table_groups):
            self.tableWidget.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget.setItem(s, 1, QTableWidgetItem(str(c[1])))

        # указываем, что таблица со студентами тоже кликабельна
        self.tableWidget_2.cellClicked.connect(self.cellClick)

        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, group_name, credits FROM 'students_info'"

        self.table_stud = self.cur.execute(self.sql).fetchall()
        # получили данные из базы о студентах, теперь заполняем построчно таблицу
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(len(self.table_stud))
        self.tableWidget_2.setColumnWidth(0, 70)
        self.tableWidget_2.setColumnWidth(1, 160)
        self.tableWidget_2.setColumnWidth(2, 230)
        self.tableWidget_2.setColumnWidth(3, 310)
        self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Имя", 'Группа', 'Выговоры (шт.)'])

        for s, c in enumerate(self.table_stud):
            self.tableWidget_2.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_2.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_2.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_2.setItem(s, 3, QTableWidgetItem(str(c[3])))

        self.tableWidget_3.cellClicked.connect(self.cellClick)
        # таблица с предметами - тоже кликабельна
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, subject_name FROM 'subjects'"

        self.table_sub = self.cur.execute(self.sql).fetchall()
        # заполняем таблицу с предметами из базы данных
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(len(self.table_sub))
        self.tableWidget_3.setColumnWidth(0, 370)
        self.tableWidget_3.setColumnWidth(1, 400)
        self.tableWidget_3.setHorizontalHeaderLabels(["ID", "Предмет"])

        for s, c in enumerate(self.table_sub):
            self.tableWidget_3.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_3.setItem(s, 1, QTableWidgetItem(str(c[1])))
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, subject_name, mark FROM 'passing'"

        self.table_passing = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу со сдачами, она также кликабельна
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(len(self.table_passing))
        self.tableWidget_4.setColumnWidth(0, 200)
        self.tableWidget_4.setColumnWidth(1, 200)
        self.tableWidget_4.setColumnWidth(2, 200)
        self.tableWidget_4.setColumnWidth(3, 170)
        self.tableWidget_4.setHorizontalHeaderLabels(["ID", "Студент", "Предмет", "Оценка"])

        for s, c in enumerate(self.table_passing):
            self.tableWidget_4.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_4.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_4.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_4.setItem(s, 3, QTableWidgetItem(str(c[3])))
        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, credits FROM 'students_info'"

        self.table_r = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу с выговорами
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setColumnWidth(0, 250)
        self.tableWidget_5.setColumnWidth(1, 270)
        self.tableWidget_5.setColumnWidth(2, 250)
        self.tableWidget_5.setHorizontalHeaderLabels(["ID", "Студент", "Долгов (шт.)"])
        lst = self.table_r.copy()

        c_ = 0
        for s, c in enumerate(lst):
            if c[2] > 3 and c[2] <= 5:
                c_ += 1
        self.tableWidget_5.setRowCount(c_)

        r = -1
        for s, c in enumerate(lst):
            if c[2] > 3 and c[2] <= 5:
                r += 1
                self.tableWidget_5.setItem(r, 0, QTableWidgetItem(str(c[0])))
                self.tableWidget_5.setItem(r, 1, QTableWidgetItem(str(c[1])))
                self.tableWidget_5.setItem(r, 2, QTableWidgetItem(str(c[2])))

        self.con = sqlite3.connect(filename)
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, credits FROM 'students_info'"

        self.table_d = self.cur.execute(self.sql).fetchall()
        # заполяем таблицу с кандидатами на отчисление

        lst = self.table_d.copy()
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setHorizontalHeaderLabels(["ID", "Студент", "Долгов (шт.)"])

        count_r = 0
        for s, c in enumerate(lst):
            if c[2] > 5:
                count_r += 1

        self.tableWidget_6.setRowCount(count_r)
        self.tableWidget_6.setColumnWidth(0, 120)
        self.tableWidget_6.setColumnWidth(1, 400)
        self.tableWidget_6.setColumnWidth(2, 250)

        row = -1
        for s, c in enumerate(lst):
            if c[2] > 5:
                row += 1
                self.tableWidget_6.setItem(row, 0, QTableWidgetItem(str(c[0])))
                self.tableWidget_6.setItem(row, 1, QTableWidgetItem(str(c[1])))
                self.tableWidget_6.setItem(row, 2, QTableWidgetItem(str(c[2])))

    def find_student(self):
        if not self.flag_deleted_db:
            """по нажати на кнопку ищем студента"""
            self.sql = "SELECT id, student_name, group_name, credits FROM 'students_info' WHERE student_name LIKE '%{}%'".format(
                self.finder.text())
            self.table_users = self.cur.execute(self.sql).fetchall()

            self.tableWidget_2.setColumnCount(4)
            self.tableWidget_2.setRowCount(len(self.table_users))
            self.tableWidget_2.setColumnWidth(0, 70)
            self.tableWidget_2.setColumnWidth(1, 160)
            self.tableWidget_2.setColumnWidth(2, 230)
            self.tableWidget_2.setColumnWidth(3, 310)
            self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Имя", 'Группа', 'Выговоры (шт.)'])

            for s, c in enumerate(self.table_users):
                self.tableWidget_2.setItem(s, 0, QTableWidgetItem(str(c[0])))
                self.tableWidget_2.setItem(s, 1, QTableWidgetItem(str(c[1])))
                self.tableWidget_2.setItem(s, 2, QTableWidgetItem(str(c[2])))
                self.tableWidget_2.setItem(s, 3, QTableWidgetItem(str(c[3])))

    # метод позволяет узнать, кликнули ли на поле или нет
    def cellClick(self, row, col):
        self.row = row
        self.col = col

    def upd_res(self):
        """функия для обовления данных после добавления/удаления групп. Это значит, что после нажатия на кнопку
         сохранить, наша таблица автоматически обновляется и мы не видим уже удаленные данные"""
        self.z = "SELECT id, group_name FROM 'group'"
        all_groups = self.cur.execute(self.z).fetchall()

        self.tableWidget.setRowCount(len(all_groups))
        for s, c in enumerate(all_groups):
            self.tableWidget.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget.setItem(s, 1, QTableWidgetItem(str(c[1])))

    def add_func(self):
        self.adding_group()
        self.upd_res()

    def delete_func(self):
        """функция для удаления группы"""
        try:
            if self.tableWidget.item(self.row, self.col).text():
                # проходимся по таблице, чтобы понять какую группу кликнули
                rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
                names = [self.tableWidget.item(i, 1).text() for i in rows]
                # берем название группы, которую нужно удалить
                ids = [self.tableWidget.item(i, 0).text() for i in rows]
                valid = QMessageBox.question(
                    self, 'Подтверждение удаления',
                    f"Вы точно хотите удалить группу с названием {''.join(names)}?",
                    QMessageBox.Yes, QMessageBox.No)

                if valid == QMessageBox.Yes:  # если согласны, удаляем из базы данных
                    delete_sql = "DELETE FROM 'group' WHERE id = {}".format(''.join(ids))
                    self.cur.execute(delete_sql)
                    self.con.commit()
                    # сохраняем и обновляем таблицу
                    self.upd_res()
                self.upd_res()  # после удаления обновляем таблицу, чтобы не отображались уже удаленные данные
            else:
                self.statusBar().showMessage('Ошибка')
        except Exception as e:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, выберите группу для удаления, кликнув на неё",
                            QMessageBox.Ok)

    def create_new_group(self):
        """обработки нажатия на кнопку сохранить в добалении группы"""
        if self.lineEdit.text():
            NEW_NAME = self.lineEdit.text()
            maxid = self.cur.execute("SELECT id FROM 'group' ORDER BY id").fetchall()[-1]  # выбираем самый последний id
            sql = "INSERT INTO 'group'(id, group_name) VALUES({}, '{}')".format(maxid[0] + 1, NEW_NAME)
            self.cur.execute(sql).fetchall()
            self.con.commit()
            self.upd_res()
            # сохраняем, обновляем таблицу и закрываем диалоговое окно
            # (то есть окно, где мы вводили данные для новой группы)
            self.dialog.close()
        else:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, внимательно вводите данные",
                            QMessageBox.Ok)
            self.dialog.close()

    def adding_group(self):
        """окно с добавлением группы"""
        try:
            self.dialog = Dialog()
            self.dialog.setGeometry(800, 300, 400, 150)
            self.dialog.setWindowTitle('Добавление группы')

            self.nazvanie = QLabel(self.dialog)
            self.nazvanie.setText('Группа')
            self.nazvanie.move(5, 15)

            self.lineEdit = QLineEdit(self.dialog)
            self.lineEdit.resize(335, 20)
            self.lineEdit.move(55, 10)

            self.create_btn = QPushButton(self.dialog)
            self.create_btn.resize(80, 30)
            self.create_btn.setText('Сохранить')
            self.create_btn.move(290, 110)
            self.create_btn.clicked.connect(self.create_new_group)
            self.dialog.show()
            self.upd_res()
        except Exception as e:
            self.statusBar().showMessage('Ошибка')

    def upd_res2(self):
        """функия для обовления данных после добавления/удаления студентов"""
        self.z = "SELECT id, student_name, group_name, credits FROM 'students_info'"
        all_groups = self.cur.execute(self.z).fetchall()

        self.tableWidget_2.setRowCount(len(all_groups))
        for s, c in enumerate(all_groups):
            self.tableWidget_2.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_2.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_2.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_2.setItem(s, 3, QTableWidgetItem(str(c[3])))

    def create_new_student(self):
        """обработчик нажатия на кнопку сохранить в добавлении студента"""
        if self.lineEdit.text():
            NEW_NAME = self.lineEdit.text()
            maxid = self.cur.execute("SELECT id FROM 'students_info' ORDER BY id").fetchall()[
                -1]  # выбираем самый последний id
            group_name = self.lineEdit2.text()
            sql = "INSERT INTO students_info(id, student_name, group_name, credits) VALUES({}, '{}', '{}', {})".format(
                maxid[0] + 1, NEW_NAME, group_name, 0)
            self.cur.execute(sql).fetchall()
            self.con.commit()
            self.upd_res2()
            self.dialog.close()
        else:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, внимательно вводите данные",
                            QMessageBox.Ok)
            self.dialog.close()

    def adding_st(self):
        try:
            self.dialog = Dialog()
            self.dialog.setGeometry(800, 300, 400, 150)
            self.dialog.setWindowTitle('Добавление студента')

            self.nazvanie = QLabel(self.dialog)
            self.nazvanie.setText('Имя')
            self.nazvanie.move(5, 15)

            self.lineEdit = QLineEdit(self.dialog)
            self.lineEdit.resize(335, 20)
            self.lineEdit.move(55, 10)

            self.nazvaniegroup = QLabel(self.dialog)
            self.nazvaniegroup.setText('Группа')
            self.nazvaniegroup.move(5, 45)

            self.lineEdit2 = QLineEdit(self.dialog)
            self.lineEdit2.resize(335, 20)
            self.lineEdit2.move(55, 45)

            self.create_btn = QPushButton(self.dialog)
            self.create_btn.resize(80, 30)
            self.create_btn.setText('Сохранить')
            self.create_btn.move(290, 110)
            self.create_btn.clicked.connect(self.create_new_student)
            self.dialog.show()
            self.upd_res2()
        except Exception as e:
            self.statusBar().showMessage('Ошибка')

    def add_func2(self):
        self.adding_st()
        self.upd_res2()

    def delete_func2(self):
        """функция для удаления студента"""
        try:
            if self.tableWidget_2.item(self.row, self.col).text():
                # проходимся по таблице, чтобы понять какую группу кликнули
                rows = list(set([i.row() for i in self.tableWidget_2.selectedItems()]))
                names = [self.tableWidget_2.item(i, 1).text() for i in rows]
                # берем название группы, которую нужно удалить
                ids = [self.tableWidget_2.item(i, 0).text() for i in rows]
                valid = QMessageBox.question(
                    self, 'Подтверждение удаления',
                    f"Вы точно хотите удалить студента с именем {''.join(names)}?",
                    QMessageBox.Yes, QMessageBox.No)

                if valid == QMessageBox.Yes:  # если согласны, удаляем из базы данных
                    delete_sql = "DELETE FROM 'students_info' WHERE id = {}".format(''.join(ids))
                    self.cur.execute(delete_sql)
                    self.con.commit()
                    self.upd_res2()
                    self.upd_res2()
                self.upd_res2()  # после удаления обновляем таблицу, чтобы не отображались уже удаленные данные
            else:
                self.statusBar().showMessage('Ошибка')
        except Exception as e:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, выберите студента для удаления, кликнув на него",
                            QMessageBox.Ok)

    def upd_res3(self):
        """функия для обовления данных после добавления/удаления предметов"""
        self.z = "SELECT id, subject_name FROM 'subjects'"
        all_groups = self.cur.execute(self.z).fetchall()

        self.tableWidget_3.setRowCount(len(all_groups))
        for s, c in enumerate(all_groups):
            self.tableWidget_3.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_3.setItem(s, 1, QTableWidgetItem(str(c[1])))

    def create_new_sub(self):
        """обработки нажатия на кнопку сохранить в добалении предметов"""
        if self.lineEdit.text():
            NEW_NAME = self.lineEdit.text()
            maxid = self.cur.execute("SELECT id FROM 'subjects' ORDER BY id").fetchall()[
                -1]  # выбираем самый последний id
            sql = "INSERT INTO subjects(id, subject_name) VALUES({}, '{}')".format(maxid[0] + 1, NEW_NAME)
            self.cur.execute(sql).fetchall()
            self.con.commit()
            self.upd_res3()
            self.dialog.close()
        else:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, внимательно вводите данные",
                            QMessageBox.Ok)
            self.dialog.close()

    def adding_sub(self):
        """окно для добавления предмета"""
        try:
            self.dialog = Dialog()
            self.dialog.setGeometry(800, 300, 400, 150)
            self.dialog.setWindowTitle('Добавление предмета')

            self.nazvanie = QLabel(self.dialog)
            self.nazvanie.setText('Предмет')
            self.nazvanie.move(5, 15)

            self.lineEdit = QLineEdit(self.dialog)
            self.lineEdit.resize(335, 20)
            self.lineEdit.move(55, 10)

            self.create_btn = QPushButton(self.dialog)
            self.create_btn.resize(80, 30)
            self.create_btn.setText('Сохранить')
            self.create_btn.move(290, 110)
            self.create_btn.clicked.connect(self.create_new_sub)
            self.dialog.show()
            self.upd_res3()
        except Exception as e:
            self.statusBar().showMessage('Ошибка')

    def add_func3(self):
        self.adding_sub()
        self.upd_res3()

    def delete_func3(self):
        """функция для удаления предмета"""
        try:
            if self.tableWidget_3.item(self.row, self.col).text():
                # проходимся по таблице, чтобы понять какой предмет кликнули
                rows = list(set([i.row() for i in self.tableWidget_3.selectedItems()]))
                names = [self.tableWidget_3.item(i, 1).text() for i in rows]
                # берем название предмета, который нужно удалить
                ids = [self.tableWidget_3.item(i, 0).text() for i in rows]
                valid = QMessageBox.question(
                    self, 'Подтверждение удаления',
                    f"Вы точно хотите удалить предмет {''.join(names)}?",
                    QMessageBox.Yes, QMessageBox.No)

                if valid == QMessageBox.Yes:  # если согласны, удаляем из базы данных
                    delete_sql = "DELETE FROM 'subjects' WHERE id = {}".format(''.join(ids))
                    self.cur.execute(delete_sql)
                    self.con.commit()
                    self.upd_res3()
                    self.upd_res3()
                self.upd_res3()  # после удаления обновляем таблицу, чтобы не отображались уже удаленные данные
            else:
                self.statusBar().showMessage('Ошибка')
        except Exception as e:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, выберите предмет для удаления, кликнув на него",
                            QMessageBox.Ok)

    def upd_res4(self):
        self.con = sqlite3.connect('studentsinfo.sqlite')
        self.cur = self.con.cursor()
        self.sql = "SELECT id, student_name, subject_name, mark FROM 'passing'"

        self.table_passing = self.cur.execute(self.sql).fetchall()

        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(len(self.table_passing))
        self.tableWidget_4.setColumnWidth(0, 200)
        self.tableWidget_4.setColumnWidth(1, 200)
        self.tableWidget_4.setColumnWidth(2, 200)
        self.tableWidget_4.setColumnWidth(3, 150)
        self.tableWidget_4.setHorizontalHeaderLabels(["ID", "Студент", "Предмет", "Оценка"])

        for s, c in enumerate(self.table_passing):
            self.tableWidget_4.setItem(s, 0, QTableWidgetItem(str(c[0])))
            self.tableWidget_4.setItem(s, 1, QTableWidgetItem(str(c[1])))
            self.tableWidget_4.setItem(s, 2, QTableWidgetItem(str(c[2])))
            self.tableWidget_4.setItem(s, 3, QTableWidgetItem(str(c[3])))

    def create_new_pass(self):
        """обработки нажатия на кнопку сохранить в добалении предметов"""
        if self.lineEdit.text() and self.lineEdit2.text() and self.lineEdit3.text():
            NEW_NAME = self.lineEdit.text()
            NEW_SUB = self.lineEdit2.text()
            NEW_MARK = self.lineEdit3.text()
            maxid = self.cur.execute("SELECT id FROM 'passing' ORDER BY id").fetchall()[
                -1]  # выбираем самый последний id
            sql = "INSERT INTO passing(id, student_name, subject_name, mark) VALUES({}, '{}', '{}', {})".format(
                maxid[0] + 1, NEW_NAME, NEW_SUB, NEW_MARK)
            self.cur.execute(sql).fetchall()
            self.con.commit()
            self.upd_res4()
            self.dialog.close()
        else:
            dialog = QMessageBox(self)
            dialog.question(self, 'Внимание', "Пожалуйста, внимательно вводите данные",
                            QMessageBox.Ok)
            self.dialog.close()

    def add_func4(self):
        """добавление сдачи"""
        try:
            self.dialog = Dialog()
            self.dialog.setGeometry(800, 300, 400, 150)
            self.dialog.setWindowTitle('Добавление сдачи')

            self.nazvanie = QLabel(self.dialog)
            self.nazvanie.setText('Студент')
            self.nazvanie.move(5, 15)

            self.lineEdit = QLineEdit(self.dialog)
            self.lineEdit.resize(335, 20)
            self.lineEdit.move(55, 10)

            self.nazvanie2 = QLabel(self.dialog)
            self.nazvanie2.setText('Предмет')
            self.nazvanie2.move(5, 45)

            self.lineEdit2 = QLineEdit(self.dialog)
            self.lineEdit2.resize(335, 20)
            self.lineEdit2.move(55, 40)

            self.nazvanie3 = QLabel(self.dialog)
            self.nazvanie3.setText('Оценка')
            self.nazvanie3.move(5, 75)

            self.lineEdit3 = QLineEdit(self.dialog)
            self.lineEdit3.resize(335, 20)
            self.lineEdit3.move(55, 70)

            self.create_btn = QPushButton(self.dialog)
            self.create_btn.resize(80, 30)
            self.create_btn.setText('Сохранить')
            self.create_btn.move(290, 110)
            self.create_btn.clicked.connect(self.create_new_pass)
            self.dialog.show()
            self.upd_res4()
        except Exception as e:
            self.statusBar().showMessage('Ошибка')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
