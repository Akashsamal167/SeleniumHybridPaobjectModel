from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver):
        self.driver=driver

        self.first_name_field_id = "input-firstname"
        self.last_name_field_id= "input-lastname"
        self.email_filed_xpath="//input[@name='email']"
        self.telephone_field_xpath="//input[@name='telephone']"
        self.password_field_xpath="//input[@name='password']"
        self.conf_password_field_xpath="//input[@name='confirm']"
        self.radio_field_xpath="//input[@value='0']"
        self.agree_field_name="agree"
        self.continue_button_xpath="//input[@value='Continue']"
        self.duplicate_email="//div[@id='account-register']/div[1]"


    def enter_firstname(self,firstnametext):
        self.driver.find_element(By.ID, self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID,self.first_name_field_id).send_keys(firstnametext)

    def enter_lastname(self,lastnametext):
        self.driver.find_element(By.ID,self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(lastnametext)

    def enter_email(self,emailaddrs):
        self.driver.find_element(By.XPATH,self.email_filed_xpath).click()
        self.driver.find_element(By.XPATH, self.email_filed_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_filed_xpath).send_keys(emailaddrs)

    def enter_telephone(self,telephone):
        self.driver.find_element(By.XPATH,self.telephone_field_xpath).click()
        self.driver.find_element(By.XPATH, self.telephone_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.telephone_field_xpath).send_keys(telephone)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def enter_conf_password(self,conpassword):
        self.driver.find_element(By.XPATH,self.conf_password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.conf_password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.conf_password_field_xpath).send_keys(conpassword)

    def select_radio_button(self):
        self.driver.find_element(By.XPATH,self.radio_field_xpath).click()

    def select_agree_check_box(self):
        self.driver.find_element(By.NAME,self.agree_field_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def retrieve_duplicate_email(self):
        return self.driver.find_element(By.XPATH,self.duplicate_email).text



