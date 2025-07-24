from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_login_page(self, signin_url):
        self.driver.get(signin_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Sign In']"))
        )
    
    def select_tenant(self, tenant_name='demo'):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "tenant"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space(text())='{tenant_name}']"))).click()
    
    def fill_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)
    
    def fill_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    def click_sign_in(self):
        self.driver.find_element(By.XPATH, "//button[.//span[text()='Sign In']]").click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/admin/dashboard")
            )
            return True
        except:
            return False