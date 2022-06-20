import sys
import bs4
import requests
from input import *
from work import *
from DataBase import *

estimation = {}


def selection(massive, value, estimation):
    i = 0
    m = massive[:]
    if value <= estimation:
        while sum(m) / len(m) < value and i <= 80:
            m.append(estimation)
            i += 1
    else:
        while sum(m) / len(m) > value and i <= 80:
            m.append(estimation)
            i += 1
    return i, sum(m) / len(m)


def calculation():
    global uiWork
    sr = round(sum(estimation[uiWork.comboBox.currentText()]) / len(estimation[uiWork.comboBox.currentText()]), 3)
    en, value = selection(estimation[uiWork.comboBox.currentText()], uiWork.doubleSpinBox.value(), uiWork.spinBox.value())
    uiWork.textBrowser.setText(f'По предмету "{uiWork.comboBox.currentText()}" ваш баллл на данный момент -'
                          f' {sr}. Чтобы получить балл {round(uiWork.doubleSpinBox.value(), 3)} '
                          f'вы можете получить {en} оценок типа {uiWork.spinBox.value()}, в '
                          f'таком случае ваш балл будет равен {round(value, 3)}')


def output():
    window.close()
    global ui_input
    ui_input = Ui_MainWindow_Input()
    ui_input.setupUi(window)
    ui_input.pushButton.clicked.connect(clickedButton)
    window.show()


def newWindow():
    window.close()
    global uiWork
    uiWork = Ui_MainWindow_Work()
    uiWork.setupUi(window)
    window.show()
    for i in estimation.keys():
        uiWork.comboBox.addItem(i)
    uiWork.pushButton.clicked.connect(calculation)
    uiWork.pushButton_2.clicked.connect(output)


def inp(ses):
    link = 'https://edu.gounn.ru/journal-student-grades-action/u.20056'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}
    res2 = ses.get(link, headers=headers)
    beaLink = bs4.BeautifulSoup(res2.text, 'html.parser')
    data = beaLink.find('div', {'class': 'layout-main'}).find('div', {'class': 'grid-body'}). \
        findAll('div', {'class': 'cell'})
    perv = data[0].get('name')
    estimation[perv] = []
    quantity = 1
    for i in data[1:]:
        estimation[i.get('name')] = []
        quantity += 1
        if i.get('name') == perv:
            break
    for i in data[:]:
        a = i.find('div', {'class': 'cell-data'})
        if isinstance(a, bs4.Tag) and (
                a.string == '5' or a.string == '4' or a.string == '3' or a.string == '2' or a.string == '1'):
            estimation[i.get('name')].append(int(a.string))


def clickedButton():
    if ui_input.checkBox.isChecked():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}
        auto = 'https://edu.gounn.ru/ajaxauthorize'
        data = {
            'username': ui_input.plainTextEdit_login.toPlainText(),
            'password': ui_input.plainTextEdit_password.toPlainText(),
            'return_uri': '/'
        }
        ses = requests.Session()
        res = ses.post(auto, data=data, headers=headers)
        if str(res.text)[-3] == 's':
            ui_input.label_dop_ifo.setText('<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">'
                                           + 'Логин или пароль введены неверно.' +
                                     '</span></p></body></html>')
            return
        controlBD.add(ui_input.plainTextEdit_login.toPlainText(), ui_input.plainTextEdit_password.toPlainText())
        inp(ses)
        newWindow()
    else:
        ui_input.label_dop_ifo.setText('<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">'
                                       + 'Вы не дали согласие.' +
                                 ' Пожалуйста, введите логин и пароль.</span></p></body></html>')


def checkStatus():  # проверка есть ли уже введёный аккаунт в бзд
    if len(controlBD.get()) != 0:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36'}
        auto = 'https://edu.gounn.ru/ajaxauthorize'
        data = {
            'username': controlBD.get()[0][0],
            'password': controlBD.get()[0][1],
            'return_uri': '/'
        }
        ses = requests.Session()
        ses.post(auto, data=data, headers=headers)
        inp(ses)
        return True
    else:
        return False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    controlBD = ControlDB()
    if checkStatus():
        newWindow()  # сразу открываем с введёнными данными
        sys.exit(app.exec())
    else:
        ui_input = Ui_MainWindow_Input()
        ui_input.setupUi(window)
        ui_input.pushButton.clicked.connect(clickedButton)
        window.show()
        sys.exit(app.exec())
