from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import time

# Path ke ChromeDriver
driver_path = "path/to/chromedriver"

# Tentukan path untuk menyimpan sesi Selenium
session_path = "D:/selenimu2"

# Pastikan path untuk menyimpan sesi sudah ada
os.makedirs(session_path, exist_ok=True)

# Set opsi untuk menyimpan sesi
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={session_path}")

# Inisialisasi WebDriver dengan opsi yang telah diatur
driver = webdriver.Chrome(options=chrome_options)

url = 'https://tgapp.herewallet.app/auth/import'
driver.get(url)
time.sleep(1)
wait = WebDriverWait(driver, 10)  # Diperpanjang menjadi 10 detik untuk menunggu kondisi tertentu

try:
    print("try login")
    # Membaca seed dari file seed.txt atau meminta input dari pengguna dan menyimpannya ke seed.txt
    seed_file_path = "seed.txt"
    if os.path.exists(seed_file_path) and os.path.getsize(seed_file_path) > 0:
        with open(seed_file_path, "r") as file:
            seed = file.read().strip()
    else:
        seed = input("Masukan Seed: ")
        with open(seed_file_path, "w") as file:
            file.write(seed)

    seed_area = '/html/body/div[1]/div/div[1]/label/textarea'
    seed_input = wait.until(EC.element_to_be_clickable((By.XPATH, seed_area)))
    seed_input.click()
    seed_input.send_keys(seed)
    time.sleep(1)

    # Ganti XPath enter_seed menjadi //*[@id="root"]/div/div[2]/button
    enter_seed_xpath = '//*[@id="root"]/div/div[2]/button'
    enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, enter_seed_xpath)))
    enter_seed_button.click()
    time.sleep(3)

    enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button')))
    enter_seed_button.click()
    time.sleep(3)

    # Loop tunggu hingga teks "Full" muncul pada elemen tertentu
    while True:
        fulltext_xpath = '/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/p'
        fulltext_element = driver.find_element(By.XPATH, fulltext_xpath)
        if "Full" in fulltext_element.text:
            print("Belum Saatnya Claim. Tunggu 2 Jam")
            time.sleep(120)
        else:
            break

    # Klik beberapa tombol berikutnya
    enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]')))
    enter_seed_button.click()

    enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/button')))
    enter_seed_button.click()

    enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/button')))
    enter_seed_button.click()

except Exception as e:
    print(f"Error: {e}")
    pass

input("Masuk ")

driver.quit()
