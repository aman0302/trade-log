import sys,os
sys.path.append(os.path.dirname(os.getcwd()))

print (sys.path)

from logger.app.App import App

app = App()
app.start()


