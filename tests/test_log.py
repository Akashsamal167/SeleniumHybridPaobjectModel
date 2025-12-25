import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from page.AccountPage import AccountPage
from page.HomePage import HomePage
from page.LoginPage import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLog:
    def test_valid_login(self):

        Home_page=HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        login_page=Home_page.select_login_option()

        Login_page=LoginPage(self.driver)
        Login_page.enter_email_addrss("akashsamal995@gmail.com")
        Login_page.enter_passwords("A@123")
        Account_page=Login_page.click_on_login_button()

        assert Account_page.edit_your_account_information_option_LinkText


        # assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    def test_invalid_emailid_login(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        login_page=Home_page.select_login_option()

        Login_page = LoginPage(self.driver)
        Login_page.enter_email_addrss("akashsamal1225@gmail.com")
        Login_page.enter_passwords("A@123")
        Login_page.click_on_login_button()


        # expe_title = "Warning: No match for E-Mail Address and/or Password."
        # assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text == expe_title

    def test_invalid_pwd(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        Home_page.select_login_option()

        Login_page = LoginPage(self.driver)
        Login_page.enter_email_addrss("akashsamal1225@gmail.com")
        Login_page.enter_passwords("frf55@123")
        Login_page.click_on_login_button()

        # self.driver.find_element(By.LINK_TEXT, "My Account").click()
        # self.driver.find_element(By.LINK_TEXT, "Login").click()
        # self.driver.find_element(By.ID, "input-email").send_keys("akashsama995@gmail.com")
        # self.driver.find_element(By.ID, "input-password").send_keys("A@1234")
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # expe_title = "Warning: No match for E-Mail Address and/or Password."
        # assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text == expe_title

    def test_without_login(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        Home_page.select_login_option()

        Login_page = LoginPage(self.driver)
        Login_page.enter_email_addrss("")
        Login_page.enter_passwords("")
        Login_page.click_on_login_button()


    def generate_email_with_time_stamp(setup_and_teardown):
        timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        return timestamp













