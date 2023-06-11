import pytest
from selenium.webdriver.common.by import By
from sett import *

def test_Incorrect_Pass_Confirm_registration(site):
    """Тест на не правильное потверждение пароля при регистрации. ТС - 014"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(ErrorPass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароли не совпадают'

def test_Incorrect_nametoshort_registration(site):
    """Тест на использование меньше  2 символов в имени при регистрации. TC - 012"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('Т')

    pytest.driver.find_element(By.NAME, 'register').click()

    # Проверка на ошибку что имя слишком короткое
    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_nametolong_registration(site):
    """Тест на использование слишком большого имени при регистрации. TC - 012"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(bigname)

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_namelatin_registration(site):
    """Тест на использовании латинских букв в имени при регистрации. TC - 012"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(latinname)

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_familiyashort_registration(site):
    """Тест на использовании меньше 2 символов в фамилии при регистрации. TC - 013"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Т')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_familiyatolong_registration(site):
    """Тест на использование больше 30 символов в фамилии при регистрации. TC - 013"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(bigname)

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_Incorrect_familiyalatin_registration(site):
    """Тест на использование латинских букв в фамилии при регистрации. TC - 013"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(latinname)

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_NoLatin_registration(site):
    """ Тест на использовании кирилици  в пароле при регистрации. TC - 009 """

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Nolatinpass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Nolatinpass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать только латинские буквы'


def test_NoBig_registration(site):
    """Тест на не использование заглавных символов в пароле. TC - 008"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Passnobig)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Passnobig)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы одну заглавную букву'

def test_short_registration(site):
    """Тест использование менее 8 символов в пароле при регистрации. TC - 007"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(shortpass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(shortpass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не менее 8 символов'

def test_nonumbers_registration(site):
    """Тест на не использование цифр/спецсимволов в пароле при регистрации. TC - 010 """

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(simplepass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(simplepass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

def test_tolong_registration(site):
    """Тест на использование больше 20 символов в пароле при регистрации. TC - 011"""

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Last_Name)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(bigpass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(bigpass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не более 20 символов'