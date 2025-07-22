import unittest
import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

clientType = random.choice(['Agent', 'Consignee'])

class CreateJobTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://13.236.99.51:3031/auth/signin")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        self.login()

    def login(self):
        driver = self.driver
        self.select_random_option("tenant")
        if clientType == 'Agent':
            driver.find_element(By.ID, "email").send_keys("lauriel@gmail.com")
            driver.find_element(By.ID, "password").send_keys("pro123")
        else:
            driver.find_element(By.ID, "email").send_keys("phong2khang@yopmail.com")
            driver.find_element(By.ID, "password").send_keys("pro123")
        driver.find_element(By.XPATH, "//button[.//span[text()='Sign In']]").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/admin/dashboard")
        )
    
    def select_random_option(self, input_id):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, input_id))).click()
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
        )
        filtered = [opt for opt in options if opt.text.strip() != "Add New"]
        if not filtered:
            raise Exception(f"No valid options found for dropdown #{input_id}")
        random.choice(filtered).click()


    def test_create_transport_job(self):
        driver = self.driver

        # Truy cập trang tạo mới
        driver.get("http://13.236.99.51:3031/admin/transport-jobs")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Transport Job']"))
        )
        
        # Click vào nút "Create New Job"
        driver.find_element(By.XPATH, "//span[text()='New']").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Detail']"))
        )

        # Chọn Job Type: IMPORT hoặc EXPORT hoặc MISC
        job_type = random.choice(['IMPORT', 'EXPORT', 'MISC'])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "jobType"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{job_type}']"))).click()

        # Sinh fake data
        cusRefNo = 'AUSYD'
        vessel = random.choice(['EVER GIVEN', 'EVER ULYSSES', 'UTOPIA OF THE SEAS', 'APL MEXICO CITY', 'APL OREGON'])
        voyage = 'V' + str(random.randint(1000, 9999))
        unloco = str(random.randint(100000, 999999))
        eta, etd = [
            (t := datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, int((datetime.now() - datetime(2025, 1, 1)).total_seconds())))),
            t.strftime("%d-%m-%Y %H:%M"),
            (t + timedelta(days=1)).strftime("%d-%m-%Y %H:%M")
        ][1:]
        dateStart = datetime.now().strftime("%d-%m-%Y %H:%M")
        dateEnd = '31-12-2025 23:59'
        
        # Nhập thông tin chung giữa hai Job Type
        # Nhập thông tin về Customer và Vessel
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "vessel"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{vessel}']"))).click()
        driver.find_element(By.ID, "voyage").send_keys(voyage)
        driver.find_element(By.ID, "referenceNumber").send_keys(cusRefNo)
                
        # Nhập thông tin UNLOCO
        driver.find_element(By.ID, "unlocoBoardOfLoading").send_keys(unloco)
        driver.find_element(By.ID, "unlocoBoardOfDischarge").send_keys(unloco)
                
        # Nhâp thông tin ETA và ETD
        driver.find_element(By.ID, "eta").send_keys(eta)
        driver.find_element(By.ID, "etd").send_keys(etd)
        
        if job_type == 'IMPORT':
            driver.find_element(By.ID, "avail").send_keys(dateStart)
            driver.find_element(By.ID, "freeDate").send_keys(dateStart)
            driver.find_element(By.ID, "stor").send_keys(dateStart)
        elif job_type == 'EXPORT':
            driver.find_element(By.ID, "expRecvDate").send_keys(dateStart)
            driver.find_element(By.ID, "cutOffDate").send_keys(dateEnd)
        elif job_type == 'MISC':
            driver.find_element(By.ID, "avail").send_keys(dateStart)
            driver.find_element(By.ID, "stor").send_keys(dateStart)
        driver.find_element(By.ID, "rcDate").send_keys(dateEnd)
        driver.find_element(By.ID, "ercDate").send_keys(dateEnd)
        driver.find_element(By.ID, "ecDate").send_keys(dateEnd)
        driver.find_element(By.ID, "hrcDate").send_keys(dateEnd)
        driver.find_element(By.ID, "hcDate").send_keys(dateEnd)
        
        if clientType == 'Agent':
            # Chọn consignee
            self.select_random_option("consignee")
            # Chọn accountReceivable
            self.select_random_option("accountReceivable")
            # Chọn deliWarehouse
            self.select_random_option("warehouse")
        else:
            # Chọn accountReceivable
            self.select_random_option("accountReceivable")
            # Chọn deliWarehouse
            self.select_random_option("warehouse")
    
        # Chọn SAVE
        driver.find_element(By.XPATH, "//button[.//span[text()='Save']]").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'success')]"))
        )
                
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()