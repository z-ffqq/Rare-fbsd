# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/dialogs/login/login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(324, 132)
        self.login_layout = QtWidgets.QVBoxLayout(LoginDialog)
        self.login_layout.setObjectName("login_layout")
        spacerItem = QtWidgets.QSpacerItem(0, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.login_layout.addItem(spacerItem)
        self.welcome_label = QtWidgets.QLabel(LoginDialog)
        self.welcome_label.setObjectName("welcome_label")
        self.login_layout.addWidget(self.welcome_label)
        spacerItem1 = QtWidgets.QSpacerItem(0, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.login_layout.addItem(spacerItem1)
        self.login_stack_layout = QtWidgets.QVBoxLayout()
        self.login_stack_layout.setObjectName("login_stack_layout")
        self.login_layout.addLayout(self.login_stack_layout)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem2)
        self.exit_button = QtWidgets.QPushButton(LoginDialog)
        self.exit_button.setObjectName("exit_button")
        self.button_layout.addWidget(self.exit_button)
        self.back_button = QtWidgets.QPushButton(LoginDialog)
        self.back_button.setObjectName("back_button")
        self.button_layout.addWidget(self.back_button)
        self.next_button = QtWidgets.QPushButton(LoginDialog)
        self.next_button.setObjectName("next_button")
        self.button_layout.addWidget(self.next_button)
        self.login_layout.addLayout(self.button_layout)

        self.retranslateUi(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Rare Login"))
        self.welcome_label.setText(_translate("LoginDialog", "<h1>Welcome to Rare</h1>"))
        self.exit_button.setText(_translate("LoginDialog", "Exit"))
        self.back_button.setText(_translate("LoginDialog", "Back"))
        self.next_button.setText(_translate("LoginDialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
