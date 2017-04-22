from selenium import webdriver
from logger.app.ExecutablePath import *
from logger.app.Kite import kite
from logger.app.Smallcase import smallcase

# browser = webdriver.Firefox(executable_path=executablepath.get_geckodriver_path())
print(get_chromedriver_path())
browser = webdriver.Chrome(executable_path=get_chromedriver_path())

kite = kite(browser)
kite.login_if_not()

smallcase = smallcase(browser)
smallcase.login_if_not()
smallcase.fetch_record()

# browser.quit()
