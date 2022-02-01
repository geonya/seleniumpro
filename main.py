from xml import dom
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class GoogleKeywordScreenShooter:
    def __init__(self, keyword, screenshots_dir, req_page_num):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
        self.req_page_num = req_page_num

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        
        def take_screenshot(current_page_num):
            print(f"Taking screenshot page No.{current_page_num}")
            search_results = self.browser.find_elements_by_class_name("g")
            try:
                shitty_element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ULSxyf")))
                self.browser.execute_script("""
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty)
                """,shitty_element)
            except Exception:
                pass
            for index, search_result in enumerate(search_results):
                search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}-p-{current_page_num}-{index}.png")
        def searcing_til_req_page_num():
            next_page_btn = self.browser.find_element_by_id("pnnext")
            current_page_num = int(self.browser.find_element_by_class_name("YyVfkd").text)
            if current_page_num < self.req_page_num:
                take_screenshot(current_page_num)
                if next_page_btn:
                    next_page_btn.click()
                    searcing_til_req_page_num()
            else:
                take_screenshot(current_page_num)

        searcing_til_req_page_num()
        
    
    def finish(self):
        self.browser.quit()
    
python_competitors = GoogleKeywordScreenShooter("python book", "screenshots", 12)
python_competitors.start()
python_competitors.finish()


