from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

class VnExpressUniCrawler:
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=self.options)
        self.url = "https://diemthi.vnexpress.net/tra-cuu-dai-hoc"

        self.uni_links = []

    def execute(self):
        # Get soup on initialize
        self.driver.get(self.url)
        self._crawl_main_page()
        

    def _crawl_main_page(self):
        loadmore_btn = self.driver.find_element(By.CLASS_NAME, "btn_loadmore")

        while loadmore_btn:
            try:
                ActionChains(self.driver).move_to_element(loadmore_btn).click(loadmore_btn).pause(3).perform()
            except Exception as e:
                #print(e)
                print("Load Finished.")

                self.main_content =  self.driver.find_element(By.CLASS_NAME, "main__content").get_attribute("innerHTML")
                self.soup = BeautifulSoup(self.main_content, "html.parser")
                
                self._get_uni_href_list()

                self.driver.quit()
                break

    def _get_uni_href_list(self):
        uni_list = self.soup.find('ul', {"class": "lookup__results"})

        a_elements = uni_list.find_all('a')

        for a in a_elements:
            self.uni_links.append(str("https://diemthi.vnexpress.net" + a['href']))

        # Remove any duplicate links
        self.uni_links = list(dict.fromkeys(self.uni_links))

        return self.uni_links
        
    def _crawl_uni_page(self, url):
        for link in self.uni_links:
            self.driver.get(link)
            self.uni_details = self.driver.find_element(By.CLASS_NAME, "main__content").get_attribute("innerHTML")
