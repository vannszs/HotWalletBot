from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from PIL import Image
import base64
import io

driver_path = "path/to/chromedriver"
session_path = "D:/selenimu2"
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

url = 'https://web.telegram.org/k/#@herewalletbot'
driver.get(url)
time.sleep(3)
last_qr_content = None
first = False
wait = WebDriverWait(driver, 10)

while True:
    try:
        login_header = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/h4')))
        if "Log in to Telegram by QR Code" in login_header.text:
            print("Silahkan Login Dengan Scan QR Code Tersebut")

            canvas_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[1]/canvas')))
            canvas_content_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas_element)

            if canvas_content_base64 != last_qr_content:
                if first:
                    img.close()

                image_content = base64.b64decode(canvas_content_base64)
                img = Image.open(io.BytesIO(image_content))
                img.show()

                last_qr_content = canvas_content_base64
                first = True
            time.sleep(3)
    except Exception as e:
        if first:
            driver.get(url)
        break

try:
    start = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[4]/button[1]')))
    start.click()
except:
    pass

input_text_xpath = '/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div[8]/div[2]/div[1]'
element_input_text = wait.until(EC.presence_of_element_located((By.XPATH, input_text_xpath)))
element_input_text.send_keys("/start")
element_input_text.send_keys(Keys.ENTER)

time.sleep(1)

element_to_click_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-center"]/div/div/div[3]/div[2]/div[2]/section/div[13]/div/div/div[2]/div[3]/a/div')))
element_to_click_2.click()

time.sleep(3)

element_to_click_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/button[1]')))
element_to_click_3.click()

popup_body = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "popup-body"))
)

iframe = popup_body.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

time.sleep(3)

element_to_wait = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]')))
element_to_wait.click()

element_to_click_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[2]/button')))
element_to_click_4.click()

time.sleep(3)

input("masuk ")
driver.quit()
#/html/body/div[1]/div/div[2]/div/div[3]/div/div[2]/div[1]/p[2]