import secrets
from select import select
import string
import pyperclip
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
def AUTO_FB_CREATE():
    serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    driver.get("https://www.facebook.com/?locale=fr_FR")
    driver.find_element(By.CSS_SELECTOR, "button[data-cookiebanner='accept_button']").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a").click()
    sleep(3)
    def randomnaa(num_names):
        fake=Faker()
        names =[fake.first_name() for _ in range (num_names)]
        return names

    firstname=randomnaa(1)
    #first name fill
    driver.find_element(By.NAME,"firstname").send_keys(firstname)

    def randomnaa1(num_names):
        fake=Faker()
        names =[fake.last_name() for _ in range (num_names)]
        return names

    lastname=randomnaa1(1)

    #last name fill
    driver.find_element(By.NAME,"lastname").send_keys(lastname)
    sleep(2)
    #Random email
    driver.execute_script("window.open('');") 
    driver.switch_to.window(driver.window_handles[1]) 
    driver.get("https://temp-mail.org/fr/") 
    sleep(10)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button").click()
    #Email fill
    driver.switch_to.window(driver.window_handles[0])

    sleep(2)
    driver.find_element(By.NAME,"reg_email__").send_keys(Keys.CONTROL+ "v")
    driver.find_element(By.NAME,"reg_email_confirmation__").send_keys(Keys.CONTROL+ "v")
    email=pyperclip.paste()+"\n"    
    sleep(2)
    #Generate and store a random password 
  
    def randompass(length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password= ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    passw=randompass()
    with open('C:/Users/fsi9/Desktop/script/DATA.txt','w') as file:
        file.write(email)
        file.write(passw)

    driver.find_element(By.ID,"password_step_input").send_keys(passw)
    sleep(2)
    #birthday day
    x_dropdown=Select(driver.find_element(By.NAME,"birthday_day"))
    x_dropdown.select_by_value("21")
    #birthday month
    x_dropdown=Select(driver.find_element(By.NAME,"birthday_month"))
    x_dropdown.select_by_value("8")
    #birthday year
    x_dropdown=Select(driver.find_element(By.NAME,"birthday_year"))
    x_dropdown.select_by_value("1999")

    #sex check
    driver.find_element(By.XPATH,"//input[@name='sex' and @value='2']").click()

    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button").click()
    sleep(30)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]").click()

    sleep(5)
    assert "captcha-recaptcha" not in driver.page_source, "Captcha detected, unable to create account."
    driver.execute_script("alert('Account Created! DATA Saved in your PC');")
    sleep(5)
    driver.quit()


