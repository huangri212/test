from selenium import webdriver
import time,unittest,sys,json,HTMLTestRunner,ConfigParser,random
from selenium.common.exceptions import NoSuchElementException
# sys.path.insert(0,"C:/Users/huanri/Documents/apa_auto/test_case")
# print sys.path
# from test_case import testconfig
sys.path.append('../')
from public.testconfig import GetTestConfig
from random import choice
# from colorama import init, Fore, Back, Style
# from apa_login import Apa_login


class Apa_login(unittest.TestCase):
    # getconf = GetTestConfig()
    url =  GetTestConfig.getUrl()
    account = GetTestConfig.getAccount()
    companyName = GetTestConfig.getCompany()
    processName = GetTestConfig.getProcess()
    
    processList = json.loads(processName)
    random_process= random.choice(processList)
    @classmethod
    def  setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(self.url)
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True

    # def test_navigator_apa(self):
        
    #     title = self.driver.find_element_by_tag_name('h2')
    #     #ckeck load login page
    #     # try:
    #     self.assertEqual(title.text,'Logi to APA')
    #     # except Exception as e: self.verificationErrors.append(str(e))
    #     # finally
    #     #     self.driver.quit
    def test_login(self):
        self.driver.find_element_by_id("loginEmail").send_keys(self.account[0])
        self.driver.find_element_by_id("loginPassword").send_keys(self.account[1])
        self.driver.find_element_by_id("loginButton").click()
        time.sleep(3)
        greeting = self.driver.find_element_by_xpath("//span[@class='greeting-user']/small")

        # try:
        #     self.assertEqual(greeting.text,"Good day,")
        # except Exception as e: self.verificationErrors.append(str(e))
        try:
            print ('can not find the greeting "Good Day"')
            self.assertEqual(greeting.text,'Good day,')

            # assert 'Good ,' in greeting.text
        except AssertionError, e:
            self.verificationErrors.append(str(e))
            raise e
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

