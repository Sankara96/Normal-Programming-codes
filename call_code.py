from time import sleep
from pywinauto.application import Application


app2 = Application().Connect(title=u'Call', class_name='QWidget')
qwidget2 = app2.Call
qwidget2.SetFocus()
qwidget2.Click()
sleep(2)
qwidget3 = qwidget2.QWidget14
qwidget3.PressMouseInput()
qwidget4 = qwidget2.QWidget9
qwidget4.Click()
qwidget5 = qwidget2.QWidget23
qwidget5.Click()
qwidget6 = qwidget2.QWidget17
qwidget6.Click()
qwidget7 = qwidget2.QWidget13
qwidget7.Click()
qwidget8 = qwidget2.QWidget21
qwidget8.Click()
qwidget5.Click()
qwidget6.Click()
qwidget9 = qwidget2.QWidget18
qwidget9.Click()
qwidget10 = qwidget2.QWidget16
qwidget10.Click()
sleep(3)
qwidget11 = qwidget2.QWidget20
qwidget11.Click()

