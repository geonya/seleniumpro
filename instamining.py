from argparse import Action
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(ChromeDriverManager().install())

main_hashtag = "dog"

browser.get(f"https://selenium-python.readthedocs.io/")

sidebar = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sphinxsidebarwrapper")))
sidebar_menus = sidebar.find_elements_by_class_name("toctree-l1")
for menu in sidebar_menus:
    ActionChains(browser).key_down(Keys.COMMAND).click(menu).perform()

for window in browser.window_handles:
    browser.switch_to.window(window)
    title = browser.find_element_by_tag_name("h1")
    print(title.text)
 
time.sleep(3)
browser.quit()