import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    #створити обєкт для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"/c:/Users/catno/BecomeAvtoQA"+r"/chromedriver.exe")
    )

    #відкрити сторінку https://github.com/login
    driver.get("https://github.com/login")

    #знайти поле для вводу імя користувача або поштову адресу 
    login_elem = driver.find_element(By.ID, "login_field")

    #ввести неправильне імя користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@ukr.net")    
    
    #знайти поле де вводити пароль
    pass_elem = driver.find_element(By.ID, "password")

    #вводимо неправильний пароль
    pass_elem.send_keys("wrongpassword")
    
    #знайти кнопку Sing in
    btm_elem = driver.find_element(By.NAME, "commit")

    #клікаємо лівою кнопною миші
    btm_elem.click()

    #перевірка що сторінка така як ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'

    #закрити браузер
    driver.close()
