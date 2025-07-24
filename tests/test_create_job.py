import unittest
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.jobs_page import JobPage
from config.setting import AGENT_EMAIL, AGENT_PASSWORD, CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD, SIGNIN_URL, JOBS_URL
from utils.data.gen_data_job import GenerateJobData

class CreateJobTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()
    
    def signIn(self, email, password):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.goto_login_page(SIGNIN_URL)
        login_page.select_tenant()
        login_page.fill_email(email)
        login_page.fill_password(password)
        assert login_page.click_sign_in(), "Login failed"
        
    def test_001(self):
        '''
        Test creating a new job with valid data
        '''
        try:
            driver = self.driver
            self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            data = GenerateJobData.generate_job_data()

            job_page = JobPage(driver, client_type='agent')
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            
            job_page.fill_job_type(data['jobType'])
            job_page.fill_reference_number(data['cusRefNo'])
            job_page.fill_vessel(data['vessel'])
            job_page.fill_voyage(data['voyage'])
            job_page.fill_unloco(data['unloco'])
            job_page.fill_eta(data['eta'])
            job_page.fill_etd(data['etd'])
            
            if(data['jobType'] == 'IMPORT'):
                job_page.fill_imp_available_date(data['datetime_start'])
                job_page.fill_first_free_date(data['datetime_start'])
                job_page.fill_imp_storage_start_date(data['datetime_start'])
            elif(data['jobType'] == 'EXPORT'):
                job_page.fill_exp_recv_date(data['datetime_start'])
                job_page.cargo_cutoff_date(data['datetime_end'])
            elif(data['jobType'] == 'MISC'):
                job_page.fill_imp_available_date(data['datetime_start'])
                job_page.fill_imp_storage_start_date(data['datetime_start'])
                
            job_page.fill_reefer_cutoff_date(data['datetime_end'])
            job_page.fill_empty_recv_date(data['datetime_start'])
            job_page.fill_empty_cutoff_date(data['datetime_end'])
            job_page.fill_harz_recv_date(data['datetime_start'])
            job_page.fill_harz_cutoff_date(data['datetime_end'])
            
            # Fill other fields as needed
            # job_page.fill_agent('Agent A')
            job_page.fill_consignee()
            job_page.fill_account_receivable()
            job_page.fill_warehouse()

            # Submit the form
            job_page.submit_form()
            assert job_page.is_success_message_visible(), "Job creation failed"

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")

if __name__ == "__main__":
    unittest.main()