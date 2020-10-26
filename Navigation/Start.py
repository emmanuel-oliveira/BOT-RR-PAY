import chromedriver_autoinstaller
from selenium import webdriver

from Utils import getProjectFolder


def startSession():
    print("PROGRAMA INICIADO")

    """pathProject = getProjectFolder()"""
    # browser = "chromedriver.exe"
    # fullRoute = getProjectFolder() + "\\" + browser
    chromedriver_autoinstaller.install()
    webBrowser = webdriver.Chrome()
    global browserDriver
    browserDriver = webBrowser


def getSessionId():
    global browserDriver
    return browserDriver.session_id
