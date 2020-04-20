import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainwindow import *
from validate import isUrl
import main


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = {}
        self.loginurl = ''
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.click)

    def click(self):
        if self.validate():
            self.run()

    def validate(self):
        self.url = self.urlEdit.text()
        if not isUrl.isurl(self.url):
            QMessageBox.about(self, '输入错误', '请正确输入url')
            return False

        if self.login.isChecked():
            self.loginurl = self.loginUrl.text()
            if not isUrl.isurl(self.loginurl):
                QMessageBox.about(self, '输入错误', '请正确输入url')
                return False
            self.user = self.username.text()
            self.pw = self.password.text()
            if self.user == '' or self.pw == '':
                QMessageBox.about(self, '输入错误', '若需登录用户名和密码不能为空。')
                return False
            self.flag = 1
            self.data = {
                'username': self.user,
                'password': self.pw
            }
        else:
            self.flag = 0
        return True

    def run(self):
        self.urlEdit.setEnabled(False)
        self.username.setEnabled(False)
        self.password.setEnabled(False)

        main.main(self.url, self.flag, self.loginurl, self.data)
        QMessageBox.about(self, '运行完毕', '运行完毕，请查看结果。')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())