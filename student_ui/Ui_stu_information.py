# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\coding_programs\PythonPrograms\student_status_information\student_ui\stu_information.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1122, 849)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\coding_programs\\PythonPrograms\\student_status_information\\student_ui\\login_ui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        self.name_label = QtWidgets.QLabel(login)
        self.name_label.setGeometry(QtCore.QRect(370, 210, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_lineEdit = QtWidgets.QLineEdit(login)
        self.name_lineEdit.setGeometry(QtCore.QRect(490, 220, 211, 51))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.sno_label = QtWidgets.QLabel(login)
        self.sno_label.setGeometry(QtCore.QRect(370, 120, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.sno_label.setFont(font)
        self.sno_label.setObjectName("sno_label")
        self.sno_lineEdit = QtWidgets.QLineEdit(login)
        self.sno_lineEdit.setGeometry(QtCore.QRect(490, 140, 211, 51))
        self.sno_lineEdit.setObjectName("sno_lineEdit")
        self.sex_label = QtWidgets.QLabel(login)
        self.sex_label.setGeometry(QtCore.QRect(370, 290, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.sex_lineEdit = QtWidgets.QLineEdit(login)
        self.sex_lineEdit.setGeometry(QtCore.QRect(490, 300, 211, 51))
        self.sex_lineEdit.setObjectName("sex_lineEdit")
        self.start_year_label = QtWidgets.QLabel(login)
        self.start_year_label.setGeometry(QtCore.QRect(310, 360, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_year_label.setFont(font)
        self.start_year_label.setObjectName("start_year_label")
        self.start_year_lineEdit = QtWidgets.QLineEdit(login)
        self.start_year_lineEdit.setGeometry(QtCore.QRect(490, 370, 211, 51))
        self.start_year_lineEdit.setObjectName("start_year_lineEdit")
        self.class_label = QtWidgets.QLabel(login)
        self.class_label.setGeometry(QtCore.QRect(370, 430, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.class_label.setFont(font)
        self.class_label.setObjectName("class_label")
        self.class_lineEdit = QtWidgets.QLineEdit(login)
        self.class_lineEdit.setGeometry(QtCore.QRect(490, 440, 211, 51))
        self.class_lineEdit.setObjectName("class_lineEdit")
        self.profession_label = QtWidgets.QLabel(login)
        self.profession_label.setGeometry(QtCore.QRect(370, 500, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.profession_label.setFont(font)
        self.profession_label.setObjectName("profession_label")
        self.profession_lineEdit = QtWidgets.QLineEdit(login)
        self.profession_lineEdit.setGeometry(QtCore.QRect(490, 510, 211, 51))
        self.profession_lineEdit.setText("")
        self.profession_lineEdit.setObjectName("profession_lineEdit")
        self.dept_label = QtWidgets.QLabel(login)
        self.dept_label.setGeometry(QtCore.QRect(370, 570, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.dept_lineEdit = QtWidgets.QLineEdit(login)
        self.dept_lineEdit.setGeometry(QtCore.QRect(490, 580, 211, 51))
        self.dept_lineEdit.setText("")
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(470, 680, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.self_info_show)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "学生个人学籍信息查看"))
        self.name_label.setText(_translate("login", "姓名："))
        self.sno_label.setText(_translate("login", "学号："))
        self.sex_label.setText(_translate("login", "性别："))
        self.start_year_label.setText(_translate("login", "入学年份："))
        self.class_label.setText(_translate("login", "班级："))
        self.profession_label.setText(_translate("login", "专业："))
        self.dept_label.setText(_translate("login", "学院："))
        self.pushButton.setText(_translate("login", "信息显示"))

    def self_info_show(self):
        stu_id=self.sno_lineEdit.text()
        try:
            db_stu_self_info=pymysql.connect(host="127.0.0.1",user="student",password="123456",database="student_status_information")
            cursor=db_stu_self_info.cursor()
            cursor.execute("select stu_id,stu_name,stu_sex,stu_year,stu_class,stu_master,stu_dept from stu_info where stu_id=%s",stu_id)
            result=cursor.fetchone()
            print(result)
            if result is not None:
                self.name_lineEdit.setText(result[1])
                self.sex_lineEdit.setText(result[2])
                self.start_year_lineEdit.setText(str(result[3]))
                self.class_lineEdit.setText(str(result[4]))
                self.profession_lineEdit.setText(result[5])
                self.dept_lineEdit.setText(result[6])
                self.sno_lineEdit.setEnabled(False)
                self.name_lineEdit.setEnabled(False)
                self.sex_lineEdit.setEnabled(False)
                self.start_year_lineEdit.setEnabled(False)
                self.class_lineEdit.setEnabled(False)
                self.profession_lineEdit.setEnabled(False)
                self.dept_lineEdit.setEnabled(False)
                db_stu_self_info.close()

            else:
                Error_msg_stu_info=QtWidgets.QMessageBox()
                Error_msg_stu_info.setText("获取个人信息异常")
                Error_msg_stu_info.show()
        except:
            Error_msg=QtWidgets.QMessageBox()
            Error_msg.setText("MYSQL服务未连接")
            Error_msg.show()