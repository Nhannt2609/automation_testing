import unittest
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.jobs_page import JobPage
from config.setting import AGENT_EMAIL, AGENT_PASSWORD, CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD, SIGNIN_URL, JOBS_URL
from utils.data.gen_data import GenerateJobData

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
        login_page.click_sign_in()
        assert login_page.is_login_successful(), "Login failed"
        
    def test_001(self):
        '''
        Check fields of the job creation form of IMPORT job type
        '''
        try:
            driver = self.driver
            data = GenerateJobData.generate_job_data()
            if data['clientType'] == 'agent':
                self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            else:
                self.signIn(CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD)

            job_page = JobPage(driver, client_type=data['clientType'])
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            
            job_page.fill_job_type('IMPORT')
            time.sleep(1)  # Wait for the job type to be set
            assert job_page.fill_imp_available_date(''), "Import available date field not found"
            assert job_page.fill_first_free_date(''), "First free date field not found"
            assert job_page.fill_imp_storage_start_date(''), "Import storage start date field not found"
            assert job_page.fill_reefer_cutoff_date(''), "Reefer cutoff date field not found"
            assert job_page.fill_empty_recv_date(''), "Empty receive date field not found"
            assert job_page.fill_empty_cutoff_date(''), "Empty cutoff date field not found"
            assert job_page.fill_harz_recv_date(''), "Harz receive date field not found"
            assert job_page.fill_harz_cutoff_date(''), "Harz cutoff date field not found"
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Consignee')]"))
            )
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
    
    def test_002(self):
        '''
        Check fields of the job creation form of EXPORT job type
        '''
        try:
            driver = self.driver
            data = GenerateJobData.generate_job_data()
            if data['clientType'] == 'agent':
                self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            else:
                self.signIn(CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD)

            job_page = JobPage(driver, client_type=data['clientType'])
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            
            job_page.fill_job_type('EXPORT')
            time.sleep(1)  # Wait for the job type to be set
            assert job_page.fill_exp_recv_date(''), "Export receive date field not found"
            assert job_page.fill_cargo_cutoff_date(''), "Cargo cutoff date field not found"
            assert job_page.fill_reefer_cutoff_date(''), "Reefer cutoff date field not found"
            assert job_page.fill_empty_recv_date(''), "Empty receive date field not found"
            assert job_page.fill_empty_cutoff_date(''), "Empty cutoff date field not found"
            assert job_page.fill_harz_recv_date(''), "Harz receive date field not found"
            assert job_page.fill_harz_cutoff_date(''), "Harz cutoff date field not found"
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Consignor')]"))
            )
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
        
    def test_003(self):
        '''
        Check fields of the job creation form of MISC job type
        '''
        try:
            driver = self.driver
            data = GenerateJobData.generate_job_data()
            if data['clientType'] == 'agent':
                self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            else:
                self.signIn(CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD)

            job_page = JobPage(driver, client_type=data['clientType'])
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            
            job_page.fill_job_type('MISC')
            time.sleep(1)  # Wait for the job type to be set
            assert job_page.fill_imp_available_date(''), "Import available date field not found"
            assert job_page.fill_imp_storage_start_date(''), "Import storage start date field not found"
            assert job_page.fill_reefer_cutoff_date(''), "Reefer cutoff date field not found"
            assert job_page.fill_empty_recv_date(''), "Empty receive date field not found"
            assert job_page.fill_empty_cutoff_date(''), "Empty cutoff date field not found"
            assert job_page.fill_harz_recv_date(''), "Harz receive date field not found"
            assert job_page.fill_harz_cutoff_date(''), "Harz cutoff date field not found"
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Consignee/Consignor')]"))
            )
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
    
    def test_004(self):
        '''
        Test creating a new job with valid data
        '''
        try:
            driver = self.driver
            data = GenerateJobData.generate_job_data()
            if data['clientType'] == 'agent':
                self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            else:
                self.signIn(CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD)

            job_page = JobPage(driver, client_type=data['clientType'])
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            
            print(f"Creating job with data: {data}")
            job_page.fill_job_type(data['jobType'])
            job_page.fill_vessel(data['vessel'])
            job_page.fill_voyage(data['voyage'])
            job_page.fill_unloco(data['unloco'])
            job_page.fill_eta(data['eta'])
            job_page.fill_etd(data['etd'])
            job_page.fill_reference_number(data['cusRefNo'])
            
            if(data['jobType'] == 'IMPORT'):
                job_page.fill_imp_available_date(data['datetime_start'])
                job_page.fill_first_free_date(data['datetime_start'])
                job_page.fill_imp_storage_start_date(data['datetime_start'])
            elif(data['jobType'] == 'EXPORT'):
                job_page.fill_exp_recv_date(data['datetime_start'])
                job_page.fill_cargo_cutoff_date(data['datetime_end'])
            elif(data['jobType'] == 'MISC'):
                job_page.fill_imp_available_date(data['datetime_start'])
                job_page.fill_imp_storage_start_date(data['datetime_start'])
                
            job_page.fill_reefer_cutoff_date(data['datetime_end'])
            job_page.fill_empty_recv_date(data['datetime_start'])
            job_page.fill_empty_cutoff_date(data['datetime_end'])
            job_page.fill_harz_recv_date(data['datetime_start'])
            job_page.fill_harz_cutoff_date(data['datetime_end'])
            
            # Fill related parties
            if data['clientType'] == 'agent':
                job_page.fill_consignee()
                job_page.fill_account_receivable()
                job_page.fill_warehouse()
            else:
                job_page.fill_account_receivable()
                job_page.fill_warehouse()

            # Submit the form
            job_page.submit_form()
            assert job_page.is_success_message_visible(), "Job creation failed"

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")

    def test_005(self):
        '''
        Test checking the required field
        '''
        try:
            driver = self.driver
            data = GenerateJobData.generate_job_data()
            if data['clientType'] == 'agent':
                self.signIn(AGENT_EMAIL, AGENT_PASSWORD)
            else:
                self.signIn(CONSIGNEE_EMAIL, CONSIGNEE_PASSWORD)

            job_page = JobPage(driver, client_type=data['clientType'])
            job_page.goto_jobs_page(JOBS_URL)
            job_page.click_create_new_job()
            print(f"Creating job with data: {data}")
            job_page.fill_job_type(data['jobType'])
            job_page.submit_form()
            
            job_types = ['IMPORT', 'EXPORT']
            
            for job_type in job_types: 
                job_page.fill_job_type(job_type)
                job_page.submit_form()
                if job_type == 'IMPORT':
                    assert 'required field' in job_page.get_vessel_error().lower(), "Vessel field of IMP job is required but was left empty."
                    assert 'cannot be blank' in job_page.get_voyage_error().lower(), "Voyage field of IMP job  is required but was left empty."
                    assert 'cannot be blank' in job_page.get_eta_error().lower(), "ETA field of IMP job is required but was left empty."
                elif job_type == 'EXPORT':
                    assert 'required field' in job_page.get_vessel_error().lower(), "Vessel field of EXP job is required but was left empty."
                    assert 'cannot be blank' in job_page.get_voyage_error().lower(), "Voyage field of EXP job is required but was left empty."
                    assert 'cannot be blank' in job_page.get_etd_error().lower(), "ETD field of EXP job is required but was left empty."
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise AssertionError(f"{self._testMethodName} failed due to an exception")
    
      
if __name__ == "__main__":
    unittest.main()