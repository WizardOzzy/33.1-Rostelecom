import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(autouse=True)
def site():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.get('https://b2c.passport.rt.ru')
    wait = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'app-header')))
    assert pytest.driver.find_element(By.ID, 'app-header')

    yield

    pytest.driver.quit()

