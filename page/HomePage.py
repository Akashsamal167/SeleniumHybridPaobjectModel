from selenium.webdriver.common.by import By

from page.LoginPage import LoginPage
from page.SearchPage import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name= "search"
    search_button_xpath= "//i[@class='fa fa-search']"
    my_account_drop_manu_Linktext= "My Account"
    login_option_link_text= "Login"
    register_option_linktext = "Register"

    def enter_productinto_searchbox_field(self,product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_onsearch_icon(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_aacount_manue(self):
        self.driver.find_element(By.LINK_TEXT, self.my_account_drop_manu_Linktext).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_linktext).click()












