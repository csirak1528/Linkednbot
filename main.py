from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


browser = webdriver.Chrome('/Users/calebsirak/linkdenbot/chromedriver')

MESSAGE = """
Lets Talk about Distributed Systems

"""
userData = {
    "username": "rudisystems@gmail.com",
    "password": "rudinet21"
}

search_link = "https://www.linkedin.com/search/results/people/?keywords=software%20engineer&network=%5B%22F%22%2C%22S%22%5D&origin=FACETED_SEARCH"


def loadLinkedin():
    browser.get("https://www.linkedin.com/")


def click(selector, id=False):
    fail = False
    for i in range(10):
        if not fail:
            fail = True
            try:
                if id:
                    browser.find_element_by_id(selector).click()
                else:
                    browser.find_element_by_css_selector(selector).click()
                time.sleep(1)
            except:
                fail = False
        else:
            break
        time.sleep(1)


def inputData(selector, data):
    time.sleep(1)
    browser.find_element_by_css_selector(selector).send_keys(data)


def setup():
    loadLinkedin()
    click("body > nav > div > a.nav__button-secondary")
    inputData("#username", userData["username"])
    inputData("#password", userData["password"])
    click("#organic-div > form > div.login__form_action_container > button")
    click("#remember-me-prompt__form-secondary > button")
    browser.get(search_link)


def getHref(selector, k=False):
    time.sleep(1)
    try:
        link = browser.find_element_by_css_selector(
            selector).get_attribute("href")
        browser.execute_script(f"window.open('{link}', '_blank');")
        time.sleep(2)
        # browser.get(link)
        if not k:
            changeTab(0)
        else:
            changeTab(0)
            browser.close()
    except:
        pass


def changeTab(id):
    browser.switch_to.window(browser.window_handles[id])
    time.sleep(1)


def changePage():
    try:
        for i in range(5):
            try:
                browser.find_element_by_xpath(
                    "/html/body/div[6]/div[3]/div/div[1]/div/div[1]/main/div/div/div[2]/div[2]/div/button[2]").click()
            except:
                pass
    except:
        for i in range(5):
            try:
                browser.find_element_by_xpath(
                    "/html/body/div[6]/div[3]/div/div[1]/div/div[1]/main/div/div/div[5]/div/div/button[2]").click()
            except:
                pass


def loadPeople():
    for i in range(1, 12):
        time.sleep(2)
        try:
            selector = f"/html/body/div[6]/div[3]/div/div[1]/div/div[1]/main/div/div/div[2]/ul/li[{i}]/div/div/div[3]/div/button"
            browser.find_element_by_xpath(selector).click()
            selector = "/html/body/div[3]/div/div/div[3]/button[1]"
            time.sleep(2)
            browser.find_element_by_xpath(selector).click()
            time.sleep(1)
            browser.find_element_by_css_selector(
                "#custom-message").send_keys(MESSAGE)
            worked = False
            for i in range(5):
                if not worked:
                    time.sleep(.4)
                    try:
                        browser.find_element_by_xpath(
                            "/html/body/div[3]/div/div/div[3]/button[2]").click()
                        worked = True
                    except:
                        worked = False
                        pass
            if not worked:
                browser.find_element_by_xpath("").click()

            time.sleep(1)
        except:
            pass


if __name__ == "__main__":
    setup()
    while True:
        loadPeople()
        changePage()
