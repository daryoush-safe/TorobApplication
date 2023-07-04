import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pandas as pd

class Login(QtWidgets.QMainWindow):
    # our offline database -> data.csv
    csv_address = "C:\\University\\AP final project\\login code\\data.csv"
    df = pd.read_csv(csv_address)

    def __init__(self):
        super(Login, self).__init__()
        self.ui_address = "C:\\University\\AP final project\\gui\\login form\\login gui.ui"
        loadUi(self.ui_address, self)
        self.loginBtn.clicked.connect(self.login)
        self.showPass.stateChanged.connect(self.show_pass)
        self.createAccBtn.clicked.connect(self.goto_sign_up)

    @staticmethod
    def verify_user(username, password):
        if len(Login.df.loc[Login.df.name == username]) == 0:
            return "Username not found"
        elif len(df.loc[(Login.df.username == username) & (Login.df.password == password)]) == 0:
            return "Incorrect password"
        return True

    def login(self):
        if len(self.usernameInput.text()) == 0 or len(self.passwordInput.text()) == 0:
            self.errorLabel.setText("All fields are required to be filled.")

        result_verification = self.verify_user(
            self.usernameInput.text(),
            self.passwordInput.text()
            )

        if result_verification == True:
            print("login succssesfuli")
        else:
            self.errorLabel.setText(result_verification)


    def show_pass(self):
        if self.showPass.isChecked():
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)

    def goto_sign_up(self):
        pass

# main
app = QApplication(sys.argv)
login = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login)
widget.setFixedHeight(860)
widget.setFixedWidth(1300)
widget.show()
app.exec_()
