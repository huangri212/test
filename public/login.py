import time,sys
sys.path.append('../')
from public.testconfig import GetTestConfig

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from testconfig import GetTestConfig
class Login:
	
	@staticmethod
	def login(self):
		
		self.driver = webdriver.Chrome()
		url =  GetTestConfig.getUrl()
		account = GetTestConfig.getAccount()
		self.driver.get(url)
		time.sleep(3)
		self.driver.find_element_by_id("loginEmail").send_keys(account[0])
		self.driver.find_element_by_id("loginPassword").send_keys('password')
		self.driver.find_element_by_id("loginButton").click()
		time.sleep(3)



