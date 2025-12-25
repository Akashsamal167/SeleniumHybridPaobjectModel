# from selenium.webdriver.common.by import By
#
#
# class AccountSuccesPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     account_creation_message_xpath= "//p[text()=('Congratulations! Your new account has been successfully created!')]"
#
#     def retrive_account_creation_message(self):
#         return self.driver.find_element(By.XPATH, self.account_creation_message_xpath).text