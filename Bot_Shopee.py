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
print(Back.RED+"Colorama Sudah Terinstall"+Back.BLACK)
os.system('pip install selenium')
print(Back.RED+"Selenium Sudah Terinstall"+Back.BLACK)
os.system('cls')

times=datetime.datetime.now()
tanggal="%s/%s/%s" % (times.day, times.month, times.year)
waktu="%s:%s:%s" % (times.hour, times.minute, times.second)

print('\n')
print(Back.LIGHTYELLOW_EX)
print(Fore.RED+"\t SCRIPT BOT SHOPEE FLASH SALE v1.2 ")
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

print("\n")
print(Back.LIGHTYELLOW_EX)
print(Fore.RED+"\t\t CREATED BY : Leo-72 ")
print(Fore.WHITE)

print(Back.RED+"""*NOTE: (WAJIB DIBACA TERLEBIH DAHULU SEBELUM MENJALANKAN SCRIPTNYA!)
    1.  SCRIPT HANYA BISA DI GUNAKAN UNTUK PC
    2.  SCRIPT SUDAH BISA LOGIN AKUN SHOPEE ITU SENDIRI (*Dengan catatan non-aktifkan kode OTP)
    3.  SCRIPT HANYA BISA BUY VIA INDOMARET
    4.  START SCRIPT 1 MENIT 20 DETIK SEBELUM FLASH SALE DI MULAI
    5.  START SETELAH MEMASUKKAN RINCIAN ALAMAT, LALU ENTER."""+Back.BLACK)

print(Fore.LIGHTGREEN_EX+"======================================================================")

# Halaman Login 
print(Fore.RED)
print(Back.YELLOW+"\t\t HALAMAN LOGIN AKUN SHOPEE KAMU : "+Back.BLACK)
print(Fore.WHITE)
username = str(input("Masukkan Email/No. Anda\t: "))
password = getpass("Masukkan Password Anda\t: ")

print(Fore.LIGHTGREEN_EX+"======================================================================")

# Halaman mengisi alamat
print(Fore.LIGHTYELLOW_EX)
print(Back.RED+"\t ISIKAN ALAMAT ANDA DISINI UNTUK PENGIRIMAN BARANG : "+Back.BLACK)
print(Fore.WHITE)
name = str(input("Nama Penerima\t\t: "))
no_telp = str(input("Nomor Telepon Penerima\t: "))
provinsi = str(input("Provinsi\t\t: "))
kota = str(input("Kota/Kabupaten\t\t: "))
kecamatan = str(input("Kecamatan\t\t: "))
kodepos = str(input("Kode Pos\t\t: "))
alamat = str(input("Alamat Penerima\t\t: "))
alamat_rinci = str(input("Rincian Alamat Tambahan (opsional): "))

print(Fore.LIGHTGREEN_EX+"======================================================================")

print(Fore.BLUE)
print("\tSelamat {}!, Semoga beruntung :)".format(name))
print(Fore.WHITE)

driver = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()
driver.get('https://shopee.co.id/buyer/login')

# time.sleep(5)
# facebook=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[5]/div[2]/button[1]/div[2]')
# facebook.click()

# time.sleep(2)
# new_window=driver.window_handles[1]
# driver.switch_to_window(new_window)

# time.sleep(1)
# userFB='{}'.format(username)
# userlogin = driver.find_element_by_id('email')
# userlogin.send_keys(userFB)

# passFB='{}'.format(password)
# userpass = driver.find_element_by_id('pass')
# userpass.send_keys(passFB)

# loginFB = driver.find_element_by_id('loginbutton')
# loginFB.click()

# new_window2 = driver.window_handles[0]
# driver.switch_to_window(new_window2)

# HALAMAN LOGIN
time.sleep(3)
print(Fore.RED+"Loading\t4% <==>")
userShopee = '{}'.format(username)
user1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input')
user1.send_keys(userShopee)

time.sleep(1)
print("Loading\t8% <====>")
passShopee = '{}'.format(password)
pass1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input')
pass1.send_keys(passShopee)

# KLIK LOGIN
time.sleep(1)
print("Loading\t12% <======>")
loginShopee = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button')
loginShopee.click()

# MENGHILANGKAN POPUP
time.sleep(5)
print("Loading\t16% <========>")
close_popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div')
close_popup.click()

# LIHAT SEMUA
time.sleep(2)
print("Loading\t20% <==========>")
look_all = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/a/button')
look_all.click()

# FLASHSALE 00:00
time.sleep(2)
print("Loading\t24% <============>")
time_zero = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/ul/li[2]/div/a')
time_zero.click()

# KLIK PRODUCT
time.sleep(3)
print("Loading\t28% <==============>")
product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/a/div[1]/div[1]/div')
product.click()

# MEMBELI PRODUCT
time.sleep(2)
print("Loading\t32% <================>")
buy_product = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
buy_product.click()

# CHECKOUT BARANG
time.sleep(5)
print(Fore.YELLOW+"Loading\t36% <==================>")
checkout = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button')
checkout.click()

# HALAMAN MENGISI ALAMAT PENERIMA
time.sleep(4)
print("Loading\t40% <====================>")
ubahAlamat = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]')
ubahAlamat.click()

# TAMBAH ALAMAT BARU
time.sleep(2)
print("Loading\t44% <======================>")
tambahAlamat = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/button')
tambahAlamat.click()

# NAMA PENERIMA
time.sleep(2)
print("Loading\t48% <========================>")
nameBuyer='{}'.format(name)
enterName = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
enterName.send_keys(nameBuyer)

# NOMOR PENERIMA
time.sleep(2)
print("Loading\t52% <==========================>")
nomorBuyer='{}'.format(no_telp)
enterNomor = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div[1]/input')
enterNomor.send_keys(nomorBuyer)

# PROVINSI
time.sleep(2)
print("Loading\t56% <============================>")
provinsi2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[1]')
provinsi2.click()

time.sleep(2)
print("Loading\t60% <==============================>")
if provinsi == "Jawa Timur" or "JAWA TIMUR" or "jawa timur" or "jatim":
    jatim = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[11]')
    jatim.click()
elif provinsi == "Jawa Tengah" or "JAWA TENGAH" or "jawa tengah" or "jateng":
    jateng = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[10]')
    jateng.click()
elif provinsi == "Jawa Barat" or "JAWA BARAT" or "jawa barat" or "jabar":
    jabar = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[9]')
    jabar.click()
else:
    print(Fore.RED+"Silahkan Masukkan Provinsi Anda terlebih dahulu !"+Fore.WHITE)

# KOTA/KABUPATEN
# time.sleep(1)
# kota2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]/div/div/div/span')
# kota2.click()

time.sleep(2)
print("Loading\t64% <================================>")
if kota == "KOTA MADIUN" or kota == "Kota Madiun" or kota == "kota madiun":
    madiun = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[33]')
    madiun.click()
    # time.sleep(1)
    # kecamatan2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/span')
    # kecamatan2.click()
    time.sleep(2)
    print("Loading\t68% <==================================>")
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
    kab_madiun = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[12]')
    kab_madiun.click()
    # time.sleep(1)
    # kecamatan2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[6]/div/div/div/span')
    # kecamatan2.click()
    time.sleep(2)
    print(Fore.GREEN+"Loading\t72% <==================================>")
    if kecamatan == "Wungu" or kecamatan == "WUNGU" or kecamatan == "wungu":
        wungu = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div[15]')
        wungu.click()
        if kodepos == "63181":
            kodeposWungu = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
            kodeposWungu.click()
        else:
            print("INPUTAN SALAH!")
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
print("Loading\t76% <====================================>")
alamatBuyer='{}'.format(alamat)
alamat2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div[1]/textarea')
alamat2.send_keys(alamatBuyer)

# ALAMAT RINCI PENERIMA
time.sleep(2)
print("Loading\t80% <======================================>")
alamatRinciBuyer='{}'.format(alamat_rinci)
alamat_rinci2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[4]/div[2]/div/div[1]/input')
alamat_rinci2.send_keys(alamatRinciBuyer)

# OK ALAMAT
time.sleep(3)
print("Loading\t84% <========================================>")
okAlamat = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]/button[2]')
okAlamat.click()

# OK ALAMAT 2
time.sleep(3)
print("Loading\t88% <==========================================>")
okAlamat2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]')
okAlamat2.click()

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
# alfamartPay = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[7]/button')
# alfamartPay.click()

time.sleep(2)
print("Loading\t92% <============================================>")
indomaretPay = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[8]/button')
indomaretPay.click()

time.sleep(3)
print("Loading\t99% <==============================================>")
buatPesanan = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[2]/div[12]/button')
buatPesanan.click()

print("Loading\t100% SUCCESS"+Fore.WHITE)

time.sleep(10)
os.system('cls')

print(Back.RED+"""
    PRODUK SUDAH DIPESAN !
    CREATED BY : LEO-72"""+Back.BLACK)
print("\n")
print(Fore.YELLOW+"TERIMAKASIH SUDAH MENGGUNAKAN SCRIPT INI DENGAN BAIK ^_^")
