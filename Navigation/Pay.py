import time

from Utils import getEnv

LINK_PAY_USER = getEnv("LINK_PAY_USER")
SCRIPT_SELECT_CASH = getEnv("SCRIPT_SELECT_CASH")
INPUT_CASH = getEnv("INPUT_CASH")
BUTTON_SEND_CASH = getEnv("BUTTON_SEND_CASH")


def payUser(driver, userId, salary):
    linkPayUser = LINK_PAY_USER + userId
    driver.get(linkPayUser)
    driver.refresh()
    time.sleep(3)
    driver.execute_script(SCRIPT_SELECT_CASH)
    driver.find_element_by_xpath(INPUT_CASH).clear()
    driver.find_element_by_xpath(INPUT_CASH).send_keys(salary)
    driver.find_element_by_xpath(BUTTON_SEND_CASH).click()
    time.sleep(2)
    print(f"Usuário {userId} pago")
