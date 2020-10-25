import time

from Utils import printLin


def enterPage(driver, linkHome):
    printLin()
    driver.get(linkHome)
    driver.refresh()
    time.sleep(5)