from PyQt6 import QtCore, QtGui, QtWidgets

from physics import converter

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setObjectName("MainWindow")
        self.resize(512, 523)
        self.setStyleSheet("#header{\n"
"    background-color: #7ec51f;\n"
"}\n"
"\n"
"#header_scale, #header_measurement{\n"
"    color: #fff;\n"
"}\n"
"\n"
"#frame_2, #frame_4 {\n"
"    background-color: #f1f8fc;\n"
"}\n"
"\n"
"#frame_3, #frame_5 {\n"
"    background-color: #feffff;\n"
"}\n"
"\n"
"#label_celcius, #label_fahrenheit, #label_kelvin, #label_rankine{\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.header)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_scale = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        self.header_scale.setFont(font)
        self.header_scale.setObjectName("header_scale")
        self.verticalLayout_2.addWidget(self.header_scale)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.header)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_measurement = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.header_measurement.setFont(font)
        self.header_measurement.setObjectName("header_measurement")
        self.verticalLayout_3.addWidget(self.header_measurement)
        self.horizontalLayout.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.header)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_celcius = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_celcius.sizePolicy().hasHeightForWidth())
        self.label_celcius.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_celcius.setFont(font)
        self.label_celcius.setObjectName("label_celcius")
        self.verticalLayout_4.addWidget(self.label_celcius)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.input_celcius = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.input_celcius.setFont(font)
        self.input_celcius.setText("")
        self.input_celcius.setObjectName("input_celcius")
        self.horizontalLayout_7.addWidget(self.input_celcius)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_fahrenheit = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fahrenheit.sizePolicy().hasHeightForWidth())
        self.label_fahrenheit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_fahrenheit.setFont(font)
        self.label_fahrenheit.setObjectName("label_fahrenheit")
        self.verticalLayout_5.addWidget(self.label_fahrenheit)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.input_fahrenheit = QtWidgets.QLineEdit(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.input_fahrenheit.setFont(font)
        self.input_fahrenheit.setText("")
        self.input_fahrenheit.setObjectName("input_fahrenheit")
        self.horizontalLayout_8.addWidget(self.input_fahrenheit)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_kelvin = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_kelvin.sizePolicy().hasHeightForWidth())
        self.label_kelvin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_kelvin.setFont(font)
        self.label_kelvin.setObjectName("label_kelvin")
        self.horizontalLayout_5.addWidget(self.label_kelvin)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.input_kelvin = QtWidgets.QLineEdit(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.input_kelvin.setFont(font)
        self.input_kelvin.setText("")
        self.input_kelvin.setObjectName("input_kelvin")
        self.horizontalLayout_9.addWidget(self.input_kelvin)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_14 = QtWidgets.QFrame(self.frame_5)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_rankine = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rankine.sizePolicy().hasHeightForWidth())
        self.label_rankine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.label_rankine.setFont(font)
        self.label_rankine.setObjectName("label_rankine")
        self.verticalLayout_6.addWidget(self.label_rankine)
        self.horizontalLayout_6.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_5)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.input_rankine = QtWidgets.QLineEdit(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.input_rankine.setFont(font)
        self.input_rankine.setText("")
        self.input_rankine.setObjectName("input_rankine")

        #Source
        self.reg_exp_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[+-]?\\d*[\\.,]?\\d+"))
        self.input_rankine.setValidator(self.reg_exp_validator)
        self.input_celcius.setValidator(self.reg_exp_validator)
        self.input_fahrenheit.setValidator(self.reg_exp_validator)
        self.input_kelvin.setValidator(self.reg_exp_validator)

        self.horizontalLayout_10.addWidget(self.input_rankine)
        self.horizontalLayout_6.addWidget(self.frame_15)
        self.verticalLayout.addWidget(self.frame_5)
        self.setCentralWidget(self.centralwidget)

        self.retranslate_ui()
        self.set_events()
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_events(self) -> None:
        self.input_celcius.textEdited.connect(self.celcius_changed)
        self.input_fahrenheit.textEdited.connect(self.fahrenheit_changed)
        self.input_kelvin.textEdited.connect(self.kelvin_changed)
        self.input_rankine.textEdited.connect(self.rankine_changed)

    def celcius_changed(self, text: str) -> None:
        if self.check_input_incongruities(text):
            return
        temperature = MainWindow.get_numeric_text(text)
        self.input_fahrenheit.setText(f"{converter.celcius_to_fahrenheit(temperature):.2f}")
        self.input_rankine.setText(f"{converter.celcius_to_rankine(temperature):.2f}")
        self.input_kelvin.setText(f"{converter.celcius_to_kelvin(temperature):.2f}")

    def fahrenheit_changed(self, text: str) -> None:
        if self.check_input_incongruities(text):
            return
        temperature = MainWindow.get_numeric_text(text)
        self.input_celcius.setText(f"{converter.fahrenheit_to_celcius(temperature):.2f}")
        self.input_rankine.setText(f"{converter.fahrenheit_to_rankine(temperature):.2f}")
        self.input_kelvin.setText(f"{converter.fahrenheit_to_kelvin(temperature):.2f}")

    def kelvin_changed(self, text: str) -> None:
        if self.check_input_incongruities(text):
            return
        temperature = MainWindow.get_numeric_text(text)
        self.input_celcius.setText(f"{converter.kelvin_to_celcius(temperature):.2f}")
        self.input_rankine.setText(f"{converter.kelvin_to_rankine(temperature):.2f}")
        self.input_fahrenheit.setText(f"{converter.kelvin_to_farenheit(temperature):.2f}")

    def rankine_changed(self, text: str) -> None:
        if self.check_input_incongruities(text):
            return
        temperature = MainWindow.get_numeric_text(text)
        self.input_celcius.setText(f"{converter.rankine_to_celcius(temperature):.2f}")
        self.input_kelvin.setText(f"{converter.rankine_to_kelvin(temperature):.2f}")
        self.input_fahrenheit.setText(f"{converter.rankine_to_fahrenheit(temperature):.2f}")

    def clear_all_inputs(self):
        self.input_celcius.setText("")
        self.input_fahrenheit.setText("")
        self.input_kelvin.setText("")
        self.input_rankine.setText("")


    def check_input_incongruities(self, text: str) -> bool:
        if len(text.strip()) == 0:
            self.clear_all_inputs()
            return True
        if len(text) == 1 and (text[0] == "-" or text[0] == "+"):
            return True
        return False

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Temperature Converter"))
        self.header_scale.setText(_translate("MainWindow", "Scale"))
        self.header_measurement.setText(_translate("MainWindow", "Measurement"))
        self.label_celcius.setText(_translate("MainWindow", "Celcius"))
        self.label_fahrenheit.setText(_translate("MainWindow", "Fahrenheit"))
        self.label_kelvin.setText(_translate("MainWindow", "Kelvin"))
        self.label_rankine.setText(_translate("MainWindow", "Rankine"))
    
    @staticmethod
    def remove_not_number(text: str) -> float:
        char = text[-1:]
        text = text[:-1]
        if char == ".":
            if text.__contains__("."):
                return text
            if len(text) > 0:
                return text + char
            return text
        if not char.isnumeric():
            return text
        return text + char

    @staticmethod
    def get_numeric_text(text: str) -> float:
        number = float(text)
        return number