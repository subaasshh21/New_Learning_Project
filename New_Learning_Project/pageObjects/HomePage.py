from selenium.webdriver.common.by import By


class RegistrationElements():
    txt_Name_xpath="//input[@id='name']"
    txt_Email_xpath="//input[@id='email']"
    txt_Phone_xpath="//input[@id='phone']"
    txt_Address_xpath="//textarea[@id='textarea']"
    radio_Male_id= (By.ID, "male")
    radio_Female_id = (By.ID, "female")
    def __init__(self, driver):
        self.driver=driver
    def entername (self,fullname):
        self.driver.find_element(By.XPATH,self.txt_Name_xpath).send_keys(fullname)
    def enteremail (self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)
    def enterphone (self,phone):
        self.driver.find_element(By.XPATH,self.txt_Phone_xpath).send_keys(phone)
    def enteraddress(self,address):
        self.driver.find_element(By.XPATH,self.txt_Address_xpath).send_keys(address)
    def select_gender_male(self):
        self.driver.find_element(*self.radio_Male_id).click()
    def select_gender_female(self):
        self.driver.find_element(*self.radio_Female_id).click()
    def select_days(self, selected_days):
        for day in selected_days:
            self.driver.find_element(By.ID,day).click()
    def select_country(self,country_name):
        country_list_xpath =self.driver.find_elements(By.XPATH, "//select[@id='country']/option")
        for country in country_list_xpath:
            if country.text==country_name:
                country.click()





