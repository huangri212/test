from selenium import webdriver
import time,unittest,random,json,ConfigParser,HTMLTestRunner,sys
sys.path.append('../')
sys.path.append('../../')
from public.login import Login
from public.testconfig import GetTestConfig
from random import choice


class Show_processmap(unittest.TestCase):
    url =  GetTestConfig.getUrl()
    account = GetTestConfig.getAccount()
    companyName = GetTestConfig.getCompany()
    processName = GetTestConfig.getProcess()
    processList = json.loads(processName)
    random_process= random.choice(processList)

    @classmethod
    def  setUp(self):
        public_login = Login.login(self)
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_show_processmap(self):

        self.driver.find_element_by_xpath("//div[@id='Process Discovery']/p[@class='icon icon']").click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath("//div[@title='" + self.companyName + "']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='customer-caption'][div[@title='" + self.companyName + "']]/div[@class='process-section']/div[@class='process-dropdown-box']/div/div/div[@class='selected']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='process-dropdown dropdown open']//following-sibling::div[1]/ul/li/a[text()='" + self.random_process +"']").click()
        self.driver.find_element_by_xpath("//div[@title='" + self.companyName +"']/following-sibling::div[1]/div/span/button").click()
        time.sleep(5)
        elem_events = self.driver.find_elements_by_xpath("//div[@class='title']")
        try:
            print ("fail to load processmap")
            self.assertNotEqual(len(elem_events),0)
        except Exception as e: 
            self.verificationErrors.append(str(e))
            raise e
    def  tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
