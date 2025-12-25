import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from page.HomePage import HomePage
from page.RegisterPage import RegisterPage




@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_valid_reg(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        Home_page.select_register_option()

        register_page=RegisterPage(self.driver)
        register_page.enter_firstname("Akash")
        register_page.enter_lastname("Samal")
        register_page.enter_email("samalakash103@gmail.com")
        register_page.enter_telephone("7411474512")
        register_page.enter_password("Ak@123")
        register_page.enter_conf_password("Ak@123")
        register_page.select_radio_button()
        register_page.select_agree_check_box()
        register_page.click_continue_button()

        # Account_SuccessPage=AccountSuccesPage(self.driver)
        # expect_title="Congratulations! Your new account has been successfully created!"
        # assert Account_SuccessPage.retrive_account_creation_message().text.__eq__(expect_title)


    def test_existvalid_reg(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        Home_page.select_register_option()

        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("Akash")
        register_page.enter_lastname("Samal")
        register_page.enter_email("samalakash565@gmail.com")
        register_page.enter_telephone("7411474512")
        register_page.enter_password("Ak@123")
        register_page.enter_conf_password("Ak@123")
        register_page.select_radio_button()
        register_page.select_agree_check_box()
        register_page.click_continue_button()
        exp_title="Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email().__eq__(exp_title)
        # contains_warningmsg = "Warning: E-Mail Address is already registered!"
        # assert self.driver.find_element(By.XPATH, "//*[text()='Warning: You must agree to the Privacy Policy!']").text.__contains__(
        #     contains_warningmsg)

    def test_blank_fields(self):
        Home_page = HomePage(self.driver)
        Home_page.click_on_my_aacount_manue()
        Home_page.select_register_option()

        register_page = RegisterPage(self.driver)
        register_page.enter_firstname("")
        register_page.enter_lastname("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_conf_password("")
        register_page.select_radio_button()
        register_page.select_agree_check_box()
        register_page.click_continue_button()
    #     privacy_warningmsg = "Warning: You must agree to the Privacy Policy!"
    #     assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
    #         privacy_warningmsg)

