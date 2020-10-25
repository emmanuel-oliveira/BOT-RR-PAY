import json
import time
from selenium import webdriver
import chromedriver_autoinstaller

from Utils import getEnv

URL_LOGIN = getEnv("URL_LOGIN")
BUTTON_LOGIN_GOOGLE = getEnv("BUTTON_LOGIN_GOOGLE")
INPUT_GOOGLE_EMAIL = getEnv("INPUT_GOOGLE_EMAIL")
INPUT_GOOGLE_PASSWORD = getEnv("INPUT_GOOGLE_PASSWORD")

def navigateToLogin(driver):
    driver.get(URL_LOGIN)


def loginButton(driver):
    driver.find_element_by_xpath(BUTTON_LOGIN_GOOGLE).click()
    time.sleep(5)


def formLoginGoogle(driver, email, password):
    driver.find_element_by_xpath(INPUT_GOOGLE_EMAIL).send_keys(email)
    driver.find_element_by_xpath(INPUT_GOOGLE_EMAIL).send_keys(u'\ue007')

    # driver.find_element_by_xpath(nextForPassword).click()
    time.sleep(5)
    driver.find_element_by_xpath(INPUT_GOOGLE_PASSWORD).send_keys(password)
    driver.find_element_by_xpath(INPUT_GOOGLE_PASSWORD).send_keys(u'\ue007')
    # driver.find_element_by_xpath(buttonLogin).click()
    time.sleep(3)
    print("-------------------")
    print("Logado")
