from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
from typing import List
import time

class NBAScraper:
	def __init__(self):
		pass
	
	@staticmethod
	def leading_scorers() -> List:
		pass

if __name__ == "__main__":
	service = Service(executable_path="chromedriver.exe")
	
	options = Options()
	# options.add_argument("--headless")

	driver = webdriver.Chrome(service=service, options=options)
	
	driver.get("https://www.nba.com/stats")


	WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.XPATH, "//div[starts-with(@class, 'LeaderBoardWithButtons_lbwbCardWrapper')]"))
	)

	source = driver.page_source
	driver.quit()

	page = soup(source, "html.parser")
	print(page.prettify())
