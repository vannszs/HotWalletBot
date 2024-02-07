from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import time
import re

session_path = "D:/selenimu2"
os.makedirs(session_path, exist_ok=True)

# Set opsi untuk menyimpan sesi
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

# Inisialisasi WebDriver dengan opsi yang telah diatur
driver = webdriver.Chrome(options=chrome_options)

url = 'https://tgapp.herewallet.app/auth/import'
time.sleep(1)
wait = WebDriverWait(driver, 10)

# Path untuk file seed
seed_file_path = "seed.txt"


def Login(iseed):
    err = 0
    while True:
        try:
            driver.get(url)
            seed_area = '/html/body/div[1]/div/div[1]/label/textarea'
            seed_input = wait.until(EC.element_to_be_clickable((By.XPATH, seed_area)))
            seed_input.click()
            seed_input.send_keys(iseed)
            time.sleep(1)

            enter_seed_xpath = '//*[@id="root"]/div/div[2]/button'
            enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, enter_seed_xpath)))
            enter_seed_button.click()
            time.sleep(3)

            enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button')))
            enter_seed_button.click()
            time.sleep(3)
            print("Berhasil Login")
            enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]')))
            enter_seed_button.click()
            claim(iseed)
            return
        except:
            if err > 5:
                return
            err +=1
            continue

def claim(iseed):
    err = 0
    try:
        while True:
            waktu_xpath = '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/p[2]'
            waktu_element = driver.find_element(By.XPATH, waktu_xpath)
            waktu_text = waktu_element.text
            # Gunakan regex untuk mencocokkan angka dan satuan waktu
            matches = re.findall(r'(\d+)([hm])', waktu_text)

            # Hitung total waktu dalam menit
            total_waktu = sum(int(value) * (60 if unit == 'h' else 1) for value, unit in matches)
            if total_waktu < 30:
                break
            print(f"Belum Saatnya Claim. Tunggu {total_waktu} Menit")
            time.sleep(total_waktu)
            break
        enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/button')))
        enter_seed_button.click()
        print("BERHASIL CLAIM \n")
        time.sleep(10)
        return
    except Exception as e:
        # print(e)
        if err == 0:
            Login(iseed)


if os.path.exists(seed_file_path) and os.path.getsize(seed_file_path) > 0:
    with open(seed_file_path, "r") as file:
        seeds = [line.strip() for line in file]
else:
    seeds = input("Masukkan Seed (pisahkan dengan koma jika lebih dari satu): ").split(",")
    with open(seed_file_path, "w") as file:
        file.write("\n".join(seeds))

iseed_index = 0

while True:
    print(f"Main Start on seed {iseed_index}")
    try:
        iseed = seeds[iseed_index]
        Login(iseed)

        iseed_index += 1
        if iseed_index >= len(seeds):
            iseed_index = 0
    except:
        iseed_index = 0

     