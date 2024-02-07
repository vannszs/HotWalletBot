from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import time
import re

class HotWalletAutomation:
    def __init__(self):
        # Set opsi untuk mode anonim dan headless
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        # Inisialisasi WebDriver dengan opsi yang telah diatur
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.error_count = 0
        self.url = 'https://tgapp.herewallet.app/auth/import'
        self.seed_file_path = "seed.txt"
        self.load_seeds()

    def load_seeds(self):
        # Membaca semua baris dari seed.txt
        with open(self.seed_file_path, "r") as file:
            self.seeds = [line.strip() for line in file]

    def claim(self):
        for seed_index, seed in enumerate(self.seeds):
            try:
                self.driver.get(self.url)
                time.sleep(1)

                # Mengisi seed pada area input
                seed_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/label/textarea')))
                seed_input.click()
                seed_input.send_keys(seed)
                time.sleep(1)

                # Menekan tombol untuk login
                enter_seed_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/button')))
                enter_seed_button.click()
                time.sleep(3)

                # Menekan tombol setelah login
                enter_seed_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button')))
                enter_seed_button.click()
                time.sleep(3)

                # Loop tunggu hingga teks "Full" muncul pada elemen tertentu
                while True:
                    fulltext_xpath = '/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/p'
                    fulltext_element = self.driver.find_element(By.XPATH, fulltext_xpath)
                    print("BERHASIL LOGIN")

                    if "Full" in fulltext_element.text:
                        break
                    else:
                        self.click_element('/html/body/div[1]/div/div/div/div[3]/div[2]')

                        waktu_xpath = '/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/p[2]'
                        total_waktu = self.get_total_wait_time(waktu_xpath)

                        print(f"Tunggu {total_waktu} Menit Untuk Claim Lagi")
                        if total_waktu <30:
                            break 
                        time.sleep(total_waktu)
                        print("Mencoba Claim Ulang")

                # Klik beberapa tombol berikutnya
                self.claim_success(seed_index)
                
            except Exception as e:
                print("Terjadi Error")
                print("Mengulangi Lagi")
                self.error_count += 1
                if self.error_count > 5:
                    print("Sepertinya anda mengalami error beberapa kali, silahkan coba hubungi @belugaa99 di discord dengan menyertakan screenshot error")
                    self.error_count = 0
                    continue
                else:
                    continue

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def get_total_wait_time(self, xpath):
        waktu_element = self.driver.find_element(By.XPATH, xpath)
        waktu_text = waktu_element.text

        # Gunakan regex untuk mencocokkan angka dan satuan waktu
        matches = re.findall(r'(\d+)([hm])', waktu_text)
        # Hitung total waktu dalam menit
        total_waktu = sum(int(value) * (60 if unit == 'h' else 1) for value, unit in matches)
        return total_waktu

    def claim_success(self, seed_index):
        # Klik beberapa tombol berikutnya
        self.click_element('/html/body/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/button')
        time.sleep(14)
        print(f"Berhasil Klaim akun ke {seed_index}")

    def close_browser(self):
        # Tutup browser pada akhirnya
        self.driver.quit()

# Contoh penggunaan:
while True:
    automation = HotWalletAutomation()
    automation.claim()
    automation.close_browser()
