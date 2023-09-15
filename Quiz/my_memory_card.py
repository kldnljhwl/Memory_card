#создай приложение для запоминания информации
from random import randint, shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, queres, relanswer, wro1, wro2, wro3):
        self.queres = queres
        self.relanswer = relanswer
        self.wro1 = wro1
        self.wro2 = wro2
        self.wro3 = wro3
quereses = list()
quereses.append(Question('Где Сибирь', 'В Сибири', 'В Китае', 'В Англии', 'В США'))
quereses.append(Question('Кто главный герой Метро 2033', 'Артем', 'Сэм', 'Ульман', 'Анна'))
quereses.append(Question('Где происходят действия Метро 2033', 'В Москве', 'В Сибири', 'В Питере', 'В Новгороде'))
app = QApplication([])
mainwin = QWidget()
mainwin.setWindowTitle('Memory Card')
mainwin.total = 0
mainwin.score = 0
title = QLabel('Какой национальности не существует?')
btn = QPushButton('Ответить')
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('') 
rbtn4 = QRadioButton('')
grpb = QGroupBox('Варианты ответов')
rgroup = QButtonGroup()
rgroup.addButton(rbtn1)
rgroup.addButton(rbtn2)
rgroup.addButton(rbtn3)
rgroup.addButton(rbtn4)
vertical1 = QVBoxLayout()
vertical2 = QVBoxLayout()
wide = QHBoxLayout()
vertical1.addWidget(rbtn1)
vertical1.addWidget(rbtn3)
vertical2.addWidget(rbtn2)
vertical2.addWidget(rbtn4)
wide.addLayout(vertical1)
wide.addLayout(vertical2)
grpb.setLayout(wide)
ansrgrpb = QGroupBox('Результат теста')
result = QLabel('Правильный/Неправильный')
riht = QLabel('Правильный')
layoutres = QVBoxLayout()
layoutres.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layoutres.addWidget(riht, alignment=Qt.AlignHCenter, stretch=2)
ansrgrpb.setLayout(layoutres)
layoutqueres = QHBoxLayout()
btnlayout = QHBoxLayout()
ansrlayout = QHBoxLayout()
layoutqueres.addWidget(title, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
ansrlayout.addWidget(grpb)
ansrlayout.addWidget(ansrgrpb)
ansrgrpb.hide()
btnlayout.addStretch(1)
btnlayout.addWidget(btn, stretch=2)
btnlayout.addStretch(1)
mainlayout = QVBoxLayout()
mainlayout.addLayout(layoutqueres, stretch=2)
mainlayout.addLayout(ansrlayout, stretch=8)
#U l t r a w i d e
mainlayout.addStretch(1)
mainlayout.addLayout(btnlayout, stretch=1)
mainlayout.addStretch(1)
mainlayout.setSpacing(5)
mainwin.setLayout(mainlayout)
def showres():
    grpb.hide()
    ansrgrpb.show()
    btn.setText('Следующий вопрос')
def showqueres():
    ansrgrpb.hide()
    grpb.show()
    btn.setText('Ответить')
    rgroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    rgroup.setExclusive(True)
def starttest():
    if btn.text() == 'Ответить':
        showres()
    else:
        showqueres()
ansers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q:Question):
    shuffle(ansers)
    ansers[0].setText(q.relanswer)
    ansers[1].setText(q.wro1)
    ansers[2].setText(q.wro2)
    ansers[3].setText(q.wro3)
    title.setText(q.queres)
    riht.setText(q.relanswer)
    showqueres()
def correct(res):
    result.setText(res)
    showres()
def setanswer():
    if ansers[0].isChecked():
        correct('Правильно')
        mainwin.score += 1
    else:
        correct('Неправильно')
def next_queres():
    mainwin.total += 1
    print('Статистика \n -Всего вопросов: ', mainwin.total, '\n -Правильных ответов: ', mainwin.score)
    current_queres = randint(0, len(quereses) - 1)
    q = quereses[current_queres]
    ask(q)
def click_ok():
    if btn.text() == 'Ответить':
        setanswer()
    else:
        next_queres()
mainwin.current_queres = -1
btn.clicked.connect(click_ok)
next_queres()
mainwin.show()
app.exec()