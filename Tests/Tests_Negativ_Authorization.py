import pytest
import time
from selenium.webdriver.common.by import By
from sett import *


def test_incorrect_autorizationall(site):
    """Тест на невалидную авторизацию. TC - 004"""

    # Невалидная почта
    pytest.driver.find_element(By.ID, 'username').send_keys(invalid_email)

    # Невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(simplepass)

    #На случай капчи. Вводить вручную
    if (pytest.driver.find_elements(By.ID, 'captcha')):
        time.sleep(20)
    else:
        pass

    pytest.driver.find_element(By.ID, 'kc-login').click()

    error_mess = pytest.driver.find_element(By.ID, 'form-error-message')

    assert error_mess.text == 'Неверный логин или пароль'


def test_incorrect_autorizationapass(site):
    """Тест на невалидную авторизацию используя частино неверные данные. TC - 005"""

    # Валидная почта
    pytest.driver.find_element(By.ID, 'username').send_keys(Mail)

    # Невалидный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(simplepass)
    if (pytest.driver.find_elements(By.ID, 'captcha')):
        time.sleep(20)
    else:
        pass
    pytest.driver.find_element(By.ID, 'kc-login').click()

    error_mess = pytest.driver.find_element(By.ID, 'form-error-message')

    assert error_mess.text == 'Неверный логин или пароль'