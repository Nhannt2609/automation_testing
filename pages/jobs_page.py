import random
from datetime import datetime, timedelta
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class JobPage:
    
    FIELD_ID_MAP = {
        "jobType": "jobType",
        "vessel": "vessel",
        "voyage": "voyage",
        "lloyd": "lloyd",
        "eta": "eta",
        "etd": "etd",
        "cusRefNo": "referenceNumber",
        "unlocoPortLoading": "unlocoBoardOfLoading",
        "unlocoPortDischarge": "unlocoBoardOfDischarge",
        "imp available date": "avail",
        "first free date": "freeDate",
        "imp storage start date": "stor",
        "imp storage last date": "storLastFreeDate",
        "exp receival date": "expRcvDate",
        "cargo cutoff date": "cutOffDate",
        "reefer cutoff date": "rcDate",
        "empty receival date": "ercDate",
        "empty cutoff date": "ecDate",
        "harz receival date": "hrcDate",
        "harz cutoff date": "hcDate"
    }
    
    def __init__(self, driver, client_type):
        self.driver = driver
        self.client_type = client_type

    def goto_jobs_page(self, jobs_url):
        self.driver.get(jobs_url)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Transport Job']"))
        )

    def click_create_new_job(self):
        self.driver.find_element(By.XPATH, "//span[text()='New']").click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Detail']"))
        )

    def select_random_option(self, input_id):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, input_id))).click()
        options = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'MuiAutocomplete-option')]"))
        )
        filtered = [opt for opt in options if opt.text.strip() != "Add New"]
        if not filtered:
            raise Exception(f"No valid options found for #{input_id}")
        random.choice(filtered).click()
    
    # Method for filling
    
    def fill_job_type(self, job_type):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "jobType"))).click()
        time.sleep(1)  # Wait for options to load
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{job_type}']"))).click()
        
    def fill_vessel(self, vessel):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "vessel"))).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{vessel}']"))
        ).click()
        
    def fill_voyage(self, voyage):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "voyage")))
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "voyage"))).send_keys(voyage)
        
    def fill_reference_number(self, reference_number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "referenceNumber")))
        self.driver.find_element(By.ID, "referenceNumber").send_keys(reference_number)
    
    def fill_unloco(self, unloco):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "unlocoBoardOfLoading")))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "unlocoBoardOfDischarge")))
        self.driver.find_element(By.ID, "unlocoBoardOfLoading").send_keys(unloco)
        self.driver.find_element(By.ID, "unlocoBoardOfDischarge").send_keys(unloco)
    
    def fill_eta(self, eta):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "eta")))
        self.driver.find_element(By.ID, "eta").send_keys(eta)
    
    def fill_etd(self, etd):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "etd")))
        self.driver.find_element(By.ID, "etd").send_keys(etd)
        
    def fill_imp_available_date(self, imp_available_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "avail")))
            self.driver.find_element(By.ID, "avail").send_keys(imp_available_date)
            return True
        except Exception as e:
            return False

    def fill_first_free_date(self, first_free_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "freeDate")))
            self.driver.find_element(By.ID, "freeDate").send_keys(first_free_date)
            return True
        except Exception as e:
            return False
    
    def fill_imp_storage_start_date(self, imp_storage_start_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "stor")))
            self.driver.find_element(By.ID, "stor").send_keys(imp_storage_start_date)
            return True
        except Exception as e:
            return False
    
    def fill_exp_recv_date(self, exp_recv_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "expRecvDate")))
            self.driver.find_element(By.ID, "expRecvDate").send_keys(exp_recv_date)
            return True
        except Exception as e:
            return False
    
    def fill_cargo_cutoff_date(self, cut_off_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "cutOffDate")))
            self.driver.find_element(By.ID, "cutOffDate").send_keys(cut_off_date)
            return True
        except Exception as e:
            return False
            
    def fill_reefer_cutoff_date(self, reefer_cutoff_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "rcDate")))
            self.driver.find_element(By.ID, "rcDate").send_keys(reefer_cutoff_date)
            return True
        except Exception as e:
            return False
    
    # def fill_empty_recv_date(self, empty_recv_date):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ercDate")))
    #     self.driver.find_element(By.ID, "ercDate").send_keys(empty_recv_date)
    
    def fill_empty_recv_date(self, empty_recv_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ercDate")))
            self.driver.find_element(By.ID, "ercDate").send_keys(empty_recv_date)
            return True
        except Exception as e:
            return False

    def fill_empty_cutoff_date(self, empty_cutoff_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ecDate")))
            self.driver.find_element(By.ID, "ecDate").send_keys(empty_cutoff_date)
            return True
        except Exception as e:
            return False

    def fill_harz_recv_date(self, harz_recv_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "hrcDate")))
            self.driver.find_element(By.ID, "hrcDate").send_keys(harz_recv_date)
            return True
        except Exception as e:
            return False

    def fill_harz_cutoff_date(self, harz_cutoff_date):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "hcDate")))
            self.driver.find_element(By.ID, "hcDate").send_keys(harz_cutoff_date)
            return True
        except Exception as e:
            return False
        
    def fill_agent(self, agent_code=None):
        if agent_code:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "agent"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{agent_code}']"))
            ).click()
        self.select_random_option("agent")
        
    def fill_consignee(self, consignee_code=None):
        if consignee_code:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "consignee"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{consignee_code}']"))
            ).click()
        self.select_random_option("consignee")
    
    def fill_account_receivable(self, account_code=None):
        if account_code:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "accountReceivable"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{account_code}']"))
            ).click()
        self.select_random_option("accountReceivable")
    
    def fill_warehouse(self, warehouse_code=None):
        if warehouse_code:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "warehouse"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{warehouse_code}']"))
            ).click()
        self.select_random_option("warehouse")

    def submit_form(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Save']]"))
        )
        save_button.click()

    def is_success_message_visible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'success')]"))
            )
            return True
        except:
            return False
    
    # Method for getting data
    def get_field_value(self, field_name):
        field_id = self.FIELD_ID_MAP.get(field_name)
        if not field_id:
            raise ValueError(f"Unknown field name: {field_name}")
        return self.driver.find_element(By.ID, field_id).get_attribute("value")
    
    # Method for getting error message
    
    def get_vessel_error(self):
        try:
            return self.driver.find_element(By.ID, "vessel-helper-text").text
        except NoSuchElementException:
            return ''
        
    def get_voyage_error(self):
        try:
            return self.driver.find_element(By.ID, "voyage-helper-text").text
        except NoSuchElementException:
            return ''
        
    def get_etd_error(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "etd")))
            return self.driver.find_element(By.ID, "etd-helper-text").text
        except NoSuchElementException:
            return ''
        
    def get_eta_error(self):
        try:
            return self.driver.find_element(By.ID, "eta-helper-text").text
        except NoSuchElementException:
            return ''
    

class ContainerTab(JobPage):
    def __init__(self, driver):
        self.driver = driver
    
    def gotoContainer(self, job_url, job_id):
        con_url = f"{job_url}/{job_id}"
        self.driver.get(con_url)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Container']"))
        )
        
    def click_add_container(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="AddBoxIcon"]'))
        ).click()
    
    def fill_containerNumber(self, containerNumber):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "code"))
            )
            self.driver.find_element(By.ID, "code").send_keys(containerNumber)
            return True
        except Exception:
            return False
    
    def fill_sealNumber(self, sealNumber):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "sealNumber"))
            )
            self.driver.find_element(By.ID, "sealNumber").send_keys(sealNumber)
            return True
        except Exception:
            return False
    
    def fill_dropMode(self, dropMode):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "dropMode"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{dropMode}']"))
            ).click()
            return True
        except Exception:
            return False
    
    def fill_containerSize(self, containerSize):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "containerSize"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{containerSize}']"))
            ).click()
            return True
        except Exception:
            return False
    
    def fill_net(self, net):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "net"))
            )
            self.driver.find_element(By.ID, "net").send_keys(net)
            return True
        except Exception:
            return False
        
    def fill_door(self, door):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "doorType"))
            )
            self.driver.find_element(By.ID, "doorType").send_keys(door)
            return True
        except Exception:
            return False
    
    def tick_harzadous(self):
        try:
            checkbox = self.driver.find_element(By.XPATH, "//div[@name='isDamagedGood' and .//span[text()='Hazardous Goods']]")
            checkbox.click()
            return True
        except:
            return False
        
    