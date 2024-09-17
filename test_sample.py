import pytest
from time import sleep
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def login_qa():
    email = "lucas.silva@voxuy.com"
    senha = "Lucas123"

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver.get("https://web.voxuy.com")

    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(senha)

    driver.find_element(By.XPATH, '/html/body/app-root/app-auth-layout/div/div[2]/div[2]/app-login/form/button[1]').click()
    sleep(2)
    whatsapp = driver.find_element(By.CLASS_NAME, 'section-title').is_displayed()

    if whatsapp:
        return True
    
    return False



def test_answer_login():
    assert login_qa() == True
