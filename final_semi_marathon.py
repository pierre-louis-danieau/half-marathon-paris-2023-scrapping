import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


def charger_plus_function(driver, n=850):
    actions = ActionChains(driver)
    a = time.time()
    for i in range(n):
        charger = WebDriverWait(driver,600).until(EC.presence_of_element_located((By.CLASS_NAME, 'view-more-list__view-more-link')))
        actions.click(charger)
        actions.perform()

def get_data(url):
    ## Update with the right path of your own web driver ##
    chrome_path = r'/Users/pierre-louis.danieau/Documents/pierre-louis-danieau/perso/web_scrapping/driver_optimized/chromedriver.exe' # web driver optimized
    
    
    service = Service(executable_path=chrome_path)
    options = Options()
    options.headless = False  # hide GUI
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(10)
    result = driver.get(url) 
    time.sleep(10)
    charger_plus_function(driver, n=10)
    try:
        soup = BeautifulSoup(driver.page_source, 'html5lib')

        rang = soup.find_all("div", {"class": "event-home__rank"})

        result = soup.find_all("div", {"class": "event-home__result"})

        info = soup.find_all("div", {"class": "event-home__info"})
    except:
        rang, result, info = [], [], []

    return rang, result, info 



def find_elements(rang, result, info):
    rang_list=[]
    for rang_i in rang:
        rang_list.append(rang_i.get_text())

    name_list=[]
    temps_list=[]
    temps_supp_list = []
    result_n = 0
    for result_i in result:
        if result_n%4==1:
            name_i = result_i.get_text()
            name_list.append(name_i)
        elif result_n%4==2:
            temps_i=result_i.get_text()
            temps_list.append(temps_i)
        elif result_n%4==3:
            temps_supp_i=result_i.get_text()
            temps_supp_list.append(temps_supp_i)
        result_n = result_n + 1

    result_n = 0
    status_list = []
    sex_list=[]
    age_list=[]

    for info_i in info:
        if result_n%4==1:
            sex_age = info_i.get_text()
            sex, age = sex_age.split('|')[0],sex_age.split('|')[1]
            sex_list.append(sex)
            age_list.append(age)
        elif result_n%4==2:
            status_i=info_i.get_text()
            status_list.append(status_i)
        result_n = result_n + 1

    return rang_list, name_list, temps_list, temps_supp_list, sex_list, age_list, status_list

def create_dataframe(rang_list, name_list, temps_list, temps_supp_list, sex_list, age_list, status_list):
    try:
        data = {'rang': rang_list, 'nom':name_list, 'temps': temps_list, 'temps_supp_list':temps_supp_list, 'sex':sex_list, 'age':age_list,'statut':status_list}
        df = pd.DataFrame.from_dict(data)
    except:
        import pdb; pdb.set_trace()
    return df

if __name__=="__main__":
    url = 'https://resultscui.active.com/events/HarmonieMutuelleSemideParis2023'

    rang, result, info = get_data(url)

    rang_list, name_list, temps_list, temps_supp_list, sex_list, age_list, status_list = find_elements(rang, result, info)
    df = create_dataframe(rang_list, name_list, temps_list, temps_supp_list, sex_list, age_list, status_list)

    df.to_csv('result.csv')
