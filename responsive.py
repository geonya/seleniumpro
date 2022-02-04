import requests
from os import mkdir
from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ResponsiveTester:

    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480, 960, 1366, 1920]
    

    def get_title(self, url):
        url_parts = url.split(".")
        if url_parts[0].split("/")[2] == "www":
            title = url_parts[1]
        else:
            title = url_parts[0].split("/")[2]
        return title

    def check_url(self, url):
        if "http" not in url:
            url_parts = url.split(".")
            url_parts[0] = "https://" + url_parts[0]
            url = ".".join(url_parts)
        try:
            r = requests.get(url)
            if r.status_code == 200 :
                print(url + " is up ✅ ")
            elif r.status_code == 400 :
                print(url + " is down ❌")
        except:
            print("error ❌")
        
        return url
        

    def screenshot(self, url):
        try:
            self.browser.get(url)
            BROWER_HEIGHT = 1055
            title = self.get_title(url)
            mkdir(f"screenshots/{title}")
            for size in self.sizes:
                self.browser.set_window_size(size, BROWER_HEIGHT)
                self.browser.execute_script("window.scrollTo(0, 0)")
                time.sleep(1)
                scroll_size = self.browser.execute_script("return document.body.scrollHeight") 
                total_sections = ceil(scroll_size / BROWER_HEIGHT )
                for section in range(total_sections + 1):
                    self.browser.execute_script(f"window.scrollTo(0, {section * BROWER_HEIGHT})")
                    time.sleep(1)
                    self.browser.save_screenshot(f"screenshots/{title}/{size}x{section}.png")
        except:
            pass

    def start(self):
        for url in self.urls:
            url = self.check_url(url)
            self.screenshot(url)

tester = ResponsiveTester(["naver.com", "https://nomadcoders.co","www.google.com"])

tester.start()








