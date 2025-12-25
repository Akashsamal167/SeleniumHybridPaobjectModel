from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    valid_hp_products_linktext = "HP LP3065"
    no_product_message_xpath= "//p[text()='There is no product that matches the search criteria.']"

    def display_statusof_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_products_linktext).is_displayed()

    def retrive_no_product_msg(self):
        return self.driver.find_element(By.XPATH, self.no_product_message_xpath).text