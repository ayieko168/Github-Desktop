from PyQt5.QtWidgets import *
from DesidnFiles.MainUi import *

class CustomCombobox(QComboBox):

    pass

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.combo = CustomCombobox()
        self.combo.addItems(["NEW1", "NEW2"])
        self.ui.verticalLayout.addWidget(self.combo)




if __name__ == "__main__":
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()









