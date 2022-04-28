import json
import random

from PyQt5 import QtCore, QtGui, QtWidgets

# Percentage will equal weight
# NOTE: FILE PARTIALLY GENERATED USING QT DESIGNER
# SEE STARTPROGRAM.PY FOR INITIALIZATION

import GeneratedLoot
import NoAvailableLoot
from GenerateDB import GenerateDB
from dbOps import dbOps


class Ui_MainWindow(object):
    dpOps = dbOps()
    destinyDB = dpOps.db.destinyDict
    generateDB = GenerateDB()

    # TODO: In order to finish implementing weight system, use random.choices to return an engram type
    # TODO: If the list is empty, then ignore that value in the weights unless choices weights can ignore things like that
    list_Of_Toggleables = []
    list_Of_Season_Booleans = []
    list_Of_Engram_Weights = [60, 35, 5]
    current_Engram_Chance_Total = 100
    list_Of_Engram_Types = ['Rare', 'Legendary', 'Exotic']

    jsonPerks = None

    def __init__(self):

        self.centralwidget = None
        self.verticalLayoutWidget = None
        self.PossibleEngrams = None
        self.label = None
        self.engram_Selectables = None
        self.rare_Engram_Checkbox = None
        self.legendary_Engram_Checkbox = None
        self.exotic_Engram_CheckBox = None
        self.verticalLayoutWidget_6 = None
        self.odds_Layout = None
        self.label_3 = None
        self.rare_Vertical_Layout = None
        self.rare_Chances_Horizontal_Layout = None
        self.rare_Chance_Label = None
        self.rare_Percentage_Chance = None
        self.rare_Chances_slider = None
        self.exotic_Chances_Vertical_Layout = None
        self.exotic_Horizonatal_Chances_Layout = None
        self.exotic_Chance_Label = None
        self.exotic_Percentage_Chance = None
        self.exotic_Chances_Slider = None
        self.legendary_Chances_Vertical_Layout = None
        self.legendary_Horizonatal_Chances_Layout = None
        self.legendary_Chance_Label = None
        self.legendary_Percentage_Chance = None
        self.legendary_Chances_Slider = None
        self.horizontalLayoutWidget_2 = None
        self.season_Toggleables_Layout = None
        self.seasons_One_To_Eight_Layout = None
        self.red_War_Toggleable = None
        self.osiris_Toggleable = None
        self.warmind_Toggleable = None
        self.outlaw_Toggleable = None
        self.forge_Toggleable = None
        self.drifter_Toggleabel = None
        self.opulence_Toggleable = None
        self.undying_Toggleable = None
        self.Seasons_Eight_To_Sixteen_Layout = None
        self.dawn_Toggleable = None
        self.worthy_Toggleable = None
        self.arrivals_Toggleable = None
        self.hunt_Toggleable = None
        self.chosen_Toggleable = None
        self.splicer_Toggleable = None
        self.lost_Toggleable = None
        self.risen_Toggleable = None
        self.verticalLayoutWidget_9 = None
        self.class_Type_Vertical_Layout = None
        self.type_Label = None
        self.warlock_RB = None
        self.hunter_RB = None
        self.titan_RB = None
        self.engramGenerate = None
        self.randomDropWindow = None
        self.noAvailableLootWindow = None
        # Load JSON File
        file = open("bin/Weapon Perks.json")
        self.jsonPerks = json.load(file)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 365)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 0, 411, 186))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.PossibleEngrams = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.PossibleEngrams.setContentsMargins(0, 0, 0, 0)
        self.PossibleEngrams.setObjectName("PossibleEngrams")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()

        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.PossibleEngrams.addWidget(self.label)

        self.engram_Selectables = QtWidgets.QHBoxLayout()
        self.engram_Selectables.setObjectName("engram_Selectables")

        self.rare_Engram_Checkbox = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rare_Engram_Checkbox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bin/images/Token_Engram_Rare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rare_Engram_Checkbox.setIcon(icon)
        self.rare_Engram_Checkbox.setIconSize(QtCore.QSize(100, 100))
        self.rare_Engram_Checkbox.setCheckable(True)
        self.rare_Engram_Checkbox.setChecked(True)
        self.rare_Engram_Checkbox.setFlat(True)
        self.rare_Engram_Checkbox.setObjectName("rare_Engram_Checkbox")
        self.engram_Selectables.addWidget(self.rare_Engram_Checkbox)

        self.legendary_Engram_Checkbox = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.legendary_Engram_Checkbox.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bin/images/Token_Engram_Legendary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.legendary_Engram_Checkbox.setIcon(icon1)
        self.legendary_Engram_Checkbox.setIconSize(QtCore.QSize(100, 100))
        self.legendary_Engram_Checkbox.setCheckable(True)
        self.legendary_Engram_Checkbox.setChecked(True)
        self.legendary_Engram_Checkbox.setFlat(True)
        self.legendary_Engram_Checkbox.setObjectName("legendary_Engram_Checkbox")
        self.engram_Selectables.addWidget(self.legendary_Engram_Checkbox)

        self.exotic_Engram_CheckBox = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exotic_Engram_CheckBox.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bin/images/Token_Engram_Exotic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exotic_Engram_CheckBox.setIcon(icon2)
        self.exotic_Engram_CheckBox.setIconSize(QtCore.QSize(100, 100))
        self.exotic_Engram_CheckBox.setCheckable(True)
        self.exotic_Engram_CheckBox.setChecked(True)
        self.exotic_Engram_CheckBox.setDefault(False)
        self.exotic_Engram_CheckBox.setFlat(True)
        self.exotic_Engram_CheckBox.setObjectName("exotic_Engram_CheckBox")
        self.engram_Selectables.addWidget(self.exotic_Engram_CheckBox)

        self.PossibleEngrams.addLayout(self.engram_Selectables)

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(810, 0, 321, 264))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")

        self.odds_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.odds_Layout.setContentsMargins(0, 0, 0, 0)
        self.odds_Layout.setObjectName("odds_Layout")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.odds_Layout.addWidget(self.label_3)

        self.rare_Vertical_Layout = QtWidgets.QVBoxLayout()
        self.rare_Vertical_Layout.setObjectName("rare_Vertical_Layout")
        self.rare_Chances_Horizontal_Layout = QtWidgets.QHBoxLayout()
        self.rare_Chances_Horizontal_Layout.setObjectName("rare_Chances_Horizontal_Layout")
        self.rare_Chance_Label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.rare_Chance_Label.setFont(font)
        self.rare_Chance_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.rare_Chance_Label.setObjectName("rare_Chance_Label")
        self.rare_Chances_Horizontal_Layout.addWidget(self.rare_Chance_Label)
        self.rare_Percentage_Chance = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.rare_Percentage_Chance.setFont(font)
        self.rare_Percentage_Chance.setAlignment(QtCore.Qt.AlignCenter)
        self.rare_Percentage_Chance.setObjectName("rare_Percentage_Chance")
        self.rare_Chances_Horizontal_Layout.addWidget(self.rare_Percentage_Chance)
        self.rare_Vertical_Layout.addLayout(self.rare_Chances_Horizontal_Layout)
        self.rare_Chances_slider = QtWidgets.QSlider(self.verticalLayoutWidget_6)
        self.rare_Chances_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rare_Chances_slider.setObjectName("rare_Chances_slider")
        self.rare_Chances_slider.setMaximum(100)
        self.rare_Chances_slider.setValue(60)
        self.rare_Chance_Label.setText("60%")
        self.rare_Chances_slider.valueChanged.connect(
            lambda: self.onSliderChange(self.rare_Chances_slider, self.rare_Percentage_Chance))

        self.rare_Vertical_Layout.addWidget(self.rare_Chances_slider)
        self.odds_Layout.addLayout(self.rare_Vertical_Layout)

        self.exotic_Chances_Vertical_Layout = QtWidgets.QVBoxLayout()
        self.exotic_Chances_Vertical_Layout.setObjectName("exotic_Chances_Vertical_Layout")
        self.exotic_Horizonatal_Chances_Layout = QtWidgets.QHBoxLayout()
        self.exotic_Horizonatal_Chances_Layout.setObjectName("exotic_Horizonatal_Chances_Layout")
        self.exotic_Chance_Label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.exotic_Chance_Label.setFont(font)
        self.exotic_Chance_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.exotic_Chance_Label.setObjectName("exotic_Chance_Label")
        self.exotic_Horizonatal_Chances_Layout.addWidget(self.exotic_Chance_Label)
        self.exotic_Percentage_Chance = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.exotic_Percentage_Chance.setFont(font)
        self.exotic_Percentage_Chance.setAlignment(QtCore.Qt.AlignCenter)
        self.exotic_Percentage_Chance.setObjectName("exotic_Percentage_Chance")
        self.exotic_Horizonatal_Chances_Layout.addWidget(self.exotic_Percentage_Chance)
        self.exotic_Chances_Vertical_Layout.addLayout(self.exotic_Horizonatal_Chances_Layout)
        self.exotic_Chances_Slider = QtWidgets.QSlider(self.verticalLayoutWidget_6)
        self.exotic_Chances_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.exotic_Chances_Slider.setObjectName("exotic_Chances_Slider")
        self.exotic_Chances_Slider.setMaximum(100)
        self.exotic_Chances_Slider.setValue(5)
        self.exotic_Chance_Label.setText("5%")
        self.exotic_Chances_Slider.valueChanged.connect(
            lambda: self.onSliderChange(self.exotic_Chances_Slider, self.exotic_Percentage_Chance))

        self.exotic_Chances_Vertical_Layout.addWidget(self.exotic_Chances_Slider)
        self.odds_Layout.addLayout(self.exotic_Chances_Vertical_Layout)

        self.legendary_Chances_Vertical_Layout = QtWidgets.QVBoxLayout()
        self.legendary_Chances_Vertical_Layout.setObjectName("legendary_Chances_Vertical_Layout")
        self.legendary_Horizonatal_Chances_Layout = QtWidgets.QHBoxLayout()
        self.legendary_Horizonatal_Chances_Layout.setObjectName("legendary_Horizonatal_Chances_Layout")
        self.legendary_Chance_Label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.legendary_Chance_Label.setFont(font)
        self.legendary_Chance_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.legendary_Chance_Label.setObjectName("legendary_Chance_Label")
        self.legendary_Horizonatal_Chances_Layout.addWidget(self.legendary_Chance_Label)
        self.legendary_Percentage_Chance = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.legendary_Percentage_Chance.setFont(font)
        self.legendary_Percentage_Chance.setAlignment(QtCore.Qt.AlignCenter)
        self.legendary_Percentage_Chance.setObjectName("legendary_Percentage_Chance")
        self.legendary_Chance_Label.setText("35%")
        self.legendary_Horizonatal_Chances_Layout.addWidget(self.legendary_Percentage_Chance)
        self.legendary_Chances_Vertical_Layout.addLayout(self.legendary_Horizonatal_Chances_Layout)
        self.legendary_Chances_Slider = QtWidgets.QSlider(self.verticalLayoutWidget_6)
        self.legendary_Chances_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.legendary_Chances_Slider.setObjectName("legendary_Chances_Slider")
        self.legendary_Chances_Slider.setMaximum(100)
        self.legendary_Chances_Slider.setValue(35)
        self.legendary_Chances_Slider.valueChanged.connect(
            lambda: self.onSliderChange(self.legendary_Chances_Slider, self.legendary_Percentage_Chance))
        self.legendary_Chances_Vertical_Layout.addWidget(self.legendary_Chances_Slider)
        self.odds_Layout.addLayout(self.legendary_Chances_Vertical_Layout)

        # For Toggleables, it may be worth making them into a loop. This is a bit ridiculous
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(420, 0, 381, 358))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.season_Toggleables_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.season_Toggleables_Layout.setContentsMargins(0, 0, 0, 0)
        self.season_Toggleables_Layout.setObjectName("season_Toggleables_Layout")
        self.seasons_One_To_Eight_Layout = QtWidgets.QVBoxLayout()
        self.seasons_One_To_Eight_Layout.setObjectName("seasons_One_To_Eight_Layout")

        # TODO: Loop over toggleables, possibly store in .JSON
        # TODO: Add CSS styling to ALL buttons, green when checked, red when unchecked.
        self.red_War_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.red_War_Toggleable)
        self.red_War_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.red_War_Toggleable))
        # Stylesheet needed for each toggleable button. (REALLY need loops)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.red_War_Toggleable.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Red_War_season_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.red_War_Toggleable.setIcon(icon3)
        self.red_War_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.red_War_Toggleable.setCheckable(True)
        self.red_War_Toggleable.setFlat(False)
        self.red_War_Toggleable.setChecked(True)
        self.red_War_Toggleable.setObjectName("red_War_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.red_War_Toggleable)

        self.osiris_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.osiris_Toggleable)
        self.osiris_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.osiris_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.osiris_Toggleable.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Curse_of_Osiris_season_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.osiris_Toggleable.setIcon(icon4)
        self.osiris_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.osiris_Toggleable.setCheckable(True)
        self.osiris_Toggleable.setChecked(True)
        self.osiris_Toggleable.setObjectName("osiris_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.osiris_Toggleable)

        self.warmind_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.warmind_Toggleable)
        self.warmind_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.warmind_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.warmind_Toggleable.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Warmind_season_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.warmind_Toggleable.setIcon(icon5)
        self.warmind_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.warmind_Toggleable.setCheckable(True)
        self.warmind_Toggleable.setChecked(True)
        self.warmind_Toggleable.setObjectName("warmind_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.warmind_Toggleable)

        self.outlaw_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.outlaw_Toggleable)
        self.outlaw_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.outlaw_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.outlaw_Toggleable.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Outlaw_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.outlaw_Toggleable.setIcon(icon6)
        self.outlaw_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.outlaw_Toggleable.setCheckable(True)
        self.outlaw_Toggleable.setChecked(True)
        self.outlaw_Toggleable.setObjectName("outlaw_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.outlaw_Toggleable)

        self.forge_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.forge_Toggleable)
        self.forge_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.forge_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.forge_Toggleable.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Forge_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.forge_Toggleable.setIcon(icon7)
        self.forge_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.forge_Toggleable.setCheckable(True)
        self.forge_Toggleable.setChecked(True)
        self.forge_Toggleable.setObjectName("forge_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.forge_Toggleable)

        self.drifter_Toggleabel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.drifter_Toggleabel)
        self.drifter_Toggleabel.clicked.connect(lambda: self.onSeasonUnchecked(self.drifter_Toggleabel))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.drifter_Toggleabel.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Drifter_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.drifter_Toggleabel.setIcon(icon8)
        self.drifter_Toggleabel.setIconSize(QtCore.QSize(30, 30))
        self.drifter_Toggleabel.setCheckable(True)
        self.drifter_Toggleabel.setChecked(True)
        self.drifter_Toggleabel.setObjectName("drifter_Toggleabel")
        self.seasons_One_To_Eight_Layout.addWidget(self.drifter_Toggleabel)

        self.opulence_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.opulence_Toggleable)
        self.opulence_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.opulence_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.opulence_Toggleable.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_Opulence_icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.opulence_Toggleable.setIcon(icon9)
        self.opulence_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.opulence_Toggleable.setCheckable(True)
        self.opulence_Toggleable.setChecked(True)
        self.opulence_Toggleable.setObjectName("opulence_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.opulence_Toggleable)

        self.undying_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.undying_Toggleable)
        self.undying_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.undying_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.undying_Toggleable.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Undying_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.undying_Toggleable.setIcon(icon10)
        self.undying_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.undying_Toggleable.setCheckable(True)
        self.undying_Toggleable.setChecked(True)
        self.undying_Toggleable.setObjectName("undying_Toggleable")
        self.seasons_One_To_Eight_Layout.addWidget(self.undying_Toggleable)
        self.season_Toggleables_Layout.addLayout(self.seasons_One_To_Eight_Layout)

        self.Seasons_Eight_To_Sixteen_Layout = QtWidgets.QVBoxLayout()
        self.Seasons_Eight_To_Sixteen_Layout.setObjectName("Seasons_Eight_To_Sixteen_Layout")

        self.dawn_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.dawn_Toggleable)
        self.dawn_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.dawn_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.dawn_Toggleable.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_Dawn_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.dawn_Toggleable.setIcon(icon11)
        self.dawn_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.dawn_Toggleable.setCheckable(True)
        self.dawn_Toggleable.setChecked(True)
        self.dawn_Toggleable.setObjectName("dawn_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.dawn_Toggleable)

        self.worthy_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.worthy_Toggleable)
        self.worthy_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.worthy_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.worthy_Toggleable.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Worthy_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.worthy_Toggleable.setIcon(icon12)
        self.worthy_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.worthy_Toggleable.setCheckable(True)
        self.worthy_Toggleable.setChecked(True)
        self.worthy_Toggleable.setObjectName("worthy_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.worthy_Toggleable)

        self.arrivals_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.arrivals_Toggleable)
        self.arrivals_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.arrivals_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.arrivals_Toggleable.setFont(font)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_Arrivals_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.arrivals_Toggleable.setIcon(icon13)
        self.arrivals_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.arrivals_Toggleable.setCheckable(True)
        self.arrivals_Toggleable.setChecked(True)
        self.arrivals_Toggleable.setObjectName("arrivals_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.arrivals_Toggleable)

        self.hunt_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.hunt_Toggleable)
        self.hunt_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.hunt_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.hunt_Toggleable.setFont(font)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Hunt_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.hunt_Toggleable.setIcon(icon14)
        self.hunt_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.hunt_Toggleable.setCheckable(True)
        self.hunt_Toggleable.setChecked(True)
        self.hunt_Toggleable.setObjectName("hunt_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.hunt_Toggleable)

        self.chosen_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.chosen_Toggleable)
        self.chosen_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.chosen_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.chosen_Toggleable.setFont(font)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Chosen_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.chosen_Toggleable.setIcon(icon15)
        self.chosen_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.chosen_Toggleable.setCheckable(True)
        self.chosen_Toggleable.setChecked(True)
        self.chosen_Toggleable.setObjectName("chosen_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.chosen_Toggleable)

        self.splicer_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.splicer_Toggleable)
        self.splicer_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.splicer_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.splicer_Toggleable.setFont(font)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Splicer_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.splicer_Toggleable.setIcon(icon16)
        self.splicer_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.splicer_Toggleable.setCheckable(True)
        self.splicer_Toggleable.setChecked(True)
        self.splicer_Toggleable.setObjectName("splicer_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.splicer_Toggleable)

        self.lost_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.lost_Toggleable)
        self.lost_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.lost_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.lost_Toggleable.setFont(font)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Lost_icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.lost_Toggleable.setIcon(icon17)
        self.lost_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.lost_Toggleable.setCheckable(True)
        self.lost_Toggleable.setChecked(True)
        self.lost_Toggleable.setObjectName("lost_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.lost_Toggleable)

        self.risen_Toggleable = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.list_Of_Toggleables.append(self.risen_Toggleable)
        self.risen_Toggleable.clicked.connect(lambda: self.onSeasonUnchecked(self.risen_Toggleable))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.risen_Toggleable.setFont(font)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("bin/images/icons/30px-Season_of_the_Risen_Icon.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.risen_Toggleable.setIcon(icon18)
        self.risen_Toggleable.setIconSize(QtCore.QSize(30, 30))
        self.risen_Toggleable.setCheckable(True)
        self.risen_Toggleable.setChecked(True)
        self.risen_Toggleable.setObjectName("risen_Toggleable")
        self.Seasons_Eight_To_Sixteen_Layout.addWidget(self.risen_Toggleable)
        self.season_Toggleables_Layout.addLayout(self.Seasons_Eight_To_Sixteen_Layout)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 189, 411, 153))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")

        self.class_Type_Vertical_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.class_Type_Vertical_Layout.setContentsMargins(0, 0, 0, 0)
        self.class_Type_Vertical_Layout.setObjectName("class_Type_Vertical_Layout")
        self.type_Label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.type_Label.setFont(font)
        self.type_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_Label.setObjectName("type_Label")
        self.class_Type_Vertical_Layout.addWidget(self.type_Label)
        self.warlock_RB = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.warlock_RB.setFont(font)
        self.warlock_RB.setChecked(True)
        self.warlock_RB.setObjectName("warlock_Type_RB")
        self.class_Type_Vertical_Layout.addWidget(self.warlock_RB)
        self.hunter_RB = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.hunter_RB.setFont(font)
        self.hunter_RB.setObjectName("warlock_Type_RB_2")
        self.class_Type_Vertical_Layout.addWidget(self.hunter_RB)
        self.titan_RB = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.titan_RB.setFont(font)
        self.titan_RB.setObjectName("warlock_Type_RB_3")
        self.class_Type_Vertical_Layout.addWidget(self.titan_RB)
        self.engramGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.engramGenerate.setGeometry(QtCore.QRect(810, 270, 321, 91))
        self.engramGenerate.clicked.connect(lambda: self.engramGenerateClick())
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.engramGenerate.setFont(font)
        self.engramGenerate.setObjectName("engramGenerate")

        # Adds the boolean values of the toggleable buttons to a list that can be crosschecked with the seasons.
        for i in self.list_Of_Toggleables:
            self.list_Of_Season_Booleans.append(i.isChecked())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loot Generator"))
        self.label.setText(_translate("MainWindow", "Possible Rolls"))
        self.label_3.setText(_translate("MainWindow", "Odds"))
        self.rare_Chance_Label.setText(_translate("MainWindow", "Rare Engram "))
        self.rare_Percentage_Chance.setText(_translate("MainWindow", "60%"))
        self.exotic_Chance_Label.setText(_translate("MainWindow", "Exotic Engram"))
        self.exotic_Percentage_Chance.setText(_translate("MainWindow", "5%"))
        self.legendary_Chance_Label.setText(_translate("MainWindow", "Legendary Engram"))
        self.legendary_Percentage_Chance.setText(_translate("MainWindow", "35%"))
        self.red_War_Toggleable.setText(_translate("MainWindow", "Red War"))
        self.osiris_Toggleable.setText(_translate("MainWindow", "Osiris"))
        self.warmind_Toggleable.setText(_translate("MainWindow", "Warmind"))
        self.outlaw_Toggleable.setText(_translate("MainWindow", "Outlaw"))
        self.forge_Toggleable.setText(_translate("MainWindow", "Forge"))
        self.drifter_Toggleabel.setText(_translate("MainWindow", "Drifter"))
        self.opulence_Toggleable.setText(_translate("MainWindow", "Opulence"))
        self.undying_Toggleable.setText(_translate("MainWindow", "Undying"))
        self.dawn_Toggleable.setText(_translate("MainWindow", "Dawn"))
        self.worthy_Toggleable.setText(_translate("MainWindow", "Worthy"))
        self.arrivals_Toggleable.setText(_translate("MainWindow", "Arrivals"))
        self.hunt_Toggleable.setText(_translate("MainWindow", "hunt"))
        self.chosen_Toggleable.setText(_translate("MainWindow", "Chosen"))
        self.splicer_Toggleable.setText(_translate("MainWindow", "Splicer"))
        self.lost_Toggleable.setText(_translate("MainWindow", "Lost"))
        self.risen_Toggleable.setText(_translate("MainWindow", "Risen"))
        self.type_Label.setText(_translate("MainWindow", "Class"))
        self.warlock_RB.setText(_translate("MainWindow", "Warlock"))
        self.hunter_RB.setText(_translate("MainWindow", "Hunter"))
        self.titan_RB.setText(_translate("MainWindow", "Titan"))
        self.engramGenerate.setText(_translate("MainWindow", "Drop an Engram"))

    # get the checked class type
    def getClassType(self, randomItem):
        classType = 3
        print("Checking item type...")
        if randomItem['type'] in self.generateDB.weapon_Types:
            return classType
        print("Weapon")
        if self.warlock_RB.isChecked():
            print("Warlock")
            classType = 2
        elif self.hunter_RB.isChecked():
            print("Hunter")
            classType = 1
        else:
            print("Titan")
            classType = 0
        return classType

    # get the checked class type
    def getClassTypeModified(self):
        classType = 0
        if self.warlock_RB.isChecked():
            print("Warlock")
            classType = 2
        elif self.hunter_RB.isChecked():
            print("Hunter")
            classType = 1
        else:
            print("Titan")
            classType = 0
        return classType

    def getRandomPerks(self, randomItem):
        print(randomItem in self.jsonPerks)

        perksSetOne = self.jsonPerks[randomItem]['Slot 1 Perks']
        perkOne = random.choice(perksSetOne)
        print(perkOne)

        perksSetTwo = self.jsonPerks[randomItem]['Slot 2 Perks']
        perkTwo = random.choice(perksSetTwo)
        print(perkTwo)

        perksSetThree = self.jsonPerks[randomItem]['Slot 3 Perks']
        perkThree = random.choice(perksSetThree)
        print(perkThree)

        return [perkOne, perkTwo, perkThree]

    @staticmethod
    def generateScreenshotUrl(urlEnd):
        return "https://bungie.net/" + urlEnd

    #TODO: When you uncheck engrams and recheck them + mess with sliders, things get messy.
    #TODO: Add method and possibly list to check if certain egnrams are selected. This will solve the issue.
    def getAllowedEngrams(self, randomItem):
        print("Checking allowed engram type....")
        list_Of_Allowed_Engrams = []
        if self.legendary_Engram_Checkbox.isChecked():
            list_Of_Allowed_Engrams.append("Legendary")
        if self.exotic_Engram_CheckBox.isChecked():
            list_Of_Allowed_Engrams.append("Exotic")
        if self.rare_Engram_Checkbox.isChecked():
            list_Of_Allowed_Engrams.append("Rare")

        if randomItem['Rarity'] in list_Of_Allowed_Engrams:
            return True
        else:
            return False

    def getAllowedEngramsList(self):
        print("Checking allowed engram type....")
        list_Of_Allowed_Engrams = []
        if self.legendary_Engram_Checkbox.isChecked():
            list_Of_Allowed_Engrams.append("Legendary")
        if self.exotic_Engram_CheckBox.isChecked():
            list_Of_Allowed_Engrams.append("Exotic")
        if self.rare_Engram_Checkbox.isChecked():
            list_Of_Allowed_Engrams.append("Rare")
        return list_Of_Allowed_Engrams

    # TODO: Use weights to determine the TYPE of engram and then get a random item from that list.
    # Creates A sub dictionary of allowed items based  on class restriction
    def createSubDictionaries(self, allowed_Engram_Type, itemDictionary, classType):
        list_Of_Allowed_items = []
        print("Length of allowed booleans: ", len(self.list_Of_Season_Booleans))
        for i in itemDictionary:
            if itemDictionary[i]['Rarity'] == allowed_Engram_Type and (itemDictionary[i]['classType'] == classType
                                                                       or itemDictionary[i]['classType'] == 3):
                # print("createSubDictionaries: 2")
                try:
                    if self.list_Of_Season_Booleans[itemDictionary[i]['season'] - 1]:
                        list_Of_Allowed_items.append(i)
                except IndexError:
                    print("Index our of bounds maybe?")

        return list_Of_Allowed_items

    def testSubDictionary(self):
        exoticList = self.createSubDictionaries('Exotic', self.destinyDB, 0)
        for i in exoticList:
            print(i)

    def getEngramType(self):
        allowedEngrams = self.getAllowedEngramsList()
        if 'Rare' not in allowedEngrams:
            self.list_Of_Engram_Weights[0] = 0
        elif 'Legendary' not in allowedEngrams:
            self.list_Of_Engram_Weights[1] = 0
        elif 'Exotic' not in allowedEngrams:
            self.list_Of_Engram_Weights[2] = 0

        try:
            return random.choices(self.list_Of_Engram_Types, weights=self.list_Of_Engram_Weights)[0]
        except:
            self.openPopUpNoAvailableRolls()

    def returnRandomLoot(self):
        engramType = self.getEngramType()
        print(engramType)
        print("engramType Successful")
        allowedList = self.createSubDictionaries(engramType, self.destinyDB, self.getClassTypeModified())
        print("allowedList Successful")
        print(len(allowedList))

        try:
            itemToReturn = random.choice(allowedList)
            return itemToReturn
        except:
            self.openPopUpNoAvailableRolls()
            return None

    def getRandomLoot(self):
        randomItem = self.returnRandomLoot()
        if randomItem is None:
            return
        randomItemDict = self.destinyDB.get(randomItem)
        # Prevents the program from crashing if the item doesn't have a season. Only affects some items, I'm not too
        # sure how to fix it right now.
        # if randomItemDict['season'] is None or randomItemDict['season'] == "No season Identified":
        #     randomItemDict['season'] = 1
        # TODO: If Screenshot is not available, then display 'no image available' image.
        screenshot_Url = "No Screenshot Available"
        perks = None

        # prints the random roll information to the terminal.
        print('------------------------------')
        print("YOUR RANDOM ROLL IS:")
        print("Name: ", randomItem)
        print("Type: ", randomItemDict['type'])
        print("Season:", randomItemDict['season'])
        print("Rarity:", randomItemDict['Rarity'])

        if 'screenshot' in randomItemDict:
            # Make Screenshot Link
            screenshot_Url = self.generateScreenshotUrl(randomItemDict['screenshot'])
            print("Screenshot: ", screenshot_Url)
        else:
            print(screenshot_Url)

        if randomItemDict['classType'] != 3:
            armorType = randomItemDict['armor tier']
        else:
            armorType = "None"
            perks = self.getRandomPerks(randomItemDict['type'])

        # Create new Dialog Box with Returned Roll and send params to GeneratedLoot.py
        self.randomDropWindow = QtWidgets.QDialog()
        lootUI = GeneratedLoot.GeneratedLootUI()
        lootUI.setupUi(self.randomDropWindow, randomItem, randomItemDict['type'], randomItemDict['season'],
                       randomItemDict['Rarity'], screenshot_Url, armorType,
                       perks)

        self.randomDropWindow.show()

    # Runs the item generator. May move item to its own class for easy access later.
    def engramGenerateClick(self):
        print("Engram Generating, please stand by")
        self.getRandomLoot()

    def openPopUpNoAvailableRolls(self):
        self.noAvailableLootWindow = QtWidgets.QDialog()
        noLootUI = NoAvailableLoot.Ui_Dialog()
        noLootUI.setupUi(self.noAvailableLootWindow)
        self.noAvailableLootWindow.show()

    def onSliderChange(self, slider, label):
        if slider.objectName() == "legendary_Chances_Slider":
            self.list_Of_Engram_Weights[1] = slider.value()
        elif slider.objectName() == "exotic_Chances_Slider":
            self.list_Of_Engram_Weights[2] = slider.value()
        elif slider.objectName() == "rare_Chances_slider":
            self.list_Of_Engram_Weights[0] = slider.value()
        print(self.list_Of_Engram_Weights)

        label.setText(str(slider.value()) + "%")
        self.current_Engram_Chance_Total = self.rare_Chances_slider.value() + self.legendary_Chances_Slider.value() \
                                           + self.exotic_Chances_Slider.value()
        allowedEngrams = self.getAllowedEngramsList()
        if 'Rare' not in allowedEngrams:
            self.list_Of_Engram_Weights[0] = 0
        elif 'Legendary' not in allowedEngrams:
            self.list_Of_Engram_Weights[1] = 0
        elif 'Exotic' not in allowedEngrams:
            self.list_Of_Engram_Weights[2] = 0

    def onSeasonUnchecked(self, button):
        if button.objectName() == "red_War_Toggleable":
            print("Red War Toggleable: ", self.list_Of_Season_Booleans[0])
            self.list_Of_Season_Booleans[0] = (not self.list_Of_Season_Booleans[0])
            print("Red War Toggleable: ", self.list_Of_Season_Booleans[0])
        elif button.objectName() == "osiris_Toggleable":
            print("Osiris Toggleable: ", self.list_Of_Season_Booleans[1])
            self.list_Of_Season_Booleans[1] = not self.list_Of_Season_Booleans[1]
            print("Osiris Toggleable: ", self.list_Of_Season_Booleans[1])
        elif button.objectName() == "warmind_Toggleable":
            self.list_Of_Season_Booleans[2] = not self.list_Of_Season_Booleans[2]
        elif button.objectName() == "outlaw_Toggleable":
            self.list_Of_Season_Booleans[3] = not self.list_Of_Season_Booleans[3]
        elif button.objectName() == "forge_Toggleable":
            self.list_Of_Season_Booleans[4] = not self.list_Of_Season_Booleans[4]
        elif button.objectName() == "drifter_Toggleabel":
            self.list_Of_Season_Booleans[5] = not self.list_Of_Season_Booleans[5]
        elif button.objectName() == "opulence_Toggleable":
            self.list_Of_Season_Booleans[6] = not self.list_Of_Season_Booleans[6]
        elif button.objectName() == "undying_Toggleable":
            self.list_Of_Season_Booleans[7] = not self.list_Of_Season_Booleans[7]
        elif button.objectName() == "dawn_Toggleable":
            self.list_Of_Season_Booleans[8] = not self.list_Of_Season_Booleans[8]
        elif button.objectName() == "worthy_Toggleable":
            self.list_Of_Season_Booleans[9] = not self.list_Of_Season_Booleans[9]
        elif button.objectName() == "arrivals_Toggleable":
            self.list_Of_Season_Booleans[10] = not self.list_Of_Season_Booleans[10]
        elif button.objectName() == "hunt_Toggleable":
            self.list_Of_Season_Booleans[11] = not self.list_Of_Season_Booleans[11]
        elif button.objectName() == "chosen_Toggleable":
            self.list_Of_Season_Booleans[12] = not self.list_Of_Season_Booleans[12]
        elif button.objectName() == "splicer_Toggleable":
            self.list_Of_Season_Booleans[13] = not self.list_Of_Season_Booleans[13]
        elif button.objectName() == "lost_Toggleable":
            self.list_Of_Season_Booleans[14] = not self.list_Of_Season_Booleans[14]
        elif button.objectName() == "risen_Toggleable":
            print("Risen Toggleable: ", self.list_Of_Season_Booleans[15])
            self.list_Of_Season_Booleans[15] = not self.list_Of_Season_Booleans[15]
            print("Risen Toggleable: ", self.list_Of_Season_Booleans[15])
