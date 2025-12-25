
import pytest
from selenium.webdriver.common.by import By

from page.HomePage import HomePage
from page.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_valid_product(self):

        home_page = HomePage(self.driver)
        home_page.enter_productinto_searchbox_field("HP")
        search_page=home_page.click_onsearch_icon()

        search_page=SearchPage(self.driver)
        assert search_page.display_statusof_valid_product()



    def test_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page=home_page.enter_productinto_searchbox_field("Honda")
        home_page.click_onsearch_icon()

        # self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Honda")
        # self.driver.find_element(By.XPATH, "//i[@class='fa fa-search']").click()

        # expect_text = "There is no product that matches the search criteria."
        # search_page=SearchPage(self.driver)
        # assert search_page.retrive_no_product_msg().text.__eq__(expect_text)

    def test_without_products(self):
        home_page = HomePage(self.driver)
        search_page=home_page.enter_productinto_searchbox_field("Honda")
        home_page.click_onsearch_icon()

        # expect_text = "There is no product that matches the search criteria."
        # search_page = SearchPage(self.driver)
        # assert search_page.retrive_no_product_msg().text == expect_text


















