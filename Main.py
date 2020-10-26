import json
import os
import chromedriver_autoinstaller
from selenium import webdriver
from Navigation import navigateToLogin, loginButton, formLoginGoogle, payUser, goToPartyPage, getUsers


def startSession():
    print("PROGRAMA INICIADO")
    chromedriver_autoinstaller.install(cwd=True)
    webBrowser = webdriver.Chrome()
    global browserDriver
    browserDriver = webBrowser


def getSessionId():
    global browserDriver
    return browserDriver.session_id


def getCredentials():
    with open(os.getcwd() + "\\values.json", "r") as file:
        data = json.load(file)
        email = data['email']
        password = data['password']
        value = data["salary"]
    return email, password, value


EMAIL, PASSWORD, SALARY = getCredentials()


if __name__ == '__main__':
    startSession()
    navigateToLogin(browserDriver)
    loginButton(browserDriver)
    formLoginGoogle(browserDriver, EMAIL, PASSWORD)
    browserDriver = goToPartyPage(browserDriver)
    usersId = getUsers(browserDriver)
    list(map(lambda x: payUser(browserDriver, x, SALARY), usersId))
