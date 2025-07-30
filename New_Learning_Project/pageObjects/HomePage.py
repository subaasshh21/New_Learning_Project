

class RegistrationElements():
    txt_Name_xpath="//input[@id='name']"
    txt_Email_xpath="//input[@id='email']"
    txt_Phone_xpath="//input[@id='phone']"
    txt_Address_xpath="//textarea[@id='textarea']"
    def __init__(self, driver):
        self.driver=driver
    def