# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/store/browse_games.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_browse_games(object):
    def setupUi(self, browse_games):
        browse_games.setObjectName("browse_games")
        browse_games.resize(706, 541)
        browse_games.setWindowTitle("Form")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(browse_games)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stack = QtWidgets.QStackedWidget(browse_games)
        self.stack.setObjectName("stack")
        self.games_page = QtWidgets.QWidget()
        self.games_page.setObjectName("games_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.games_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.games = QtWidgets.QScrollArea(self.games_page)
        self.games.setWidgetResizable(True)
        self.games.setObjectName("games")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 503))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.games.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.games)
        self.stack.addWidget(self.games_page)
        self.error = QtWidgets.QWidget()
        self.error.setObjectName("error")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.error)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.error_label = QtWidgets.QLabel(self.error)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_6.addWidget(self.error_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.stack.addWidget(self.error)
        self.horizontalLayout_2.addWidget(self.stack)
        self.filter_scroll = QtWidgets.QScrollArea(browse_games)
        self.filter_scroll.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filter_scroll.setWidgetResizable(True)
        self.filter_scroll.setObjectName("filter_scroll")
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setGeometry(QtCore.QRect(0, 0, 198, 521))
        self.scroll_widget.setObjectName("scroll_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.price_gb = QtWidgets.QGroupBox(self.scroll_widget)
        self.price_gb.setObjectName("price_gb")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.price_gb)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clear_price = QtWidgets.QRadioButton(self.price_gb)
        self.clear_price.setChecked(True)
        self.clear_price.setObjectName("clear_price")
        self.verticalLayout_2.addWidget(self.clear_price)
        self.free_button = QtWidgets.QRadioButton(self.price_gb)
        self.free_button.setObjectName("free_button")
        self.verticalLayout_2.addWidget(self.free_button)
        self.under10 = QtWidgets.QRadioButton(self.price_gb)
        self.under10.setObjectName("under10")
        self.verticalLayout_2.addWidget(self.under10)
        self.under20 = QtWidgets.QRadioButton(self.price_gb)
        self.under20.setObjectName("under20")
        self.verticalLayout_2.addWidget(self.under20)
        self.under30 = QtWidgets.QRadioButton(self.price_gb)
        self.under30.setObjectName("under30")
        self.verticalLayout_2.addWidget(self.under30)
        self.above = QtWidgets.QRadioButton(self.price_gb)
        self.above.setObjectName("above")
        self.verticalLayout_2.addWidget(self.above)
        self.on_discount = QtWidgets.QRadioButton(self.price_gb)
        self.on_discount.setObjectName("on_discount")
        self.verticalLayout_2.addWidget(self.on_discount)
        self.verticalLayout_3.addWidget(self.price_gb)
        self.genre_gb = QtWidgets.QGroupBox(self.scroll_widget)
        self.genre_gb.setObjectName("genre_gb")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.genre_gb)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addWidget(self.genre_gb)
        self.type_gb = QtWidgets.QGroupBox(self.scroll_widget)
        self.type_gb.setObjectName("type_gb")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.type_gb)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3.addWidget(self.type_gb)
        self.platform_gb = QtWidgets.QGroupBox(self.scroll_widget)
        self.platform_gb.setObjectName("platform_gb")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.platform_gb)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3.addWidget(self.platform_gb)
        self.others_gb = QtWidgets.QGroupBox(self.scroll_widget)
        self.others_gb.setObjectName("others_gb")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.others_gb)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.others_gb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.filter_scroll.setWidget(self.scroll_widget)
        self.horizontalLayout_2.addWidget(self.filter_scroll)

        self.retranslateUi(browse_games)
        self.stack.setCurrentIndex(0)

    def retranslateUi(self, browse_games):
        _translate = QtCore.QCoreApplication.translate
        self.error_label.setText(_translate("browse_games", "An error occured"))
        self.price_gb.setTitle(_translate("browse_games", "Price"))
        self.clear_price.setText(_translate("browse_games", "Clear price filter"))
        self.free_button.setText(_translate("browse_games", "Free"))
        self.under10.setText(_translate("browse_games", "Under 10"))
        self.under20.setText(_translate("browse_games", "Under 20"))
        self.under30.setText(_translate("browse_games", "Under 30"))
        self.above.setText(_translate("browse_games", "14.99 and above"))
        self.on_discount.setText(_translate("browse_games", "Discount"))
        self.genre_gb.setTitle(_translate("browse_games", "Genre"))
        self.type_gb.setTitle(_translate("browse_games", "Type"))
        self.platform_gb.setTitle(_translate("browse_games", "Platform"))
        self.others_gb.setTitle(_translate("browse_games", "Other Tags"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    browse_games = QtWidgets.QWidget()
    ui = Ui_browse_games()
    ui.setupUi(browse_games)
    browse_games.show()
    sys.exit(app.exec_())
