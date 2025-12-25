# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from datetime import datetime
#
# @pytest.fixture()
# def setup_and_teardown():
#     global driver
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://tutorialsninja.com/demo/")
#     yield
#     driver.quit()
#
# def test_valid_login(setup_and_teardown):
#
#     driver.find_element(By.LINK_TEXT,"My Account").click()
#     driver.find_element(By.LINK_TEXT,"Login").click()
#     driver.find_element(By.ID,"input-email").send_keys("akashsamal995@gmail.com")
#     driver.find_element(By.ID,"input-password").send_keys("A@123")
#     driver.find_element(By.XPATH,"//input[@type='submit']").click()
#     assert driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
#
#
# def test_invalid_emailid_login(setup_and_teardown):
#
#     driver.find_element(By.LINK_TEXT, "My Account").click()
#     driver.find_element(By.LINK_TEXT, "Login").click()
#     driver.find_element(By.ID, "input-email").send_keys("akashsama@gmail.com")
#     driver.find_element(By.ID, "input-password").send_keys("A@123")
#     driver.find_element(By.XPATH, "//input[@type='submit']").click()
#     expe_title = "Warning: No match for E-Mail Address and/or Password."
#     #assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text == expe_title
#
# def test_ivalid_pwd(setup_and_teardown):
#
#     driver.find_element(By.LINK_TEXT, "My Account").click()
#     driver.find_element(By.LINK_TEXT, "Login").click()
#     driver.find_element(By.ID, "input-email").send_keys("akashsama995@gmail.com")
#     driver.find_element(By.ID, "input-password").send_keys("A@1234")
#     driver.find_element(By.XPATH, "//input[@type='submit']").click()
#     expe_title = "Warning: No match for E-Mail Address and/or Password."
#     #assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text == expe_title
#
#
# def generate_email_with_time_stamp(setup_and_teardown):
#     timestamp= datetime.now().strftime("%m/%d/%Y %H:%M:%S")
#     return timestamp
