# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgramUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(991, 752)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setBaseSize(QtCore.QSize(1, 1))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(False)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.ctrl_220V_button = QtWidgets.QPushButton(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.ctrl_220V_button.setPalette(palette)
        self.ctrl_220V_button.setCheckable(True)
        self.ctrl_220V_button.setObjectName("ctrl_220V_button")
        self.gridLayout.addWidget(self.ctrl_220V_button, 2, 1, 1, 1)
        self.timeDisp = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeDisp.setFont(font)
        self.timeDisp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeDisp.setTextFormat(QtCore.Qt.AutoText)
        self.timeDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.timeDisp.setObjectName("timeDisp")
        self.gridLayout.addWidget(self.timeDisp, 2, 0, 1, 1)
        self.baud_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.baud_comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baud_comboBox.sizePolicy().hasHeightForWidth())
        self.baud_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.baud_comboBox.setFont(font)
        self.baud_comboBox.setObjectName("baud_comboBox")
        self.baud_comboBox.addItem("")
        self.baud_comboBox.addItem("")
        self.gridLayout.addWidget(self.baud_comboBox, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Msg_TextEdit = QtWidgets.QTextBrowser(self.groupBox_2)
        self.Msg_TextEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Msg_TextEdit.sizePolicy().hasHeightForWidth())
        self.Msg_TextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Msg_TextEdit.setFont(font)
        self.Msg_TextEdit.setAcceptDrops(True)
        self.Msg_TextEdit.setReadOnly(True)
        self.Msg_TextEdit.setObjectName("Msg_TextEdit")
        self.gridLayout_6.addWidget(self.Msg_TextEdit, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.AnalogVideo_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.AnalogVideo_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.AnalogVideo_checkBox.setFont(font)
        self.AnalogVideo_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AnalogVideo_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalogVideo_checkBox.setChecked(False)
        self.AnalogVideo_checkBox.setAutoRepeat(False)
        self.AnalogVideo_checkBox.setTristate(False)
        self.AnalogVideo_checkBox.setObjectName("AnalogVideo_checkBox")
        self.gridLayout_3.addWidget(self.AnalogVideo_checkBox, 6, 0, 1, 1)
        self.Box4_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box4_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box4_checkBox.setFont(font)
        self.Box4_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box4_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box4_checkBox.setCheckable(True)
        self.Box4_checkBox.setChecked(False)
        self.Box4_checkBox.setAutoRepeat(False)
        self.Box4_checkBox.setTristate(False)
        self.Box4_checkBox.setObjectName("Box4_checkBox")
        self.gridLayout_3.addWidget(self.Box4_checkBox, 1, 5, 1, 1)
        self.BoardRefresh_button = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoardRefresh_button.sizePolicy().hasHeightForWidth())
        self.BoardRefresh_button.setSizePolicy(sizePolicy)
        self.BoardRefresh_button.setObjectName("BoardRefresh_button")
        self.gridLayout_3.addWidget(self.BoardRefresh_button, 0, 0, 1, 1)
        self.Progress_bar = QtWidgets.QProgressBar(self.groupBox_3)
        self.Progress_bar.setProperty("value", 99)
        self.Progress_bar.setObjectName("Progress_bar")
        self.gridLayout_3.addWidget(self.Progress_bar, 0, 2, 1, 6)
        self.Box2_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box2_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box2_checkBox.setFont(font)
        self.Box2_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box2_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box2_checkBox.setCheckable(True)
        self.Box2_checkBox.setChecked(False)
        self.Box2_checkBox.setAutoRepeat(False)
        self.Box2_checkBox.setTristate(False)
        self.Box2_checkBox.setObjectName("Box2_checkBox")
        self.gridLayout_3.addWidget(self.Box2_checkBox, 1, 3, 1, 1)
        self.Box3_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box3_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box3_checkBox.setFont(font)
        self.Box3_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box3_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box3_checkBox.setCheckable(True)
        self.Box3_checkBox.setChecked(False)
        self.Box3_checkBox.setAutoRepeat(False)
        self.Box3_checkBox.setTristate(False)
        self.Box3_checkBox.setObjectName("Box3_checkBox")
        self.gridLayout_3.addWidget(self.Box3_checkBox, 1, 4, 1, 1)
        self.Lvds_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.Lvds_comboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lvds_comboBox.sizePolicy().hasHeightForWidth())
        self.Lvds_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Lvds_comboBox.setFont(font)
        self.Lvds_comboBox.setObjectName("Lvds_comboBox")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.Lvds_comboBox.addItem("")
        self.gridLayout_3.addWidget(self.Lvds_comboBox, 0, 1, 1, 1)
        self.Box7_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box7_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box7_checkBox.setFont(font)
        self.Box7_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box7_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box7_checkBox.setCheckable(True)
        self.Box7_checkBox.setChecked(False)
        self.Box7_checkBox.setAutoRepeat(False)
        self.Box7_checkBox.setTristate(False)
        self.Box7_checkBox.setObjectName("Box7_checkBox")
        self.gridLayout_3.addWidget(self.Box7_checkBox, 1, 8, 1, 1)
        self.Audio_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Audio_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Audio_checkBox.setFont(font)
        self.Audio_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Audio_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Audio_checkBox.setChecked(False)
        self.Audio_checkBox.setAutoRepeat(False)
        self.Audio_checkBox.setTristate(False)
        self.Audio_checkBox.setObjectName("Audio_checkBox")
        self.gridLayout_3.addWidget(self.Audio_checkBox, 2, 0, 1, 1)
        self.AnalogIO_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.AnalogIO_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.AnalogIO_checkBox.setFont(font)
        self.AnalogIO_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AnalogIO_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalogIO_checkBox.setChecked(False)
        self.AnalogIO_checkBox.setAutoRepeat(False)
        self.AnalogIO_checkBox.setTristate(False)
        self.AnalogIO_checkBox.setObjectName("AnalogIO_checkBox")
        self.gridLayout_3.addWidget(self.AnalogIO_checkBox, 3, 0, 1, 1)
        self.downloadMode_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.downloadMode_comboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadMode_comboBox.sizePolicy().hasHeightForWidth())
        self.downloadMode_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.downloadMode_comboBox.setFont(font)
        self.downloadMode_comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.downloadMode_comboBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.downloadMode_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.downloadMode_comboBox.setFrame(True)
        self.downloadMode_comboBox.setObjectName("downloadMode_comboBox")
        self.downloadMode_comboBox.addItem("")
        self.downloadMode_comboBox.addItem("")
        self.downloadMode_comboBox.addItem("")
        self.downloadMode_comboBox.addItem("")
        self.gridLayout_3.addWidget(self.downloadMode_comboBox, 1, 0, 1, 1)
        self.Box1_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box1_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box1_checkBox.setFont(font)
        self.Box1_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box1_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box1_checkBox.setCheckable(True)
        self.Box1_checkBox.setChecked(False)
        self.Box1_checkBox.setAutoRepeat(False)
        self.Box1_checkBox.setTristate(False)
        self.Box1_checkBox.setObjectName("Box1_checkBox")
        self.gridLayout_3.addWidget(self.Box1_checkBox, 1, 2, 1, 1)
        self.Box5_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box5_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box5_checkBox.setFont(font)
        self.Box5_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box5_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box5_checkBox.setCheckable(True)
        self.Box5_checkBox.setChecked(False)
        self.Box5_checkBox.setAutoRepeat(False)
        self.Box5_checkBox.setTristate(False)
        self.Box5_checkBox.setObjectName("Box5_checkBox")
        self.gridLayout_3.addWidget(self.Box5_checkBox, 1, 6, 1, 1)
        self.download_button = QtWidgets.QPushButton(self.groupBox_3)
        self.download_button.setEnabled(False)
        self.download_button.setToolTip("")
        self.download_button.setObjectName("download_button")
        self.gridLayout_3.addWidget(self.download_button, 0, 8, 1, 1)
        self.Box6_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box6_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Box6_checkBox.setFont(font)
        self.Box6_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box6_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box6_checkBox.setCheckable(True)
        self.Box6_checkBox.setChecked(False)
        self.Box6_checkBox.setAutoRepeat(False)
        self.Box6_checkBox.setTristate(False)
        self.Box6_checkBox.setObjectName("Box6_checkBox")
        self.gridLayout_3.addWidget(self.Box6_checkBox, 1, 7, 1, 1)
        self.Box0_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Box0_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Box0_checkBox.setFont(font)
        self.Box0_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Box0_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Box0_checkBox.setCheckable(True)
        self.Box0_checkBox.setChecked(False)
        self.Box0_checkBox.setAutoRepeat(False)
        self.Box0_checkBox.setTristate(False)
        self.Box0_checkBox.setObjectName("Box0_checkBox")
        self.gridLayout_3.addWidget(self.Box0_checkBox, 1, 1, 1, 1)
        self.DigitalIO_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.DigitalIO_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DigitalIO_checkBox.setFont(font)
        self.DigitalIO_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.DigitalIO_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DigitalIO_checkBox.setChecked(False)
        self.DigitalIO_checkBox.setAutoRepeat(False)
        self.DigitalIO_checkBox.setTristate(False)
        self.DigitalIO_checkBox.setObjectName("DigitalIO_checkBox")
        self.gridLayout_3.addWidget(self.DigitalIO_checkBox, 4, 0, 1, 1)
        self.PScontrol_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.PScontrol_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PScontrol_checkBox.setFont(font)
        self.PScontrol_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PScontrol_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PScontrol_checkBox.setChecked(False)
        self.PScontrol_checkBox.setAutoRepeat(False)
        self.PScontrol_checkBox.setTristate(False)
        self.PScontrol_checkBox.setObjectName("PScontrol_checkBox")
        self.gridLayout_3.addWidget(self.PScontrol_checkBox, 5, 0, 1, 1)
        self.LVDS_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.LVDS_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LVDS_checkBox.setFont(font)
        self.LVDS_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LVDS_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LVDS_checkBox.setChecked(False)
        self.LVDS_checkBox.setAutoRepeat(False)
        self.LVDS_checkBox.setTristate(False)
        self.LVDS_checkBox.setObjectName("LVDS_checkBox")
        self.gridLayout_3.addWidget(self.LVDS_checkBox, 8, 0, 1, 1)
        self.AnalogFpga_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.AnalogFpga_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.AnalogFpga_checkBox.setFont(font)
        self.AnalogFpga_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AnalogFpga_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalogFpga_checkBox.setChecked(False)
        self.AnalogFpga_checkBox.setAutoRepeat(False)
        self.AnalogFpga_checkBox.setTristate(False)
        self.AnalogFpga_checkBox.setObjectName("AnalogFpga_checkBox")
        self.gridLayout_3.addWidget(self.AnalogFpga_checkBox, 13, 0, 1, 1)
        self.DigitalFpga_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.DigitalFpga_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DigitalFpga_checkBox.setFont(font)
        self.DigitalFpga_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.DigitalFpga_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DigitalFpga_checkBox.setChecked(False)
        self.DigitalFpga_checkBox.setAutoRepeat(False)
        self.DigitalFpga_checkBox.setTristate(False)
        self.DigitalFpga_checkBox.setObjectName("DigitalFpga_checkBox")
        self.gridLayout_3.addWidget(self.DigitalFpga_checkBox, 14, 0, 1, 1)
        self.LvdsFpga_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.LvdsFpga_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LvdsFpga_checkBox.setFont(font)
        self.LvdsFpga_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LvdsFpga_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LvdsFpga_checkBox.setChecked(False)
        self.LvdsFpga_checkBox.setAutoRepeat(False)
        self.LvdsFpga_checkBox.setTristate(False)
        self.LvdsFpga_checkBox.setObjectName("LvdsFpga_checkBox")
        self.gridLayout_3.addWidget(self.LvdsFpga_checkBox, 15, 0, 1, 1)
        self.TypecSwitch_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.TypecSwitch_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TypecSwitch_checkBox.setFont(font)
        self.TypecSwitch_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TypecSwitch_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TypecSwitch_checkBox.setChecked(False)
        self.TypecSwitch_checkBox.setAutoRepeat(False)
        self.TypecSwitch_checkBox.setTristate(False)
        self.TypecSwitch_checkBox.setObjectName("TypecSwitch_checkBox")
        self.gridLayout_3.addWidget(self.TypecSwitch_checkBox, 10, 0, 1, 1)
        self.PcieBase_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.PcieBase_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PcieBase_checkBox.setFont(font)
        self.PcieBase_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PcieBase_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PcieBase_checkBox.setChecked(False)
        self.PcieBase_checkBox.setAutoRepeat(False)
        self.PcieBase_checkBox.setTristate(False)
        self.PcieBase_checkBox.setObjectName("PcieBase_checkBox")
        self.gridLayout_3.addWidget(self.PcieBase_checkBox, 9, 0, 1, 1)
        self.UsbMonitor_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.UsbMonitor_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.UsbMonitor_checkBox.setFont(font)
        self.UsbMonitor_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.UsbMonitor_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UsbMonitor_checkBox.setChecked(False)
        self.UsbMonitor_checkBox.setAutoRepeat(False)
        self.UsbMonitor_checkBox.setTristate(False)
        self.UsbMonitor_checkBox.setObjectName("UsbMonitor_checkBox")
        self.gridLayout_3.addWidget(self.UsbMonitor_checkBox, 11, 0, 1, 1)
        self.DigitalVideo_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.DigitalVideo_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DigitalVideo_checkBox.setFont(font)
        self.DigitalVideo_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.DigitalVideo_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DigitalVideo_checkBox.setChecked(False)
        self.DigitalVideo_checkBox.setAutoRepeat(False)
        self.DigitalVideo_checkBox.setTristate(False)
        self.DigitalVideo_checkBox.setObjectName("DigitalVideo_checkBox")
        self.gridLayout_3.addWidget(self.DigitalVideo_checkBox, 7, 0, 1, 1)
        self.Usb_PD_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.Usb_PD_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Usb_PD_checkBox.setFont(font)
        self.Usb_PD_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Usb_PD_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Usb_PD_checkBox.setChecked(False)
        self.Usb_PD_checkBox.setAutoRepeat(False)
        self.Usb_PD_checkBox.setTristate(False)
        self.Usb_PD_checkBox.setObjectName("Usb_PD_checkBox")
        self.gridLayout_3.addWidget(self.Usb_PD_checkBox, 16, 0, 1, 1)
        self.UsbMonitor2_checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.UsbMonitor2_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.UsbMonitor2_checkBox.setFont(font)
        self.UsbMonitor2_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.UsbMonitor2_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UsbMonitor2_checkBox.setChecked(False)
        self.UsbMonitor2_checkBox.setAutoRepeat(False)
        self.UsbMonitor2_checkBox.setTristate(False)
        self.UsbMonitor2_checkBox.setObjectName("UsbMonitor2_checkBox")
        self.gridLayout_3.addWidget(self.UsbMonitor2_checkBox, 12, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ProgramUpdate"))
        self.groupBox.setTitle(_translate("Form", "串口设置"))
        self.lineEdit.setText(_translate("Form", "00 00 00 00 00 00 00 00"))
        self.ctrl_220V_button.setText(_translate("Form", "220V"))
        self.ctrl_220V_button.setShortcut(_translate("Form", "F4"))
        self.timeDisp.setText(_translate("Form", "00:00:00"))
        self.baud_comboBox.setItemText(0, _translate("Form", "115200"))
        self.baud_comboBox.setItemText(1, _translate("Form", "921600"))
        self.groupBox_2.setTitle(_translate("Form", "提示消息"))
        self.Msg_TextEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">欢迎使用，请选择串口号...</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Form", "板卡节点"))
        self.AnalogVideo_checkBox.setText(_translate("Form", "模拟信号"))
        self.Box4_checkBox.setText(_translate("Form", "机箱 4"))
        self.BoardRefresh_button.setText(_translate("Form", "刷新节点"))
        self.BoardRefresh_button.setShortcut(_translate("Form", "F5"))
        self.Box2_checkBox.setText(_translate("Form", "机箱 2"))
        self.Box3_checkBox.setText(_translate("Form", "机箱 3"))
        self.Lvds_comboBox.setItemText(0, _translate("Form", "NORMAL"))
        self.Lvds_comboBox.setItemText(1, _translate("Form", "LVDS"))
        self.Lvds_comboBox.setItemText(2, _translate("Form", "N10"))
        self.Lvds_comboBox.setItemText(3, _translate("Form", "N86_1"))
        self.Lvds_comboBox.setItemText(4, _translate("Form", "N81"))
        self.Lvds_comboBox.setItemText(5, _translate("Form", "PT320"))
        self.Lvds_comboBox.setItemText(6, _translate("Form", "N86_2"))
        self.Lvds_comboBox.setItemText(7, _translate("Form", "PT320_2"))
        self.Lvds_comboBox.setItemText(8, _translate("Form", "EXT_2"))
        self.Lvds_comboBox.setItemText(9, _translate("Form", "Bootloader"))
        self.Box7_checkBox.setText(_translate("Form", "机箱 7"))
        self.Audio_checkBox.setText(_translate("Form", "音频板"))
        self.AnalogIO_checkBox.setText(_translate("Form", "模拟IO板"))
        self.downloadMode_comboBox.setCurrentText(_translate("Form", "NODE"))
        self.downloadMode_comboBox.setItemText(0, _translate("Form", "NODE"))
        self.downloadMode_comboBox.setItemText(1, _translate("Form", "BOARD"))
        self.downloadMode_comboBox.setItemText(2, _translate("Form", "BOX"))
        self.downloadMode_comboBox.setItemText(3, _translate("Form", "ALL"))
        self.Box1_checkBox.setText(_translate("Form", "机箱 1"))
        self.Box5_checkBox.setText(_translate("Form", "机箱 5"))
        self.download_button.setText(_translate("Form", "开始下载"))
        self.download_button.setShortcut(_translate("Form", "F8"))
        self.Box6_checkBox.setText(_translate("Form", "机箱 6"))
        self.Box0_checkBox.setText(_translate("Form", "机箱 0"))
        self.DigitalIO_checkBox.setText(_translate("Form", "数字IO板"))
        self.PScontrol_checkBox.setText(_translate("Form", "电源板"))
        self.LVDS_checkBox.setText(_translate("Form", "LVDS板"))
        self.AnalogFpga_checkBox.setText(_translate("Form", "模拟 FPGA"))
        self.DigitalFpga_checkBox.setText(_translate("Form", "数字 FPGA"))
        self.LvdsFpga_checkBox.setText(_translate("Form", "LVDS FPGA"))
        self.TypecSwitch_checkBox.setText(_translate("Form", "Type-c Switch"))
        self.PcieBase_checkBox.setText(_translate("Form", "底板"))
        self.UsbMonitor_checkBox.setText(_translate("Form", "Usb Monitor"))
        self.DigitalVideo_checkBox.setText(_translate("Form", "数字信号"))
        self.Usb_PD_checkBox.setText(_translate("Form", "Usb PD"))
        self.UsbMonitor2_checkBox.setText(_translate("Form", "Usb Monitor2"))
