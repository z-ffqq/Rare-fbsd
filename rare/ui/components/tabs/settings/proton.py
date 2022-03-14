# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/settings/proton.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProtonSettings(object):
    def setupUi(self, ProtonSettings):
        ProtonSettings.setObjectName("ProtonSettings")
        ProtonSettings.resize(400, 300)
        ProtonSettings.setWindowTitle("GroupBox")
        self.formLayout = QtWidgets.QFormLayout(ProtonSettings)
        self.formLayout.setObjectName("formLayout")
        self.proton_wrapper_label = QtWidgets.QLabel(ProtonSettings)
        self.proton_wrapper_label.setObjectName("proton_wrapper_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.proton_wrapper_label)
        self.proton_combo = QtWidgets.QComboBox(ProtonSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proton_combo.sizePolicy().hasHeightForWidth())
        self.proton_combo.setSizePolicy(sizePolicy)
        self.proton_combo.setObjectName("proton_combo")
        self.proton_combo.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.proton_combo)
        self.proton_prefix_label = QtWidgets.QLabel(ProtonSettings)
        self.proton_prefix_label.setObjectName("proton_prefix_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.proton_prefix_label)
        self.placeholder_prefix_edit = QtWidgets.QLineEdit(ProtonSettings)
        self.placeholder_prefix_edit.setObjectName("placeholder_prefix_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.placeholder_prefix_edit)

        self.retranslateUi(ProtonSettings)
        QtCore.QMetaObject.connectSlotsByName(ProtonSettings)

    def retranslateUi(self, ProtonSettings):
        _translate = QtCore.QCoreApplication.translate
        ProtonSettings.setTitle(_translate("ProtonSettings", "Proton Settings"))
        self.proton_wrapper_label.setText(_translate("ProtonSettings", "Proton"))
        self.proton_combo.setItemText(0, _translate("ProtonSettings", "Don\'t use Proton"))
        self.proton_prefix_label.setText(_translate("ProtonSettings", "Prefix"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProtonSettings = QtWidgets.QGroupBox()
    ui = Ui_ProtonSettings()
    ui.setupUi(ProtonSettings)
    ProtonSettings.show()
    sys.exit(app.exec_())
