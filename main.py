from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import time
import re

# Set opsi untuk mode anonim dan headless
chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

# Inisialisasi WebDriver dengan opsi yang telah diatur
driver = webdriver.Chrome(options=chrome_options)
errorc = 0
url = 'https://tgapp.herewallet.app/auth/import'

while True:
    try:
        driver.get(url)
        time.sleep(1)
        wait = WebDriverWait(driver, 10)

        # Membaca seed dari file seed.txt atau meminta input dari pengguna dan menyimpannya ke seed.txt
        seed_file_path = "seed.txt"
        if os.path.exists(seed_file_path) and os.path.getsize(seed_file_path) > 0:
            with open(seed_file_path, "r") as file:
                seed = file.read().strip()
        else:
            print("Kami tidak akan mengambil atau menyimpan seed anda, seed anda tersimpan pada seed.txt pada file yang sama")
            seed = input("Masukan Seed/Pharse : ")
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
        print("BERHASIL LOGIN")

        # Loop tunggu hingga teks "Full" muncul pada elemen tertentu
        while True:
            fulltext_xpath = '/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/p'
            fulltext_element = driver.find_element(By.XPATH, fulltext_xpath)

            if "Full" in fulltext_element.text:
                break
            else:
                enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]')))
                enter_seed_button.click()

                waktu_xpath = '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/p[2]'
                waktu_element = driver.find_element(By.XPATH, waktu_xpath)
                waktu_text = waktu_element.text
        
                # Gunakan regex untuk mencocokkan angka dan satuan waktu
                matches = re.findall(r'(\d+)([hm])', waktu_text)
                
                # Hitung total waktu dalam menit
                total_waktu = sum(int(value) * (60 if unit == 'h' else 1) for value, unit in matches)
                
                print(f"Tunggu {total_waktu} Menit Untuk Claim Lagi")
                if total_waktu <30:
                    break
                time.sleep(total_waktu)
                print("Mencoba Claim Ulang")
                input()

        # Klik beberapa tombol berikutnya
        print("keluar dari loop")
        enter_seed_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/button')))
        enter_seed_button.click()
        time.sleep(14)
        print("BERHASIL CLAIM")

    except Exception as e:
        print("Terjadi Error")
        print("Mengulangi Lagi")
        errorc +=1
        if errorc >5:
            print("Sepertinya anda mengalami error beberapa kali, silahkan coba hubungi @belugaa99 di discord dengan menyertakan screenshot error")
            errorc = 0
            continue
        else:
            continue

driver.quit()
