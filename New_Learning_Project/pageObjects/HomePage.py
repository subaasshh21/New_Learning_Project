import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationElements():
    txt_Name_xpath="//input[@id='name']"
    txt_Email_xpath="//input[@id='email']"
    txt_Phone_xpath="//input[@id='phone']"
    txt_Address_xpath="//textarea[@id='textarea']"
    radio_Male_id= (By.ID, "male")
    radio_Female_id = (By.ID, "female")
    date_input_xpath = "//input[@id='datepicker']"
    month_xpath = "//span[@class='ui-datepicker-month']"
    year_xpath = "//span[@class='ui-datepicker-year']"
    next_btn_xpath = "//a[@title='Next']"
    prev_btn_xpath = "//a[@title='Prev']"
    day_xpath_template = "//table[@class='ui-datepicker-calendar']"

    def __init__(self, driver):
        self.wait = WebDriverWait(driver,10)
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
    def select_colour(self,colour_name):
        select=Select(self.driver.find_element(By.ID,"colors"))
        select.select_by_visible_text(colour_name)
    def select_animal(self,animal_name):
        select=Select(self.driver.find_element(By.ID,"animals"))
        select.select_by_visible_text(animal_name)
    def select_date(self,date_str):
        target_date=datetime.datetime.strptime(date_str,"%m/%d/%Y")
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.date_input_xpath))).click()
        while True:
            displayed_month=self.driver.find_element(By.XPATH,self.month_xpath).text
            displayed_year=self.driver.find_element(By.XPATH,self.year_xpath).text
            current_date=datetime.datetime.strptime(f"{displayed_month}{displayed_year}","%B%Y")
            if current_date.year < target_date.year or \
                    (current_date.year==target_date.year and current_date.month < target_date.month):
                    self.driver.find_element(By.XPATH,self.next_btn_xpath).click()
            elif current_date.year > target_date.year or \
                    (current_date.year == target_date.year and current_date.month > target_date.month):
                self.driver.find_element(By.XPATH, self.prev_btn_xpath).click()
            else:
                break
        day_xpath = f"{self.day_xpath_template}//a[text()='{target_date.day}']"
        self.driver.find_element(By.XPATH, day_xpath).click()







