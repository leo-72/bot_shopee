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
os.system('pip install selenium')
print(Back.RED+"Anda Sudah Menginstall Selenium"+Back.BLACK)
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

print(Fore.LIGHTGREEN_EX+"==========================================================")

# Halaman Login Facebook
print(Fore.RED)
print(Back.YELLOW+"HALAMAN LOGIN AKUN SHOPEE KAMU :"+Back.BLACK)
print(Fore.WHITE)
username = str(input("Masukkan Email/No. Anda\t: "))
password = getpass("Masukkan Password Anda\t: ")

print(Fore.LIGHTGREEN_EX+"==========================================================")

# Halaman mengisi alamat
print(Fore.LIGHTYELLOW_EX)
print(Back.RED+"ISIKAN ALAMAT ANDA DISINI UNTUK PENGIRIMAN BARANG :"+Back.BLACK)
print(Fore.WHITE)
name = str(input("Nama Penerima\t\t: "))
no_telp = int(input("Nomor Telepon Penerima\t: "))
provinsi = str(input("Provinsi\t\t: "))
kota = str(input("Kota/Kabupaten\t\t: "))
kecamatan = str(input("Kecamatan\t\t: "))
kodepos = int(input("Kode Pos\t\t: "))
alamat = str(input("Alamat Penerima\t\t: "))
alamat_rinci = str(input("Rincian Alamat Tambahan (opsional): "))

print(Fore.LIGHTGREEN_EX+"==========================================================")

print(Fore.BLUE)
print("Selamat {}!, Semoga beruntung :)".format(name))
print(Fore.WHITE)

driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()
driver.get('https://shopee.co.id/buyer/login')

time.sleep(4)
facebook=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[1]/div[2]')
facebook.click()

time.sleep(3)
new_window=driver.window_handles[1]
driver.switch_to_window(new_window)

time.sleep(2)
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

# MENGHILANGKAN POPUP
time.sleep(5)
close_popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div')
close_popup.click()

# LIHAT SEMUA
time.sleep(2)
look_all = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/a/button')
look_all.click()

# FLASHSALE 00:00
time.sleep(2)
time_zero = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/ul/li[2]/div/a/div[1]')
time_zero.click()

# KLIK PRODUCT
time.sleep(3)
product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[6]/div/div[1]/a/div[1]/div/div')
product.click()

# MEMBELI PRODUCT
time.sleep(2)
buy_product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
buy_product.click()

# CHECKOUT BARANG
time.sleep(4)
checkout = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
checkout.click()

# HALAMAN MENGISI ALAMAT PENERIMA
# NAMA PENERIMA
time.sleep(3)
nameBuyer='{}'.format(name)
enterName = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[1]/input')
enterName.send_keys(nameBuyer)

# NOMOR PENERIMA
nomorBuyer='{}'.format(no_telp)
enterNomor = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[3]/div/div[1]/input')
enterNomor.send_keys(nomorBuyer)

# PROVINSI
time.sleep(2)
provinsi2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div/div/div/span')
provinsi2.click()

time.sleep(2)
if provinsi == "Jawa Timur" or "JAWA TIMUR" or "jawa timur" or "jatim":
    jatim = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[11]')
    jatim.click()
elif provinsi == "Jawa Tengah" or "JAWA TENGAH" or "jawa tengah" or "jateng":
    jateng = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[10]')
    jateng.click()
elif provinsi == "Jawa Barat" or "JAWA BARAT" or "jawa barat" or "jabar":
    jabar = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div/div/div/div[3]/div/div[9]')
    jabar.click()
else:
    print(Fore.RED+"Silahkan Masukkan Provinsi Anda terlebih dahulu !"+Fore.WHITE)

# KOTA/KABUPATEN
time.sleep(2)
kota2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/span')
kota2.click()

time.sleep(2)
if kota == "KOTA MADIUN" or kota == "Kota Madiun" or kota == "kota madiun":
    madiun = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div[3]/div/div[33]')
    madiun.click()
    time.sleep(2)
    kecamatan2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/span')
    kecamatan2.click()
    time.sleep(2)
    if kecamatan == "Taman" or kecamatan == "TAMAN" or kecamatan == "taman":
        taman = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[3]')
        taman.click()
    elif kecamatan == "Kartoharjo" or kecamatan == "KARTOHARJO" or kecamatan == "kartoharjo":
        kartoharjo = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[1]')
        kartoharjo.click()
    elif kecamatan == "Manguharjo" or kecamatan == "MANGUHARJO" or kecamatan == "manguharjo":
        manguharjo = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[2]')
        manguharjo.click()
    else:
        print(Fore.RED+"Silahkan Masukkan Kecamatan Anda !"+Fore.WHITE)

elif kota == "KABUPATEN MADIUN" or kota == "Kabupaten Madiun" or kota == "kabupaten madiun" or kota == "KAB MADIUN" or kota == "KAB. MADIUN" or kota == "Kab. Madiun" or kota == "kab. madiun":
    kab_madiun = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div[3]/div/div[12]')
    kab_madiun.click()
    time.sleep(2)
    kecamatan2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/span')
    kecamatan2.click()
    time.sleep(2)
    if kecamatan == "Wungu" or kecamatan == "WUNGU" or kecamatan == "wungu":
        wungu = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[15]')
        wungu.click()
    elif kecamatan == "Kebonsari" or kecamatan == "KEBONSARI" or kecamatan == "kebonsari":
        kebonsari = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[8]')
        kebonsari.click()
    elif kecamatan == "Mejayan" or kecamatan == "MEJAYAN" or kecamatan == "mejayan":
        mejayan = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/div[3]/div/div[10]')
        mejayan.click()
    else:
        print(Fore.RED+"Silahkan Masukkan Kecamatan Anda !"+Fore.WHITE)

else:
    print(FOre.RED+"Silahkan Masukkan Nama Kota/Kabupaten Anda !"+Fore.WHITE)

# ALAMAT PENERIMA
time.sleep(2)
alamatBuyer='{}'.format(alamat)
alamat2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[8]/div[1]/div/div[1]/textarea')
alamat2.send_keys(alamatBuyer)

# ALAMAT RINCI PENERIMA
time.sleep(2)
alamatRinciBuyer='{}'.format(alamat_rinci)
alamat_rinci2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[8]/div[2]/div/div[1]/input')
alamat_rinci2.send_keys(alamatRinciBuyer)

# OK ALAMAT
time.sleep(2)
okAlamat = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]/button[2]')
okAlamat.click()

# elif kota == "KOTA KEDIRI" or "Kota Kediri" or "kota kediri":
#     kediri = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div[3]/div/div[32]')
#     kediri.click()
# elif kota == "KABUPATEN KEDIRI" or "Kabupaten Kediri" or "kabupaten kediri" or "KAB KEDIRI" or "KAB. KEDIRI" or "Kab. Kediri" or "kab. kediri":
#     kab_kediri = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/div[3]/div/div[9]')
#     kab_kediri.click()

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