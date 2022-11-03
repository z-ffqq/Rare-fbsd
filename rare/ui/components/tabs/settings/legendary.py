# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/settings/legendary.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LegendarySettings(object):
    def setupUi(self, LegendarySettings):
        LegendarySettings.setObjectName("LegendarySettings")
        LegendarySettings.resize(595, 334)
        LegendarySettings.setWindowTitle("LegendarySettings")
        self.legendary_layout = QtWidgets.QHBoxLayout(LegendarySettings)
        self.legendary_layout.setObjectName("legendary_layout")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.install_dir_group = QtWidgets.QGroupBox(LegendarySettings)
        self.install_dir_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.install_dir_group.setObjectName("install_dir_group")
        self.install_dir_layout = QtWidgets.QVBoxLayout(self.install_dir_group)
        self.install_dir_layout.setObjectName("install_dir_layout")
        self.left_layout.addWidget(self.install_dir_group, 0, QtCore.Qt.AlignTop)
        self.download_group = QtWidgets.QGroupBox(LegendarySettings)
        self.download_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.download_group.setObjectName("download_group")
        self.download_layout = QtWidgets.QFormLayout(self.download_group)
        self.download_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.download_layout.setObjectName("download_layout")
        self.max_workers_label = QtWidgets.QLabel(self.download_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_workers_label.sizePolicy().hasHeightForWidth())
        self.max_workers_label.setSizePolicy(sizePolicy)
        self.max_workers_label.setObjectName("max_workers_label")
        self.download_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.max_workers_label)
        self.max_workers_layout = QtWidgets.QHBoxLayout()
        self.max_workers_layout.setObjectName("max_workers_layout")
        self.max_worker_spin = QtWidgets.QSpinBox(self.download_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_worker_spin.sizePolicy().hasHeightForWidth())
        self.max_worker_spin.setSizePolicy(sizePolicy)
        self.max_worker_spin.setMinimum(0)
        self.max_worker_spin.setMaximum(16)
        self.max_worker_spin.setProperty("value", 0)
        self.max_worker_spin.setObjectName("max_worker_spin")
        self.max_workers_layout.addWidget(self.max_worker_spin)
        self.max_workers_info_label = QtWidgets.QLabel(self.download_group)
        font = QtGui.QFont()
        font.setItalic(True)
        self.max_workers_info_label.setFont(font)
        self.max_workers_info_label.setObjectName("max_workers_info_label")
        self.max_workers_layout.addWidget(self.max_workers_info_label)
        self.download_layout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.max_workers_layout)
        self.max_memory_label = QtWidgets.QLabel(self.download_group)
        self.max_memory_label.setObjectName("max_memory_label")
        self.download_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.max_memory_label)
        self.max_memory_layout = QtWidgets.QHBoxLayout()
        self.max_memory_layout.setObjectName("max_memory_layout")
        self.max_memory_spin = QtWidgets.QSpinBox(self.download_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_memory_spin.sizePolicy().hasHeightForWidth())
        self.max_memory_spin.setSizePolicy(sizePolicy)
        self.max_memory_spin.setMinimum(0)
        self.max_memory_spin.setMaximum(10240)
        self.max_memory_spin.setSingleStep(128)
        self.max_memory_spin.setProperty("value", 1024)
        self.max_memory_spin.setObjectName("max_memory_spin")
        self.max_memory_layout.addWidget(self.max_memory_spin)
        self.max_memory_info_label = QtWidgets.QLabel(self.download_group)
        font = QtGui.QFont()
        font.setItalic(True)
        self.max_memory_info_label.setFont(font)
        self.max_memory_info_label.setObjectName("max_memory_info_label")
        self.max_memory_layout.addWidget(self.max_memory_info_label)
        self.download_layout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.max_memory_layout)
        self.preferred_cdn_label = QtWidgets.QLabel(self.download_group)
        self.preferred_cdn_label.setObjectName("preferred_cdn_label")
        self.download_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.preferred_cdn_label)
        self.preferred_cdn_line = QtWidgets.QLineEdit(self.download_group)
        self.preferred_cdn_line.setObjectName("preferred_cdn_line")
        self.download_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.preferred_cdn_line)
        self.disable_https_label = QtWidgets.QLabel(self.download_group)
        self.disable_https_label.setObjectName("disable_https_label")
        self.download_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.disable_https_label)
        self.disable_https_check = QtWidgets.QCheckBox(self.download_group)
        self.disable_https_check.setText("")
        self.disable_https_check.setObjectName("disable_https_check")
        self.download_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.disable_https_check)
        self.left_layout.addWidget(self.download_group, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(spacerItem)
        self.legendary_layout.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setObjectName("right_layout")
        self.locale_group = QtWidgets.QGroupBox(LegendarySettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locale_group.sizePolicy().hasHeightForWidth())
        self.locale_group.setSizePolicy(sizePolicy)
        self.locale_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.locale_group.setObjectName("locale_group")
        self.locale_layout = QtWidgets.QVBoxLayout(self.locale_group)
        self.locale_layout.setObjectName("locale_layout")
        self.right_layout.addWidget(self.locale_group, 0, QtCore.Qt.AlignTop)
        self.cleanup_group = QtWidgets.QGroupBox(LegendarySettings)
        self.cleanup_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cleanup_group.setObjectName("cleanup_group")
        self.cleanup_layout = QtWidgets.QVBoxLayout(self.cleanup_group)
        self.cleanup_layout.setObjectName("cleanup_layout")
        self.clean_keep_manifests_button = QtWidgets.QPushButton(self.cleanup_group)
        self.clean_keep_manifests_button.setObjectName("clean_keep_manifests_button")
        self.cleanup_layout.addWidget(self.clean_keep_manifests_button)
        self.clean_button = QtWidgets.QPushButton(self.cleanup_group)
        self.clean_button.setObjectName("clean_button")
        self.cleanup_layout.addWidget(self.clean_button)
        self.right_layout.addWidget(self.cleanup_group, 0, QtCore.Qt.AlignTop)
        self.meta_group = QtWidgets.QGroupBox(LegendarySettings)
        self.meta_group.setObjectName("meta_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.meta_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.win32_cb = QtWidgets.QCheckBox(self.meta_group)
        self.win32_cb.setObjectName("win32_cb")
        self.verticalLayout_2.addWidget(self.win32_cb)
        self.mac_cb = QtWidgets.QCheckBox(self.meta_group)
        self.mac_cb.setObjectName("mac_cb")
        self.verticalLayout_2.addWidget(self.mac_cb)
        self.refresh_game_meta_btn = QtWidgets.QPushButton(self.meta_group)
        self.refresh_game_meta_btn.setObjectName("refresh_game_meta_btn")
        self.verticalLayout_2.addWidget(self.refresh_game_meta_btn)
        self.right_layout.addWidget(self.meta_group)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.right_layout.addItem(spacerItem1)
        self.legendary_layout.addLayout(self.right_layout)

        self.retranslateUi(LegendarySettings)
        QtCore.QMetaObject.connectSlotsByName(LegendarySettings)

    def retranslateUi(self, LegendarySettings):
        _translate = QtCore.QCoreApplication.translate
        self.install_dir_group.setTitle(_translate("LegendarySettings", "Default Installation Directory"))
        self.download_group.setTitle(_translate("LegendarySettings", "Download Settings"))
        self.max_workers_label.setText(_translate("LegendarySettings", "Max Workers"))
        self.max_workers_info_label.setText(_translate("LegendarySettings", "Less is slower (0: Default)"))
        self.max_memory_label.setText(_translate("LegendarySettings", "Max Shared Memory"))
        self.max_memory_spin.setSuffix(_translate("LegendarySettings", "MiB"))
        self.max_memory_info_label.setText(_translate("LegendarySettings", "Less is slower (0: Default)"))
        self.preferred_cdn_label.setText(_translate("LegendarySettings", "Preferred CDN"))
        self.preferred_cdn_line.setPlaceholderText(_translate("LegendarySettings", "Default"))
        self.disable_https_label.setText(_translate("LegendarySettings", "Disable HTTPS"))
        self.locale_group.setTitle(_translate("LegendarySettings", "Locale"))
        self.cleanup_group.setTitle(_translate("LegendarySettings", "Cleanup"))
        self.clean_keep_manifests_button.setText(_translate("LegendarySettings", "Clean, but keep manifests"))
        self.clean_button.setText(_translate("LegendarySettings", "Remove everything"))
        self.meta_group.setTitle(_translate("LegendarySettings", "Game metadata"))
        self.win32_cb.setText(_translate("LegendarySettings", "Load 32bit data"))
        self.mac_cb.setText(_translate("LegendarySettings", "Load MacOS data"))
        self.refresh_game_meta_btn.setText(_translate("LegendarySettings", "Refresh game meta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LegendarySettings = QtWidgets.QWidget()
    ui = Ui_LegendarySettings()
    ui.setupUi(LegendarySettings)
    LegendarySettings.show()
    sys.exit(app.exec_())
