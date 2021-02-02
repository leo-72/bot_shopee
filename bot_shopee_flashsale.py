# CREATED BY: leo-72
# GITHUB ACCOUNT: https://github.com/leo-72
# INSTAGRAM ACCOUNT: https://www.instagram.com/nadhifpamungkas27

import os
import selenium
from selenium import webdriver
from getpass import getpass
import datetime
import time
import colorama
from colorama import Fore, Back
colorama.init()

os.system('cls')
os.system('pip install colorama')
print(Back.RED+"Anda Sudah Menginstall Colorama"+Back.BLACK)
os.system('cls')

times=datetime.datetime.now()
tanggal="%s/%s/%s" % (times.day, times.month, times.year)
waktu="%s:%s:%s" % (times.hour, times.minute, times.second)

print('\n')
print(Back.LIGHTYELLOW_EX)
print(Fore.RED+"SCRIPT BOT SHOPEE FLASH SALE VIA LOGIN FACEBOOK")
print(Back.BLACK)

print(Fore.RED)
print("""
                Tanggal Sekarang
                    {}
    """.format(tanggal))

print(Fore.RED)
print("""
                 Waktu Sekarang
                    {}
    """.format(waktu))
print(Fore.WHITE)

print(Back.RED+"""*NOTE: 
    1.  SCRIPT HANYA BISA DI GUNAKAN UNTUK PC
    2.  SCRIPT HANYA BISA LOGIN VIA FACEBOOK
    3.  SCRIPT HANYA BISA BUY VIA SHOPEEPAY
    4.  START SCRIPT 30 DETIK SEBELUM FLASH SALE DI MULAI
    5.  START SETELAH MEMASUKKAN PASSWORD, LALU ENTER."""+Back.BLACK)

print(Fore.CYAN)
name = str(input("Masukkan Nama Anda: "))

print(Fore.RED)
print(Back.YELLOW+"HALAMAN LOGIN AKUN SHOPEE KAMU :"+Back.BLACK)
username = str(input("Masukkan Email/No. Anda\t: "))
password = getpass("Masukkan Password Anda\t: ")

print(Fore.BLUE)
print("Selamat {}!, Semoga beruntung :)".format(name))
print(Fore.WHITE)

driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()
driver.get('https://shopee.co.id/buyer/login')

time.sleep(4)
facebook=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[1]/div[2]')
facebook.click()

time.sleep(2)
new_window=driver.window_handles[1]
driver.switch_to_window(new_window)

time.sleep(3)
userFB='{}'.format(username)
userlogin = driver.find_element_by_id('email')
userlogin.send_keys(userFB)

passFB='{}'.format(password)
userpass = driver.find_element_by_id('pass')
userpass.send_keys(passFB)

loginFB = driver.find_element_by_id('loginbutton')
loginFB.click()

new_window2 = driver.window_handles[0]
driver.switch_to_window(new_window2)

time.sleep(5)
close_popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div')
close_popup.click()

time.sleep(2)
look_all = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/a/button')
look_all.click()

time.sleep(2)
time_zero = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/ul/li[2]/div/a/div[1]')
time_zero.click()

time.sleep(2)
product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[6]/div[2]/div[1]/a/div[1]/div[1]/div')
product.click()

time.sleep(2)
buy_product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
buy_product.click()

time.sleep(4)
checkout = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
checkout.click()

# time.sleep(3)
# shopee_pay = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[1]/button/div')
# shopee_pay.click()

# time.sleep(2)
# create_product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')
# create_product.click()

os.system('cls')

print(Back.RED+"""
    PRODUK SUDAH DIPESAN !
    CREATED BY: LEO-72"""+Back.BLACK)
print("\n")
print(Fore.YELLOW+"TERIMAKASIH SUDAH MENGGUNAKAN SCRIPT INI DENGAN BAIK ^^")
