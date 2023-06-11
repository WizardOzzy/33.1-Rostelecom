import pytest
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from sett import *


def test_incorect_passchange_short(site):
    """Тест на использование меньше 8 символов при смене пароля. ТС - 018 """

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

    #На получение письма
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

    pytest.driver.find_element(By.ID, 'password-new').send_keys(shortpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(shortpass)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не менее 8 символов'

def test_incorect_passchange_nobig(site):
    """"Тест на смену пароля без использования больших букв. ТС - 019"""

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

    #Ожидание письма
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


    pytest.driver.find_element(By.ID, 'password-new').send_keys(Passnobig)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Passnobig)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы одну заглавную букву'


def test_incorect_passchange_nolatin(site):
    """Тест на смену пароля без использования латинских букв. ТС - 019 """

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # На ввод капчи
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    # Ожидание письма
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

    pytest.driver.find_element(By.ID, 'password-new').send_keys(Nolatinpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Nolatinpass)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать только латинские буквы'

def test_incorect_passchange_nonumbers(site):
    """Тест на смену пароля без использования цифр/спецсимволов """

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # На ввод капчи
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    # Ожидание письма
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


    pytest.driver.find_element(By.ID, 'password-new').send_keys(simplepass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(simplepass)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

def test_incorect_passchange_tolong(site):
    """Тест на смену пароля с использованием слишком много символов. ТС - 018 """

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # На ввод капчи
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    # Ожидание письма
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

    pytest.driver.find_element(By.ID, 'password-new').send_keys(bigpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(bigpass)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не более 20 символов'

def test_incorect_passchange_on_actual(site):
    """Тест на смену пароля на актуальный пароль. Данный негативный тест должен производится
       после выполнения тестов Регистраций Авторизаций и смены пароля на новом аккаунте.TC - 017"""

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # На ввод капчи
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    # Ожидание письма
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

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Этот пароль уже использовался, укажите другой пароль'