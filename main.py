from PyQt5 import QtWidgets
import sys
import bs4
import requests
from input import Ui_MainWindow


def clickedButton():
    if ui.checkBox.isChecked():
        print(ui.plainTextEdit_login.toPlainText())
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}
        auto = 'https://edu.gounn.ru/ajaxauthorize'
        link = 'https://edu.gounn.ru/journal-student-grades-action/u.20056'
        data = {
            'username': ui.plainTextEdit_login.toPlainText(),
            'password': ui.plainTextEdit_password.toPlainText(),
            'return_uri': '/'
        }
        ses = requests.Session()
        res = ses.post(auto, data=data, headers=headers)
        print(res.text)
        if str(res.text)[-3] == 's':
            ui.label_dop_ifo.setText('<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">'
                                     + 'Логин или пароль введены неверно.' +
                                     '</span></p></body></html>')
            return
        res2 = ses.get(link, headers=headers)
        beaLink = bs4.BeautifulSoup(res2.text, 'html.parser')
        data = beaLink.find('div', {'class': 'layout-main'}).find('div', {'class': 'grid-body'}). \
            findAll('div', {'class': 'cell'})
        perv = data[0].get('name')
        estimation = {perv: []}
        quantity = 1
        print(beaLink.text)
        for i in data[1:]:
            estimation[i.get('name')] = []
            quantity += 1
            if i.get('name') == perv:
                break
        for i in data[quantity:]:
            a = i.find('div', {'class': 'cell-data'})
            if isinstance(a, bs4.Tag) and (
                    a.string == '5' or a.string == '4' or a.string == '3' or a.string == '2' or a.string == '1'):
                estimation[i.get('name')].append(int(a.string))
        print(estimation)
        window.close()

    else:
        ui.label_dop_ifo.setText('<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">'
                                 + 'Вы не дали согласие.' +
                                 ' Пожалуйста, введите логин и пароль.</span></p></body></html>')


def checkStatus():  # проверка есть ли уже введёный аккаунт в бзд
    return False


if __name__ == '__main__':
    if checkStatus():
        pass  # сразу открываем с введёнными данными
    else:
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        ui.pushButton.clicked.connect(clickedButton)
        window.show()
        sys.exit(app.exec())
