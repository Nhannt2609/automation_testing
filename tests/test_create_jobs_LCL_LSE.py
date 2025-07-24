# import unittest
# import time
# import random
# from datetime import datetime, timedelta
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from faker import Faker

# fake = Faker()
# from dotenv import load_dotenv
# import os
# load_dotenv()

# class CreateJobLclLseTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("xxx")
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.ID, "email"))
#         )
#         self.login()

#     def login(self):
#         driver = self.driver
#         driver.find_element(By.ID, "email").send_keys("xxx")
#         driver.find_element(By.ID, "password").send_keys("xxx")
#         driver.find_element(By.XPATH, "//button[.//span[text()='Sign In']]").click()
#         WebDriverWait(driver, 10).until(
#             EC.url_contains("/admin/dashboard")
#         )
    
#     def select_random_option(self, input_id):
#         driver = self.driver
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, input_id))).click()
#         options = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
#         )
#         filtered = [opt for opt in options if opt.text.strip() != "Add New"]
#         if not filtered:
#             raise Exception(f"No valid options found for dropdown #{input_id}")
#         random.choice(filtered).click()


#     def test_create_transport_job(self):
#         driver = self.driver

#         # Truy cập trang tạo mới
#         driver.get("xxx")
#         wait = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//span[text()='Transport Job']"))
#         )
#         driver.find_element(By.XPATH, "//span[text()='General Freight']").click()
#         wait = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//span[text()='ACTIVE']"))
#         )
#         rdNum = random.randint(1,6)
        
#         # Chọn Shipment Type
#         # shipment_type = random.choice(["LCL", "LSE"])
#         shipment_type = "LSE"  # Giả sử chỉ test với LCL
#         driver.find_element(By.XPATH, f"//span[text()='{shipment_type}']").click()
        
#         # Click vào nút "Create New Job"
#         driver.find_element(By.XPATH, "//span[text()='New']").click()
        
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//span[text()='Detail']"))
#         )

#         # Chọn Job Type: IMPORT hoặc EXPORT ngẫu nhiên
#         # job_type = random.choice(["IMPORT", "EXPORT"])
#         job_type = "IMPORT"  # Giả sử chỉ test với IMPORT
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "jobType"))).click()
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{job_type}']"))).click()

#         # Sinh fake data
#         cusRefNo = 'AUSYD'
#         vessel = random.choice(['EVER GIVEN', 'EVER ULYSSES', 'UTOPIA OF THE SEAS'])
#         voyage = 'V' + str(random.randint(1000, 9999))
#         flightNo = 'FL' + str(random.randint(1000, 9999))
#         airlineCode = 'AU'
#         unloco = str(random.randint(100000, 999999))
#         eta, etd = [
#             (t := datetime(2025, 1, 1) + timedelta(seconds=random.randint(0, int((datetime.now() - datetime(2025, 1, 1)).total_seconds())))),
#             t.strftime("%d-%m-%Y %H:%M"),
#             (t + timedelta(days=1)).strftime("%d-%m-%Y %H:%M")
#         ][1:]
#         date_start = datetime.now().strftime("%d-%m-%Y %H:%M")
#         datetime_end = '31-12-2025 23:59'
#         mblNo = fake.bothify(text='??-########')
#         hblNo = fake.bothify(text='??-########')
        
#         # shipment_type = "LCL"
#         job_type = "IMPORT"
        
#         if job_type == "IMPORT":
#             driver.find_element(By.ID, "referenceNumber").send_keys(cusRefNo)
#             if shipment_type == 'LCL':
#                 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "vessel"))).click()
#                 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{vessel}']"))).click()
#                 driver.find_element(By.ID, "voyage").send_keys(voyage)
#             else:
#                 driver.find_element(By.ID, "flightNumber").send_keys(flightNo)
#                 driver.find_element(By.ID, "airlineCode").send_keys(airlineCode)
                
#             # Nhập thông tin UNLOCO
#             driver.find_element(By.ID, "unlocoBoardOfLoading").send_keys(unloco)
#             driver.find_element(By.ID, "unlocoBoardOfDischarge").send_keys(unloco)
                
#             # Nhâp thông tin ETA và ETD
#             driver.find_element(By.ID, "eta").send_keys(eta)
#             driver.find_element(By.ID, "etd").send_keys(etd)
                
#             # Nhập các fields khác
#             driver.find_element(By.ID, "avail").send_keys(date_start)
#             driver.find_element(By.ID, "freeDate").send_keys(date_start)
#             driver.find_element(By.ID, "stor").send_keys(date_start)
#             driver.find_element(By.ID, "storLastFreeDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "rcDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "ercDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "ecDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "hrcDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "hcDate").send_keys(datetime_end)
#             driver.find_element(By.ID, "mblNo").send_keys(mblNo)
#             driver.find_element(By.ID, "hblNo").send_keys(hblNo)
            
#         # Chọn Agent ngẫu nhiên (field không bắt buộc)
#         if rdNum % 2 == 0:
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "agent"))).click()
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
#             )
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{random.choice(['KINTRASYD', 'LAUCOMPER', 'ILUTRASYD'])}']"))).click()
#             # Chọn Consignee dựa theo Agent
#             self.select_random_option("consignee")
#             # Chọn accountReceivable
#             self.select_random_option("accountReceivable")
#             # Chọn deliWarehouse
#             self.select_random_option("warehouse")
#         else:
#             # Chọn Consignee
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "consignee"))).click()
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
#             )
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{random.choice(['KINTRASYD', 'CLAGLO', 'UCLOG'])}']"))).click()
#             # Chọn accountReceivable
#             self.select_random_option("accountReceivable")
#             # Chọn deliWarehouse
#             self.select_random_option("warehouse")
        
#         driver.find_element(By.XPATH, "//button[.//span[text()='Save']]").click()
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'success') or contains(text(), 'success')]"))
#         )
                
#     def tearDown(self):
#         time.sleep(2)
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()