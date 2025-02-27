# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/games/game_info/game_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameInfo(object):
    def setupUi(self, GameInfo):
        GameInfo.setObjectName("GameInfo")
        GameInfo.resize(408, 340)
        self.main_layout = QtWidgets.QHBoxLayout(GameInfo)
        self.main_layout.setObjectName("main_layout")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.main_layout.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setObjectName("right_layout")
        self.info_layout = QtWidgets.QFormLayout()
        self.info_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_layout.setContentsMargins(6, 6, 6, 6)
        self.info_layout.setSpacing(12)
        self.info_layout.setObjectName("info_layout")
        self.lbl_dev = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dev.sizePolicy().hasHeightForWidth())
        self.lbl_dev.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dev.setFont(font)
        self.lbl_dev.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_dev.setObjectName("lbl_dev")
        self.info_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_dev)
        self.dev = QtWidgets.QLabel(GameInfo)
        self.dev.setText("error")
        self.dev.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dev.setObjectName("dev")
        self.info_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dev)
        self.lbl_app_name = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_app_name.sizePolicy().hasHeightForWidth())
        self.lbl_app_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_app_name.setFont(font)
        self.lbl_app_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_app_name.setObjectName("lbl_app_name")
        self.info_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_app_name)
        self.app_name = QtWidgets.QLabel(GameInfo)
        self.app_name.setText("error")
        self.app_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.app_name.setObjectName("app_name")
        self.info_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.app_name)
        self.lbl_version = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_version.sizePolicy().hasHeightForWidth())
        self.lbl_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_version.setFont(font)
        self.lbl_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.info_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_version)
        self.version = QtWidgets.QLabel(GameInfo)
        self.version.setText("error")
        self.version.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.version.setObjectName("version")
        self.info_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.version)
        self.lbl_grade = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_grade.sizePolicy().hasHeightForWidth())
        self.lbl_grade.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_grade.setFont(font)
        self.lbl_grade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_grade.setObjectName("lbl_grade")
        self.info_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_grade)
        self.grade = QtWidgets.QLabel(GameInfo)
        self.grade.setText("error")
        self.grade.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.grade.setObjectName("grade")
        self.info_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.grade)
        self.lbl_install_size = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_install_size.sizePolicy().hasHeightForWidth())
        self.lbl_install_size.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_install_size.setFont(font)
        self.lbl_install_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_install_size.setObjectName("lbl_install_size")
        self.info_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_install_size)
        self.install_size = QtWidgets.QLabel(GameInfo)
        self.install_size.setText("error")
        self.install_size.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.install_size.setObjectName("install_size")
        self.info_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.install_size)
        self.lbl_install_path = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_install_path.sizePolicy().hasHeightForWidth())
        self.lbl_install_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_install_path.setFont(font)
        self.lbl_install_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_install_path.setObjectName("lbl_install_path")
        self.info_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_install_path)
        self.install_path = QtWidgets.QLabel(GameInfo)
        self.install_path.setText("error")
        self.install_path.setWordWrap(True)
        self.install_path.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.install_path.setObjectName("install_path")
        self.info_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.install_path)
        self.lbl_platform = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_platform.sizePolicy().hasHeightForWidth())
        self.lbl_platform.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_platform.setFont(font)
        self.lbl_platform.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_platform.setObjectName("lbl_platform")
        self.info_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_platform)
        self.platform = QtWidgets.QLabel(GameInfo)
        self.platform.setText("error")
        self.platform.setObjectName("platform")
        self.info_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.platform)
        self.lbl_game_actions = QtWidgets.QLabel(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_game_actions.sizePolicy().hasHeightForWidth())
        self.lbl_game_actions.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_game_actions.setFont(font)
        self.lbl_game_actions.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_game_actions.setObjectName("lbl_game_actions")
        self.info_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_game_actions)
        self.game_actions_stack = QtWidgets.QStackedWidget(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_actions_stack.sizePolicy().hasHeightForWidth())
        self.game_actions_stack.setSizePolicy(sizePolicy)
        self.game_actions_stack.setMinimumSize(QtCore.QSize(250, 0))
        self.game_actions_stack.setMaximumSize(QtCore.QSize(250, 16777215))
        self.game_actions_stack.setObjectName("game_actions_stack")
        self.installed_page = QtWidgets.QWidget()
        self.installed_page.setObjectName("installed_page")
        self.installed_layout = QtWidgets.QVBoxLayout(self.installed_page)
        self.installed_layout.setContentsMargins(0, 0, 0, 0)
        self.installed_layout.setObjectName("installed_layout")
        self.verify_stack = QtWidgets.QStackedWidget(self.installed_page)
        self.verify_stack.setObjectName("verify_stack")
        self.verify_button_page = QtWidgets.QWidget()
        self.verify_button_page.setObjectName("verify_button_page")
        self.verify_page_layout = QtWidgets.QHBoxLayout(self.verify_button_page)
        self.verify_page_layout.setContentsMargins(0, 0, 0, 0)
        self.verify_page_layout.setSpacing(0)
        self.verify_page_layout.setObjectName("verify_page_layout")
        self.verify_button = QtWidgets.QPushButton(self.verify_button_page)
        self.verify_button.setObjectName("verify_button")
        self.verify_page_layout.addWidget(self.verify_button)
        self.verify_stack.addWidget(self.verify_button_page)
        self.verify_progress_page = QtWidgets.QWidget()
        self.verify_progress_page.setObjectName("verify_progress_page")
        self.verify_progress_layout = QtWidgets.QHBoxLayout(self.verify_progress_page)
        self.verify_progress_layout.setContentsMargins(0, 0, 0, 0)
        self.verify_progress_layout.setSpacing(0)
        self.verify_progress_layout.setObjectName("verify_progress_layout")
        self.verify_progress = QtWidgets.QProgressBar(self.verify_progress_page)
        self.verify_progress.setProperty("value", 24)
        self.verify_progress.setObjectName("verify_progress")
        self.verify_progress_layout.addWidget(self.verify_progress)
        self.verify_stack.addWidget(self.verify_progress_page)
        self.installed_layout.addWidget(self.verify_stack)
        self.repair_button = QtWidgets.QPushButton(self.installed_page)
        self.repair_button.setObjectName("repair_button")
        self.installed_layout.addWidget(self.repair_button)
        self.move_stack = QtWidgets.QStackedWidget(self.installed_page)
        self.move_stack.setObjectName("move_stack")
        self.move_button_page = QtWidgets.QWidget()
        self.move_button_page.setObjectName("move_button_page")
        self.move_button_layout = QtWidgets.QHBoxLayout(self.move_button_page)
        self.move_button_layout.setContentsMargins(0, 0, 0, 0)
        self.move_button_layout.setSpacing(0)
        self.move_button_layout.setObjectName("move_button_layout")
        self.move_button = QtWidgets.QToolButton(self.move_button_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_button.sizePolicy().hasHeightForWidth())
        self.move_button.setSizePolicy(sizePolicy)
        self.move_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.move_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.move_button.setArrowType(QtCore.Qt.DownArrow)
        self.move_button.setObjectName("move_button")
        self.move_button_layout.addWidget(self.move_button)
        self.move_stack.addWidget(self.move_button_page)
        self.move_progress_page = QtWidgets.QWidget()
        self.move_progress_page.setObjectName("move_progress_page")
        self.move_progress_layout = QtWidgets.QHBoxLayout(self.move_progress_page)
        self.move_progress_layout.setContentsMargins(0, 0, 0, 0)
        self.move_progress_layout.setSpacing(0)
        self.move_progress_layout.setObjectName("move_progress_layout")
        self.move_progress = QtWidgets.QProgressBar(self.move_progress_page)
        self.move_progress.setProperty("value", 24)
        self.move_progress.setObjectName("move_progress")
        self.move_progress_layout.addWidget(self.move_progress)
        self.move_stack.addWidget(self.move_progress_page)
        self.installed_layout.addWidget(self.move_stack)
        self.uninstall_button = QtWidgets.QPushButton(self.installed_page)
        self.uninstall_button.setObjectName("uninstall_button")
        self.installed_layout.addWidget(self.uninstall_button)
        self.game_actions_stack.addWidget(self.installed_page)
        self.uninstalled_page = QtWidgets.QWidget()
        self.uninstalled_page.setObjectName("uninstalled_page")
        self.uninstalled_layout = QtWidgets.QVBoxLayout(self.uninstalled_page)
        self.uninstalled_layout.setContentsMargins(0, 0, 0, 0)
        self.uninstalled_layout.setObjectName("uninstalled_layout")
        self.install_button = QtWidgets.QPushButton(self.uninstalled_page)
        self.install_button.setObjectName("install_button")
        self.uninstalled_layout.addWidget(self.install_button)
        self.import_button = QtWidgets.QPushButton(self.uninstalled_page)
        self.import_button.setObjectName("import_button")
        self.uninstalled_layout.addWidget(self.import_button)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.uninstalled_layout.addItem(spacerItem)
        self.game_actions_stack.addWidget(self.uninstalled_page)
        self.info_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.game_actions_stack)
        self.right_layout.addLayout(self.info_layout)
        self.requirements_group = QtWidgets.QFrame(GameInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requirements_group.sizePolicy().hasHeightForWidth())
        self.requirements_group.setSizePolicy(sizePolicy)
        self.requirements_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.requirements_group.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.requirements_group.setObjectName("requirements_group")
        self.requirements_layout = QtWidgets.QHBoxLayout(self.requirements_group)
        self.requirements_layout.setContentsMargins(0, 0, 0, 0)
        self.requirements_layout.setObjectName("requirements_layout")
        self.right_layout.addWidget(self.requirements_group)
        self.main_layout.addLayout(self.right_layout)
        self.main_layout.setStretch(1, 1)

        self.retranslateUi(GameInfo)
        self.game_actions_stack.setCurrentIndex(1)
        self.verify_stack.setCurrentIndex(0)
        self.move_stack.setCurrentIndex(0)

    def retranslateUi(self, GameInfo):
        _translate = QtCore.QCoreApplication.translate
        GameInfo.setWindowTitle(_translate("GameInfo", "Game Info"))
        self.lbl_dev.setText(_translate("GameInfo", "Developer"))
        self.lbl_app_name.setText(_translate("GameInfo", "Application Name"))
        self.lbl_version.setText(_translate("GameInfo", "Version"))
        self.lbl_grade.setText(_translate("GameInfo", "ProtonDB Grade"))
        self.lbl_install_size.setText(_translate("GameInfo", "Installation Size"))
        self.lbl_install_path.setText(_translate("GameInfo", "Installation Path"))
        self.lbl_platform.setText(_translate("GameInfo", "Platform"))
        self.lbl_game_actions.setText(_translate("GameInfo", "Actions"))
        self.verify_button.setText(_translate("GameInfo", "Verify Installation"))
        self.repair_button.setText(_translate("GameInfo", "Repair Installation"))
        self.move_button.setText(_translate("GameInfo", "Move Installation"))
        self.uninstall_button.setText(_translate("GameInfo", "Uninstall Game"))
        self.install_button.setText(_translate("GameInfo", "Install Game"))
        self.import_button.setText(_translate("GameInfo", "Import Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameInfo = QtWidgets.QWidget()
    ui = Ui_GameInfo()
    ui.setupUi(GameInfo)
    GameInfo.show()
    sys.exit(app.exec_())
