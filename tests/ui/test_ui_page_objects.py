from modules.ui.page_objects.sing_in_page import SingInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створити обект сторінки
    sing_in_page = SingInPage()

    # відкрити сторінку https://github.com/login
    sing_in_page.go_to()

    # пробуємо зайти в систему GitHub
    sing_in_page.try_login('page_object@gmail.com', 'wrongPassword')

    # перевірити назву сторінку, очікуваній назві
    assert sing_in_page.check_title("Sign in to GitHub · GitHub")

    # закрити браузер
    sing_in_page.close()