import unittest
import traceback
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.result_writer import results, record_result

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.test_start_time = time.time()

    def tearDown(self):
        self.driver.quit()

    def test_001_login_success(self):
        try:
            driver = self.driver
            driver.get("https://demo.tech-demo.online/auth/sign-in")
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
            driver.find_element(By.ID, "email").send_keys("dummyops.syd@thandy.com.au")
            driver.find_element(By.ID, "password").send_keys("pro123")
            driver.find_element(By.XPATH, "//span[text()='Sign In']").click()
            WebDriverWait(driver, 5).until(EC.url_contains("dashboard"))
            self.assertIn("dashboard", driver.current_url)
            record_result("test_001_login_success", "SUCCESS", self.test_start_time)
        except Exception:
            record_result("test_001_login_success", "FAIL", self.test_start_time, traceback.format_exc())

    # def test_002_login_wrong_password(self):
    #     try:
    #         driver = self.driver
    #         driver.get("https://demo.tech-demo.online/auth/sign-in")
    #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    #         driver.find_element(By.ID, "email").send_keys("dummyops.syd@thandy.com.au")
    #         driver.find_element(By.ID, "password").send_keys("pro1234")
    #         driver.find_element(By.XPATH, "//span[text()='Sign In']").click()
    #         error_msg = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'email or password')]"))
    #         )
    #         self.assertIn("you entered is incorrect", error_msg.text.lower())
    #         record_result("test_002_login_wrong_password", "SUCCESS", self.test_start_time)
    #     except Exception:
    #         record_result("test_002_login_wrong_password", "FAIL", self.test_start_time, traceback.format_exc())

    # def test_003_login_null(self):
    #     try:
    #         driver = self.driver
    #         driver.get("https://demo.tech-demo.online/auth/sign-in")
    #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    #         driver.find_element(By.ID, "email").send_keys("")
    #         driver.find_element(By.ID, "password").send_keys("")
    #         driver.find_element(By.XPATH, "//span[text()='Sign In']").click()
    #         error_msg = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, "email-helper-text"))
    #         )
    #         self.assertIn("cannot be blank", error_msg.text.lower())
    #         record_result("test_003_login_null", "SUCCESS", self.test_start_time)
    #     except Exception:
    #         record_result("test_003_login_null", "FAIL", self.test_start_time, traceback.format_exc())