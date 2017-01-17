from pywinauto.application import Application

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" ')
chromewidgetwin = app.Chrome_WidgetWin_1
chromewidgetwin.Wait('ready')

app.Kill_()