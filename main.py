from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from PIL import Image
import base64
import io
import qrcode
import random
import re

# Path to the ChromeDriver
driver_path = "path/to/chromedriver"

# Set up Chrome option
chrome_options = webdriver.ChromeOptions()
session_path = "D:/selenium" ## Change this with your path
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")  # Set log level to suppress INFO and WARNING messages
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--mute-audio")
# chrome_options.add_argument("--incognito")  

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Telegram URL
url = 'https://web.telegram.org/k/#@herewalletbot'
driver.get(url)

# Initialize variables

wait = WebDriverWait(driver, 10)


def login():
    first = False
    while True:
        try:
            login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[2]/button'))).click()
            time.sleep(5)
            nomer = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')))
            nomeruser = input("enter your phone number without country code")
            nomer.send_keys(nomeruser)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/button[1]'))).click()
            while True:
                try:
                    textt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[4]/div/p/span')))
                    break
                except:
                    print("Please Wait")
            otp = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[4]/div/div[3]/div/input')))
            otpmu = input("input your otp : ")
            otp.send_keys(otpmu)
        except Exception as e:
            if first:
                driver.get(url)
            print("Login Successfully")
            action()
            break


def action():
    try:
        url = 'https://web.telegram.org/k/#@herewalletbot'
        driver.get(url)
        driver.get(url)
        time.sleep(3)
        input_text_xpath = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div[8]/div[2]/div[1]'
        element_input_text = wait.until(EC.presence_of_element_located((By.XPATH, input_text_xpath)))
        element_input_text.send_keys("/start")
        element_input_text.send_keys(Keys.ENTER)
        element_to_click_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-center"]/div/div/div[3]/div[2]/div[2]/section/div[13]/div/div/div[2]/div[3]')))
        element_to_click_2.click()
        element_to_click_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/button[1]/div')))
        element_to_click_3.click()
        print("Process 1 Success")
        iframe()
    except Exception as e:
        print("Got an error in def action, retry \n")
        return

def claim():
    try:
        while True:
            try:
                waktu_xpath = '/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/p[2]'
                waktu_element = wait.until(EC.presence_of_element_located((By.XPATH, waktu_xpath)))
                waktu_text = waktu_element.text
                # Gunakan regex untuk mencocokkan angka dan satuan waktu
                matches = re.findall(r'(\d+)([hm])', waktu_text)

                # Hitung total waktu dalam menit
                total_waktu = sum(int(value) * (60 if unit == 'h' else 1) for value, unit in matches)
                timee = random.randint(10,30)
                fill = waktu_element.text
                if total_waktu < timee or "Filled" in fill:
                    break
                print(f"Wait {total_waktu} Minutes For Next Claim, dont close the bot")
                time.sleep(int(total_waktu * 60))
                break
            except:
                print("Got an error, retry \n")
                error()
                break

        enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[2]/button')))
        enter_seed_button.click()
        print("Successfully Claim \n")
        time.sleep(60)
        return
    except Exception as e:
        print("Got an error in def claim, retry \n")
        error()

def iframe():
    time.sleep(3)
    try:
        popup_body = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup-body"))
        )

        iframe = popup_body.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        try:
            login =  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/button/p'))).click()
            input_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/label/textarea')))
            seed = input("Enter Your Seed/Phrase here: ")
            input_field.click()
            input_field.send_keys(seed)
            login = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/button'))).click()
            login = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/button'))).click()
            time.sleep(3)
        except:
            pass

        element_to_wait = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[5]/div')))
        element_to_wait.click()
        print("Process 2 Success")
        claim()
    except:
        print("Got an error in def iframe, Please Login To Your HotWallet First the restart the bot \n")
        input()
        error()



def error():
    url = 'https://web.telegram.org/k/#@herewalletbot'
    driver.get(url)
    driver.refresh
    login()

if __name__ == "__main__":
    while True:
        login()