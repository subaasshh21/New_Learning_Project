from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.HomePage import RegistrationElements



class Test_001_RegElements:
    baseURL="https://testautomationpractice.blogspot.com/2018/09/automation-form.html"
    def test_Registration_ele(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.GUIregistration=RegistrationElements(self.driver)
        self.GUIregistration.entername("Jhon")
        self.GUIregistration.enteremail("abc@gmail.com")
        self.GUIregistration.enterphone("1234567890")




