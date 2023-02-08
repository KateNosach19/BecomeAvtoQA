from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SingInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(SingInPage.URL)

    def try_login(self, username, password):
        #знайти поле для вводу неправильного імя користувача або пошти         login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem = self.driver.find_element(By.ID, "login_field")

        #ввести неправильне імя або пошту
        login_elem.send_keys(username)

        #знайти поле для вводу пароля 
        pass_elem = self.driver.find_element(By.ID, "password")
        
        #ввести неправильний пароль
        pass_elem.send_keys(password)

        #знайти кнопку   
        btm_elem = self.driver.find_element(By.NAME, "commit")

        #клікнути лівою кнопкою миші  
        btm_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title