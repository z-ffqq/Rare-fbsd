import re
from logging import getLogger
from typing import Dict

from PyQt5.QtCore import pyqtSignal, QSettings
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QPushButton, QInputDialog, QFrame, QMessageBox, QSizePolicy

from rare import shared
from rare.ui.components.tabs.settings.wrapper import Ui_WrapperSettings
from rare.utils import config_helper
from rare.utils.extra_widgets import FlowLayout
from rare.utils.utils import icon

logger = getLogger("Wrapper Settings")

extra_wrapper_regex = {
    "proton": "\".*proton\" run",  # proton
    "mangohud": "mangohud"  # mangohud
}


class WrapperWidget(QFrame):
    delete_wrapper = pyqtSignal(str)

    def __init__(self, text: str):
        super(WrapperWidget, self).__init__()
        self.setLayout(QHBoxLayout())
        self.text = text
        self.layout().addWidget(QLabel(text))
        self.setProperty("frameShape", 6)

        self.delete_button = QPushButton(icon("ei.remove"), "")
        self.layout().addWidget(self.delete_button)
        self.delete_button.clicked.connect(self.delete)

    def delete(self):
        self.delete_wrapper.emit(self.text)


class WrapperSettings(QGroupBox, Ui_WrapperSettings):
    wrappers: Dict[str, WrapperWidget] = dict()
    extra_wrappers: Dict[str, str] = dict()
    app_name: str

    def __init__(self):
        super(WrapperSettings, self).__init__("Wrapper")
        self.setupUi(self)
        self.widgets.setLayout(FlowLayout())
        self.core = shared.LegendaryCoreSingleton()

        self.add_button.clicked.connect(self.add_button_pressed)
        self.settings = QSettings()

    def get_wrapper_string(self):
        return " ".join(self.get_wrapper_list())

    def get_wrapper_list(self):
        return list(self.extra_wrappers.values()) + list(self.wrappers.keys())

    def add_button_pressed(self):
        wrapper, done = QInputDialog.getText(self, "Input Dialog", self.tr("Insert name of wrapper"))
        if not done:
            return
        self.add_wrapper(wrapper)

    def add_wrapper(self, text: str):
        for key, extra_wrapper in extra_wrapper_regex.items():
            if re.match(extra_wrapper, text):
                self.extra_wrappers[key] = text
                self.save()
                return
        if self.wrappers.get(text):
            QMessageBox.warning(self, "Warning", self.tr("Wrapper is already in the list"))
            return

        self.widget_stack.setCurrentIndex(0)

        widget = WrapperWidget(text)
        self.widgets.layout().addWidget(widget)
        widget.delete_wrapper.connect(self.delete_wrapper)
        self.widgets.layout().addWidget(widget)
        self.wrappers[text] = widget

        # flow layout bug: Workaround
        lbl = QLabel("")
        self.widgets.layout().addWidget(lbl)
        lbl.deleteLater()

        self.save()

    def delete_wrapper(self, text: str):
        widget = self.wrappers.get(text, None)
        if not widget and self.extra_wrappers.get(text, None):
            self.extra_wrappers.pop(text)
        elif widget:
            widget.deleteLater()
            self.wrappers.pop(text)

        if not self.wrappers:
            self.widget_stack.setCurrentIndex(1)

        self.save()

    def save(self):
        # save wrappers twice, to support wrappers with spaces
        if len(self.wrappers) == 0 and len(self.extra_wrappers) == 0:
            config_helper.remove_option(self.app_name, "wrapper")
            self.settings.remove(f"{self.app_name}/wrapper")
        else:
            config_helper.add_option(self.app_name, "wrapper", self.get_wrapper_string())
            self.settings.setValue(f"{self.app_name}/wrapper", self.get_wrapper_list())

    def load_settings(self, app_name: str):
        self.app_name = app_name
        for i in self.wrappers.values():
            i.deleteLater()
        self.wrappers.clear()
        self.extra_wrappers.clear()

        wrappers = self.settings.value(f"{self.app_name}/wrapper", [], str)

        if not wrappers and (cfg := self.core.lgd.config.get(self.app_name, "wrapper", fallback="")):
            logger.info("Loading wrappers from legendary config")
            # no qt wrapper, but legendary wrapper, to have backward compatibility
            pattern = re.compile(r'''((?:[^ "']|"[^"]*"|'[^']*')+)''')
            wrappers = pattern.split(cfg)[1::2]

        for wrapper in wrappers:
            self.add_wrapper(wrapper)

        if not self.wrappers:
            self.widget_stack.setCurrentIndex(1)
            return
        else:
            self.widget_stack.setCurrentIndex(0)
