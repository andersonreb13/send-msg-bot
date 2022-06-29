from selenium import webdriver
import urllib
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv


def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]', 40)
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    msg_box.send_keys('\n')
    time.sleep(1)


def prepare_msg():
    base_msg = """ 
    *Python-bot* 
    
    Essa é uma mensagem automática!
    [...] 
    """
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'

    file = open('send-msg-bot/contacts.csv')
    type(file)
    csvreader = csv.reader(file)

    for contact in csvreader:
        msg = urllib.parse.quote(base_msg)
        url_msg = base_url.format(contact[0], msg)
        send_message(url_msg)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
prepare_msg()