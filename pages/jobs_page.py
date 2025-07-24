import random
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobPage:
    def __init__(self, driver, client_type):
        self.driver = driver
        self.client_type = client_type

    def goto_jobs_page(self, jobs_url):
        self.driver.get(jobs_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Transport Job']"))
        )

    def click_create_new_job(self):
        self.driver.find_element(By.XPATH, "//span[text()='New']").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Detail']"))
        )

    def select_random_option(self, input_id):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, input_id))).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
        )
        filtered = [opt for opt in options if opt.text.strip() != "Add New"]
        if not filtered:
            raise Exception(f"No valid options found for #{input_id}")
        random.choice(filtered).click()
        
    def fill_job_type(self, job_type='IMPORT'):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "jobType"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{job_type}']"))
        ).click()
        
    def fill_vessel(self, vessel):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "vessel"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{vessel}']"))
        ).click()
        
    def fill_voyage(self, voyage):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "voyage"))).send_keys(voyage)
        
    def fill_reference_number(self, reference_number):
        self.driver.find_element(By.ID, "referenceNumber").send_keys(reference_number)
    
    def fill_unloco(self, unloco):
        self.driver.find_element(By.ID, "unlocoBoardOfLoading").send_keys(unloco)
        self.driver.find_element(By.ID, "unlocoBoardOfDischarge").send_keys(unloco)
    
    def fill_eta_etd(self, eta):
        self.driver.find_element(By.ID, "eta").send_keys(eta)
    
    def fill_etd(self, etd):
        self.driver.find_element(By.ID, "etd").send_keys(etd)
        
    def fill_imp_available_date(self, imp_available_date):
        self.driver.find_element(By.ID, "avail").send_keys(imp_available_date)

    def fill_first_free_date(self, first_free_date):
        self.driver.find_element(By.ID, "freeDate").send_keys(first_free_date)
    
    def fill_imp_storage_start_date(self, imp_storage_start_date):
        self.driver.find_element(By.ID, "stor").send_keys(imp_storage_start_date)
        
    def fill_exp_recv_date(self, exp_recv_date):
        self.driver.find_element(By.ID, "expRecvDate").send_keys(exp_recv_date)
    
    def fill_cargo_cutoff_date(self, cut_off_date):
        self.driver.find_element(By.ID, "cutOffDate").send_keys(cut_off_date)
            
    def fill_reefer_cutoff_date(self, reefer_cutoff_date):
        self.driver.find_element(By.ID, "rcDate").send_keys(reefer_cutoff_date)
    
    def fill_empty_recv_date(self, empty_recv_date):
        self.driver.find_element(By.ID, "ercDate").send_keys(empty_recv_date)
    
    def fill_empty_cutoff_date(self, empty_cutoff_date):
        self.driver.find_element(By.ID, "ecDate").send_keys(empty_cutoff_date)
    
    def fill_harz_recv_date(self, harz_recv_date):
        self.driver.find_element(By.ID, "hrcDate").send_keys(harz_recv_date)
        
    def fill_harz_cutoff_date(self, harz_cutoff_date):
        self.driver.find_element(By.ID, "hcDate").send_keys(harz_cutoff_date)
        
    def fill_agent(self, agent_code=None):
        if agent_code:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "agent"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{agent_code}']"))
            ).click()
        self.select_random_option("agent")
        
    def fill_consignee(self, consignee_code=None):
        if consignee_code:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "consignee"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{consignee_code}']"))
            ).click()
        self.select_random_option("consignee")
    
    def fill_account_receivable(self, account_code=None):
        if account_code:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "accountReceivable"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{account_code}']"))
            ).click()
        self.select_random_option("accountReceivable")
    
    def fill_warehouse(self, warehouse_code=None):
        if warehouse_code:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "warehouse"))).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{warehouse_code}']"))
            ).click()
        self.select_random_option("warehouse")

    def submit_form(self):
        self.driver.find_element(By.XPATH, "//button[.//span[text()='Save']]").click()

    def is_success_message_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'success')]"))
            )
            return True
        except:
            return False