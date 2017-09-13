from logger.action.BrowserFactory import browser_factory

browser = browser_factory().get_browser()
browser.get("http://www.google.com")