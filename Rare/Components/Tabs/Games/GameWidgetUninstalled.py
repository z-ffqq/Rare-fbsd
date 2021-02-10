import os
from logging import getLogger

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QInputDialog
from legendary.core import LegendaryCore
from legendary.models.game import Game

from Rare.utils.Dialogs.InstallDialog import InstallDialog
from Rare.utils.QtExtensions import ClickableLabel
from Rare.utils.RareConfig import IMAGE_DIR

logger = getLogger("Uninstalled")


class GameWidgetUninstalled(QWidget):
    def __init__(self, core: LegendaryCore, game: Game):
        super(GameWidgetUninstalled, self).__init__()
        self.layout = QVBoxLayout()
        self.core = core
        self.game = game

        if os.path.exists(f"{IMAGE_DIR}/{game.app_name}/UninstalledArt.png"):
            pixmap = QPixmap(f"{IMAGE_DIR}/{game.app_name}/UninstalledArt.png")
        else:
            logger.warning(f"No Image found: {self.game.app_title}")
            pixmap = None
        if pixmap:
            w = 200
            pixmap = pixmap.scaled(w, int(w * 4 / 3))
            self.image = ClickableLabel()
            self.image.setPixmap(pixmap)
            self.layout.addWidget(self.image)
        self.title_label = QLabel(f"<h3>{game.app_title}</h3>")
        self.title_label.setStyleSheet("""
                    QLabel{
                       text-align: center;
                    }
                """)
        self.title_label.setWordWrap(True)
        self.layout.addWidget(self.title_label)

        self.info_label = QLabel("")
        self.layout.addWidget(self.info_label)

        self.setLayout(self.layout)
        self.setFixedWidth(self.sizeHint().width())

    def mousePressEvent(self, a0) -> None:
        self.install()

    def install(self):
        logger.info("Install " + self.game.app_title)
        infos = InstallDialog().get_information()
        if infos != 0:
            path, max_workers = infos
            print(path, max_workers)