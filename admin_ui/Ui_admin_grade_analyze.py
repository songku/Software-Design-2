# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\coding_programs\PythonPrograms\student_status_information\admin_ui\admin_grade_analyze.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1122, 849)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\coding_programs\\PythonPrograms\\student_status_information\\admin_ui\\login_ui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.name_label = QtWidgets.QLabel(login)
        self.name_label.setGeometry(QtCore.QRect(70, 180, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_lineEdit = QtWidgets.QLineEdit(login)
        self.name_lineEdit.setGeometry(QtCore.QRect(190, 190, 211, 51))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.select_all_Button = QtWidgets.QPushButton(login)
        self.select_all_Button.setGeometry(QtCore.QRect(710, 660, 191, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.select_all_Button.setFont(font)
        self.select_all_Button.setObjectName("select_all_Button")
        self.select_Button = QtWidgets.QPushButton(login)
        self.select_Button.setGeometry(QtCore.QRect(240, 660, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.select_Button.setFont(font)
        self.select_Button.setObjectName("select_Button")
        self.sno_label = QtWidgets.QLabel(login)
        self.sno_label.setGeometry(QtCore.QRect(70, 90, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.sno_label.setFont(font)
        self.sno_label.setObjectName("sno_label")
        self.sno_lineEdit = QtWidgets.QLineEdit(login)
        self.sno_lineEdit.setGeometry(QtCore.QRect(190, 110, 211, 51))
        self.sno_lineEdit.setObjectName("sno_lineEdit")
        self.class_label = QtWidgets.QLabel(login)
        self.class_label.setGeometry(QtCore.QRect(70, 260, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.class_label.setFont(font)
        self.class_label.setObjectName("class_label")
        self.class_lineEdit = QtWidgets.QLineEdit(login)
        self.class_lineEdit.setGeometry(QtCore.QRect(190, 270, 211, 51))
        self.class_lineEdit.setObjectName("class_lineEdit")
        self.profession_label = QtWidgets.QLabel(login)
        self.profession_label.setGeometry(QtCore.QRect(70, 330, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.profession_label.setFont(font)
        self.profession_label.setObjectName("profession_label")
        self.profession_lineEdit = QtWidgets.QLineEdit(login)
        self.profession_lineEdit.setGeometry(QtCore.QRect(190, 340, 211, 51))
        self.profession_lineEdit.setText("")
        self.profession_lineEdit.setObjectName("profession_lineEdit")
        self.dept_label = QtWidgets.QLabel(login)
        self.dept_label.setGeometry(QtCore.QRect(70, 400, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.dept_lineEdit = QtWidgets.QLineEdit(login)
        self.dept_lineEdit.setGeometry(QtCore.QRect(190, 410, 211, 51))
        self.dept_lineEdit.setText("")
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.stu_status_tableWidget = QtWidgets.QTableWidget(login)
        self.stu_status_tableWidget.setGeometry(QtCore.QRect(480, 110, 601, 501))
        self.stu_status_tableWidget.setObjectName("stu_status_tableWidget")
        self.stu_status_tableWidget.setColumnCount(0)
        self.stu_status_tableWidget.setRowCount(0)
        self.compre_grade_label = QtWidgets.QLabel(login)
        self.compre_grade_label.setGeometry(QtCore.QRect(10, 480, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.compre_grade_label.setFont(font)
        self.compre_grade_label.setObjectName("compre_grade_label")
        self.compre_grade_lineEdit = QtWidgets.QLineEdit(login)
        self.compre_grade_lineEdit.setGeometry(QtCore.QRect(190, 490, 211, 51))
        self.compre_grade_lineEdit.setObjectName("compre_grade_lineEdit")
        self.stu_status_lineEdit = QtWidgets.QLineEdit(login)
        self.stu_status_lineEdit.setGeometry(QtCore.QRect(190, 560, 211, 51))
        self.stu_status_lineEdit.setText("")
        self.stu_status_lineEdit.setObjectName("stu_status_lineEdit")
        self.stu_status_label = QtWidgets.QLabel(login)
        self.stu_status_label.setGeometry(QtCore.QRect(10, 550, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stu_status_label.setFont(font)
        self.stu_status_label.setObjectName("stu_status_label")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "??????????????????"))
        self.name_label.setText(_translate("login", "?????????"))
        self.select_all_Button.setText(_translate("login", "??????"))
        self.select_Button.setText(_translate("login", "??????"))
        self.sno_label.setText(_translate("login", "?????????"))
        self.class_label.setText(_translate("login", "?????????"))
        self.profession_label.setText(_translate("login", "?????????"))
        self.dept_label.setText(_translate("login", "?????????"))
        self.compre_grade_label.setText(_translate("login", "???????????????"))
        self.stu_status_label.setText(_translate("login", "???????????????"))
