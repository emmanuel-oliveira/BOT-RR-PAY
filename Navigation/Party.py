from bs4 import BeautifulSoup
import time

from Utils import getValue, getEnv

ID_PARTY = getEnv("ID_PARTY")
LINK_PARTY = getEnv("LINK_PARTY")
SCRIPT_CLICK_BUTTON_BLUE = getEnv("SCRIPT_CLICK_BUTTON_BLUE")


def goToPartyPage(driver):
    linkParty = LINK_PARTY + str(ID_PARTY)
    driver.get(linkParty)
    driver.refresh()
    print("Listando usuários ativos")
    time.sleep(3)
    return driver


def getUsers(driver):
    for x in range(0, 50):
        try:
            driver.execute_script(SCRIPT_CLICK_BUTTON_BLUE)
        except:
            pass

    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "list_table tc"})
    tr = table.find_all("tr", {
        "class": ['list_link header_buttons_hover turn_0 list_only', 'list_link header_buttons_hover']})
    users = []
    for x in tr:
        if x.find("td", {"class": "list_head tip"}) is None and x.find("span",
                                                                       {"class": "green"}) is not None and x.find("td",
                                                                                                                  {
                                                                                                                      "class": "list_helper tip"}) is None:
            users.append(x.get("user", None))

    users = list(dict.fromkeys(users))
    print("Usuários ativos:", len(users))
    print("-------------------")
    return users
