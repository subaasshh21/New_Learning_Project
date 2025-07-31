from selenium.webdriver.common.by import By


class RegistrationElements():
    txt_Name_xpath="//input[@id='name']"
    txt_Email_xpath="//input[@id='email']"
    txt_Phone_xpath="//input[@id='phone']"
    txt_Address_xpath="//textarea[@id='textarea']"
    radio_Male_id= (By.ID, "male")
    radio_Female_id = (By.ID, "female")
    check_days_id=(By.ID, "sunday","monday","tuesday","wednesday","thursday","friday","saturday")
    def __init__(self, driver):
        self.driver=driver
    def entername (self,fullname):
        self.driver.find_element(By.XPATH,self.txt_Name_xpath).send_keys(fullname)
    def enteremail (self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)
    def enterphone (self,phone):
        self.driver.find_element(By.XPATH,self.txt_Phone_xpath).send_keys(phone)
    def enteraddress(self,address):
        self.driver.findelement(By.XPATH,self.txt_Address_xpath).send_keys(address)
    def is_gender_selected(self,gender:str)->bool:
        locator=self.radio_Male_id if gender.lower()=="Male" else self.radio_Female_id
        return self.driver.find_element(locator).is_selected()





