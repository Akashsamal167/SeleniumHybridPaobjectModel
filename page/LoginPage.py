from selenium.webdriver.common.by import By

from page.AccountPage import AccountPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_addrs_id="input-email"
    passwords_id="input-password"
    login_button_xpath="//input[@type='submit']"
    #warning_message=


    def enter_email_addrss(self,email_address_text):
        self.driver.find_element(By.ID, self.email_addrs_id).click()
        self.driver.find_element(By.ID, self.email_addrs_id).clear()
        self.driver.find_element(By.ID, self.email_addrs_id).send_keys(email_address_text)

    def enter_passwords(self,password_text):
        self.driver.find_element(By.ID, self.passwords_id).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    #def warning_message(self):





