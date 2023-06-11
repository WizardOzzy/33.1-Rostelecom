import pytest
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sett import *


def test_open_site(site):
    """Дымовое на открытие страницы авторизации. TC - 001"""

    response = requests.get('https://b2c.passport.rt.ru/')

    assert response.status_code == 200


def test_open_reg(site):
    """Дымовое на открытие страницы регистрации. TC - 002"""

    pytest.driver.find_element(By.ID, 'kc-register').click()

    assert pytest.driver.find_element(By.NAME, 'register').text == 'Зарегистрироваться'




def test_switching(site):
    """Тест проверяет переключение табов. TC - 005"""
    # В тесте обнаружен баг. Подробнее в баг-репорте (BR-1)

    namelog = pytest.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder')

    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(Mail)
    pytest.driver.find_element(By.ID, 'password').click()
    assert namelog.text == 'Электронная почта'
    for i in range(0, 25):
        pytest.driver.find_element(By.ID, 'username').send_keys(Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    pytest.driver.find_element(By.ID, 'password').click()
    assert namelog.text == 'Мобильный телефон'
    for i in range(0, 25):
        pytest.driver.find_element(By.ID, 'username').send_keys(Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'username').send_keys(ls)
    pytest.driver.find_element(By.ID, 'password').click()
    assert namelog.text == 'Лицевой счёт'
    for i in range(0, 25):
        pytest.driver.find_element(By.ID, 'username').send_keys(Keys.BACKSPACE)
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    pytest.driver.find_element(By.ID, 'password').click()
    assert namelog.text == 'Логин'



def test_registration(site):
    """Тест на валидную регистрацию. TC - 006"""

    response = requests.get(OneSec)

    otvet = response.json()
    with open('mail.txt', 'w', encoding='UTF-8') as data_out:
        data_out.write(otvet[0])
    otvetlist = otvet[0]
    login = otvetlist.split('@')[0]
    domain = otvetlist.split('@')[1]



    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()
    assert pytest.driver.find_element(By.NAME, 'register').text == 'Зарегистрироваться'

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(otvet)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Pass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()
    #Ожидание письма на почту
    time.sleep(30)

    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')

    messages = response.json()

    meskey = messages[0]['id']

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
    text = response.json()
    soup = BeautifulSoup(text['body'], 'html.parser')
    delenieotvet = soup.p.text.split(': ')[1].strip()
    messaglist = list(delenieotvet)
    print(messaglist)

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(1)
    logname = pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name')
    assert logname.text == Last_Name


def test_autorization(site):
    """Тест на валидную авторизацию"""

    # МОЖЕТ ПОТРЕБОВАТЬСЯ ВВОД КАПЧИ
    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)
    # Если капча то время для ввода капчи
    if (pytest.driver.find_elements(By.ID, 'captcha')):
        time.sleep(20)
    else:
        pass
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(1)
    logname = pytest.driver.find_element(By.CLASS_NAME, 'user-name__last-name')
    assert logname.text == Last_Name


def test_pass_change(site):
    """Тест на смену пароля. TC - 016"""


    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    #На ввод капчи
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    #Ожидание прихода письма
    time.sleep(30)

    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')

    messages = response.json()

    meskey = messages[0]['id']

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
    text = response.json()
    soup = BeautifulSoup(text['body'], 'html.parser')
    delenieotvet = soup.p.text.split(': ')[1].strip().split('.')[0]
    messaglist = list(delenieotvet)
    print(messaglist)

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)


    pytest.driver.find_element(By.ID, 'password-new').send_keys(newpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(newpass)


    pytest.driver.find_element(By.ID, 't-btn-reset-pass').click()

    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'password').send_keys(newpass)

    pytest.driver.find_element(By.ID, 'kc-login').click()    #Может быть капча
