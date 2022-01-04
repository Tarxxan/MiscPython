import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\cpang\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.get("https://my.concordia.ca/psp/upprpr9/?cmd=login&languageCd=ENG")
id = browser.find_element_by_id("userid")
id.send_keys("")

password = browser.find_element_by_id("pwd")
password.send_keys("")

password.send_keys(Keys.RETURN)
browser.get(
    "https://my.concordia.ca/psp/upprpr9/EMPLOYEE/EMPL/s/WEBLIB_CONCORD.CU_SIS_INFO.FieldFormula"
    ".IScript_COOP_Learning?PORTALPARAM_PTCNAV=CU_COOP_LEARNING&EOPP.SCNode=EMPL&EOPP.SCPortal=EMPLOYEE&EOPP.SCName"
    "=CU_STUDENT_REQUESTS&EOPP.SCLabel=Student%20Services&EOPP.SCPTfname=CU_STUDENT_REQUESTS&FolderPath"
    "=PORTAL_ROOT_OBJECT.CU_STUDENT_REQUESTS.CU_COOP_LEARNING&IsFolder=false")
browser.get("https://icope.concordia.ca/myAccount/coopjobs.htm")

while "refresh":
    time.sleep(240+randint(0,240))
    tabs = browser.window_handles
    print(tabs)
    for tab in tabs:
        browser.refresh()
        if len(tabs) != 1:
            current = browser.current_url
        else:
            current = ""

        if current == "https://icope.concordia.ca/notLoggedIn.htm":
            browser.close()
            browser.switch_to.window(tabs[1])
            break;

        if len(tabs) > 1:
            browser.switch_to.window(tab)


