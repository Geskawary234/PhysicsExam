# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sim settingsGwAZAG.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

from Methods import resource_path

class Ui_SimulationSettings(object):
    def setupUi(self, SimulationSettings):
        if not SimulationSettings.objectName():
            SimulationSettings.setObjectName(u"SimulationSettings")
        SimulationSettings.resize(1262, 368)
        self.centralwidget = QWidget(SimulationSettings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SurfAng = QSlider(self.centralwidget)
        self.SurfAng.setObjectName(u"SurfAng")
        self.SurfAng.setGeometry(QRect(260, 40, 331, 51))
        self.SurfAng.setMinimum(10)
        self.SurfAng.setMaximum(80)
        self.SurfAng.setValue(10)
        self.SurfAng.setSliderPosition(10)
        self.SurfAng.setTracking(True)
        self.SurfAng.setOrientation(Qt.Orientation.Horizontal)
        self.SurfAng.setInvertedAppearance(False)
        self.SurfAng.setTickPosition(QSlider.TickPosition.NoTicks)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 221, 21))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 250, 629, 91))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Pause = QPushButton(self.horizontalLayoutWidget)
        self.Pause.setObjectName(u"Pause")
        font1 = QFont()
        font1.setPointSize(26)
        self.Pause.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.Pause.setIcon(icon)
        self.Pause.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.Pause)

        self.Restart = QPushButton(self.horizontalLayoutWidget)
        self.Restart.setObjectName(u"Restart")
        self.Restart.setFont(font1)

        self.horizontalLayout.addWidget(self.Restart)

        self.SurfLen = QLabel(self.centralwidget)
        self.SurfLen.setObjectName(u"SurfLen")
        self.SurfLen.setGeometry(QRect(20, 190, 591, 51))
        self.SurfLen.setFont(font)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(650, 50, 607, 266))
        self.ObjTpe = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ObjTpe.setObjectName(u"ObjTpe")
        self.ObjTpe.setContentsMargins(0, 0, 0, 0)
        self.SphereSelect = QPushButton(self.horizontalLayoutWidget_2)
        self.SphereSelect.setObjectName(u"SphereSelect")
        icon1 = QIcon()
        icon1.addFile(resource_path("sphere.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SphereSelect.setIcon(icon1)
        self.SphereSelect.setIconSize(QSize(256, 256))

        self.ObjTpe.addWidget(self.SphereSelect)

        self.CylinderSelect = QPushButton(self.horizontalLayoutWidget_2)
        self.CylinderSelect.setObjectName(u"CylinderSelect")
        icon2 = QIcon()
        icon2.addFile(resource_path("cylinder.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CylinderSelect.setIcon(icon2)
        self.CylinderSelect.setIconSize(QSize(256, 256))

        self.ObjTpe.addWidget(self.CylinderSelect)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(810, 0, 331, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 241, 21))
        self.label_3.setFont(font)
        self.GroundLevel = QSlider(self.centralwidget)
        self.GroundLevel.setObjectName(u"GroundLevel")
        self.GroundLevel.setGeometry(QRect(260, 120, 331, 51))
        self.GroundLevel.setMinimum(0)
        self.GroundLevel.setMaximum(30)
        self.GroundLevel.setPageStep(0)
        self.GroundLevel.setValue(0)
        self.GroundLevel.setSliderPosition(0)
        self.GroundLevel.setTracking(True)
        self.GroundLevel.setOrientation(Qt.Orientation.Horizontal)
        self.GroundLevel.setTickPosition(QSlider.TickPosition.NoTicks)
        SimulationSettings.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SimulationSettings)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1262, 22))
        SimulationSettings.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SimulationSettings)
        self.statusbar.setObjectName(u"statusbar")
        SimulationSettings.setStatusBar(self.statusbar)

        self.retranslateUi(SimulationSettings)

        QMetaObject.connectSlotsByName(SimulationSettings)
    # setupUi

    def retranslateUi(self, SimulationSettings):
        SimulationSettings.setWindowTitle(QCoreApplication.translate("SimulationSettings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438", None))
#if QT_CONFIG(accessibility)
        self.SurfAng.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("SimulationSettings", u"\u0423\u0433\u043e\u043b \u043f\u043b\u043e\u0441\u043a\u043e\u0441\u0442\u0438", None))
        self.Pause.setText("")
        self.Restart.setText(QCoreApplication.translate("SimulationSettings", u"\u0420\u0435\u0441\u0442\u0430\u0440\u0442", None))
        self.SurfLen.setText(QCoreApplication.translate("SimulationSettings", u"\u0414\u043b\u0438\u043d\u043d\u0430 \u043f\u043b\u043e\u0441\u043a\u043e\u0441\u0442\u0438", None))
        self.SphereSelect.setText("")
        self.CylinderSelect.setText("")
        self.label_2.setText(QCoreApplication.translate("SimulationSettings", u"\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430: \u0428\u0430\u0440", None))
        self.label_3.setText(QCoreApplication.translate("SimulationSettings", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0437\u0435\u043c\u043b\u0438: 0.0 \u043c", None))
#if QT_CONFIG(accessibility)
        self.GroundLevel.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

