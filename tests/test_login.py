import unittest
import traceback
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from config.setting import AGENT_EMAIL, AGENT_PASSWORD, SIGNIN_URL

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.test_start_time = time.time()

    def tearDown(self):
        self.driver.quit()
        
    def test_001(self):
        '''
        Test login with valid credentials
        '''
        try:
            driver = self.driver
            login_page = LoginPage(driver)
            login_page.goto_login_page(SIGNIN_URL)
            login_page.select_tenant()
            login_page.fill_email(AGENT_EMAIL)
            login_page.fill_password(AGENT_PASSWORD)
            login_page.click_sign_in()
            login_page.is_login_successful(), "Login failed"
        except Exception:
            raise AssertionError(f"{self._testMethodName} failed due to an exception")

    def test_002(self):
        '''
            Test login with wrong password
        '''
        try:
            driver = self.driver
            login_page = LoginPage(driver)
            login_page.goto_login_page(SIGNIN_URL)
            login_page.select_tenant()
            login_page.fill_email(AGENT_EMAIL)
            login_page.fill_password("wrongpassword")
            login_page.click_sign_in()
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'incorrect')]"))
            )
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")

    def test_003(self):
        '''
        Test login with email not existed
        '''
        try:
            driver = self.driver
            login_page = LoginPage(driver)
            login_page.goto_login_page(SIGNIN_URL)
            login_page.select_tenant()
            login_page.fill_email("fakeemail@gmail.com")
            login_page.fill_password("anyPassword")
            login_page.click_sign_in()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'account')]"))
            )
        except Exception:
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
            
    def test_004(self):
        '''
        Test login with null email and password
        '''
        try:
            driver = self.driver
            login_page = LoginPage(driver)
            login_page.goto_login_page(SIGNIN_URL)
            login_page.select_tenant()
            login_page.fill_email("")
            login_page.fill_password("")
            login_page.click_sign_in()
            error_msg = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email-helper-text"))
            )
            assert "cannot be blank" in error_msg.text.lower()
        except Exception:
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
    
if __name__ == "__main__":
    unittest.main()