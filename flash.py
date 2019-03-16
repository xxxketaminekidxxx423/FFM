#MODULE#
import os,sys,time,datetime
from time import sleep
from datetime import datetime
#WAKTU#
waktu = datetime.now()
tahun = waktu.year
bulan = waktu.month
hari = waktu.day
jam = waktu.hour
menit = waktu.minute
detik = waktu.second
waktu2 = time.ctime()
#COLOR#
if sys.platform in ["linux","linux2"]:
	W = ("\033[0m")
	G = ("\033[32;1m")
	R = ("\033[31;1m")
else:
	W = ("")
	G = ("")
	R = ("")
#FUNCTION#
banner =(G+" d88888b d88888b .88b  d88. \n 88'     88'     88'YbdP`88  "+R+"- Fastboot Flashing Mobile\n"+G+" 88ooo   88ooo   88  88  88  "+R+"- Version : 1.0\n "+G+"88~~~   88~~~   88  88  88  "+R+"- Author : Alee Martinezz\n "+G+"88      88      88  88  88  "+R+"- Donate : +6283841365567 (AX)\n "+G+"YP      YP      YP  YP  YP ")
def port():
	print ("\x1bc")
	print (R+"------------------------------")
	print (G+"[!] Cek Devices")
	print (R+"------------------------------\n")
	os.system("fastboot devices")
	print (R+"\n------------------------------\n")
def twrp():
	try:
		print (G+"[+] Menginstall TWRP...")
		namaF = raw_input("Masukan nama file : ")
		os.system("fastboot flash recovery TWRP/"+namaF+".img")
		print (G+"[+] Berhasil menginstall TWRP")
		sleep(3)
		print (G+"[!] Rebooting...")
		os.system("fastboot reboot")
	except:
		print (R+"\n[!] Gagal menginstall TWRP\n")
def flash():
	try:
		print (R+"------------------------")
		print (G+"[1] Flash all")
		print (G+"[2] flash all except data storage")
		print (R+"------------------------")
		pilih = input(W+"Pilih menu : ")
	except:
		print (R+"\n[!] Pilih menu dengan benar\n")
	try:
		if pilih > 2:
			print (R+"\n[!] Pilih menu dengan benar\n")
		elif pilih == 1:
			print (G+"[+] Flashing rom...")
			os.system("fastboot flash tz ROM/tz.mbn")
			os.system("fastboot flash sbll ROM/sbll.mbn")
			os.system("fastboot flash rpm ROM/rpm.mbn")
			os.system("fastboot flash aboot ROM/emmc_appsboot.mbn")
			os.system("fastboot flash tzbak ROM/tz.mbn")
			os.system("fastboot flash rpmbak ROM/rpm.mbn")
			os.system("fastboot flash abootbak ROM/emmc_appsboot.mbn")
			os.system("fastboot flash devcfg ROM/devcfg.mbn")
			os.system("fastboot flash lksecapp ROM/lksecapp.mbn")
			os.system("fastboot flash cmnlib ROM/cmnlib.mbn")
			os.system("fastboot flash cmnlib64 ROM/cmnlib64.mbn")
			os.system("fastboot flash keymaster ROM/keymaster.mbn")
			os.system("fastboot flash devcfgbak ROM/devcfg.mbn")
			os.system("fastboot flash lksecappbak ROM/lksecapp.mbn")
			os.system("fastboot flash cmnlibbak ROM/cmnlib.mbn")
			os.system("fastboot flash cmnlib64bak ROM/cmnlib64.mbn")
			os.system("fastboot flash keymasterbak ROM/keymaster.mbn")
			os.system("fastboot flash dsp ROM/adspso.bin")
			os.system("fastboot erase boot")
			os.system("fastboot flash modem ROM/NON-HLOS.bin")
			os.system("fastboot flash system ROM/system.img")
			os.system("fastboot flash cache ROM/cache.img")
			os.system("fastboot flash userdata ROM/userdata.img")
			os.system("fastboot flash recovery ROM/recovery.img")
			os.system("fastboot flash boot ROM/boot.img")
			os.system("fastboot flash misc ROM/misc.img")
			os.system("fastboot flash splash ROM/splash.img")
			os.system("fastboot flash cust ROM/cust.img")
			print (G+"[!] Flashing rom selesai")
			sleep(3)
			print (G+"[!] Rebooting...")
			os.system("fastboot reboot")
		elif pilih == 2:
			print (G+"[+] Flashing rom...")
			os.system("fastboot flash tz ROM/tz.mbn")
			os.system("fastboot flash sbll ROM/sbll.mbn")
			os.system("fastboot flash rpm ROM/rpm.mbn")
			os.system("fastboot flash aboot ROM/emmc_appsboot.mbn")
			os.system("fastboot flash tzbak ROM/tz.mbn")
			os.system("fastboot flash rpmbak ROM/rpm.mbn")
			os.system("fastboot flash abootbak ROM/emmc_appsboot.mbn")
			os.system("fastboot flash devcfg ROM/devcfg.mbn")
			os.system("fastboot flash lksecapp ROM/lksecapp.mbn")
			os.system("fastboot flash cmnlib ROM/cmnlib.mbn")
			os.system("fastboot flash cmnlib64 ROM/cmnlib64.mbn")
			os.system("fastboot flash keymaster ROM/keymaster.mbn")
			os.system("fastboot flash devcfgbak ROM/devcfg.mbn")
			os.system("fastboot flash lksecappbak ROM/lksecapp.mbn")
			os.system("fastboot flash cmnlibbak ROM/cmnlib.mbn")
			os.system("fastboot flash cmnlib64bak ROM/cmnlib64.mbn")
			os.system("fastboot flash keymasterbak ROM/keymaster.mbn")
			os.system("fastboot flash dsp ROM/adspso.bin")
			os.system("fastboot erase boot")
			os.system("fastboot flash modem ROM/NON-HLOS.bin")
			os.system("fastboot flash system ROM/system.img")
			os.system("fastboot flash cache ROM/cache.img")
			os.system("fastboot flash recovery ROM/recovery.img")
			os.system("fastboot flash boot ROM/boot.img")
			os.system("fastboot flash misc ROM/misc.img")
			os.system("fastboot flash splash ROM/splash.img")
			os.system("fastboot flash cust ROM/cust.img")
			print (G+"[!] Flashing rom selesai")
			sleep(3)
			print (G+"[!] Rebooting...")
			os.system("fastboot reboot")
		else:
			print (R+"\n[!] Pilih menu dengan benar\n")
	except:
		print (R+"\n[!] Pilih menu dengan benar\n")
def adb():
	try:
		print (G+"[+] Menginstall adb & fastboot....")
		os.system("cp ADB/fastboot /data/data/com.termux/files/usr/bin")
		os.system("cp ADB/adb /data/data/com.termux/files/usr/bin")
		os.system("chmod 755 /data/data/com.termux/files/usr/bin/fastboot")
		os.system("chmod 755 /data/data/com.termux/files/usr/bin/adb")
		sleep(3)
		print (G+"[+] Menginstall adb & fastboot selesai")
	except OSError:
		pass
def oem():
	try:
		print ("\x1bc")
		print (R+"--------------------------")
		print (G+"Check OEM & lock").center(30)
		print (R+"--------------------------\n"+G)
		os.system("fastboot oem device-info")
		print (G+"\n--------------------------")
	except:
		print (R+"\n[!] Inputan tidak di temukan")
	sleep(3)
	try:
		print (R+"--------------------------")
		print (G+"[1] Lock OEM [2] Cancel")
		print (R+"--------------------------")
		pilih = input(W+"Pilih menu : ")
		if pilih > 2:
			print (R+"\n[!] Inputan tidak di temukan")
		elif pilih == 1:
			print ("\x1bc")
			print (R+"[!] locking OEM...")
			sleep(3)
			os.system("fastboot oem lock")
			print (G+"\n[!] Success locking OEM\n")
		elif pilih == 2:
			print (R+"\n[!] Cancel for lock OEM\n")
		else:
			print (R+"\n[!] Pilih menu dengan benar\n")
	except:
		print (R+"\n[!] Pilih menu dengan benar\n")
def about():
	print ("\x1bc")
	print (R+"------------------------------------")
	print (G+"Xiaomi Flashing").center(37)
	print (R+"------------------------------------")
	print (G+"Coder : Alee Martinezz")
	print (G+"Find Me :")
	print (G+"Facebook :"+R+" http://fb.me/leemrtnzz")
	print (G+"Telegram :"+R+" http://t.me/leemrtnzz")
	print (G+"Whatsapp :"+R+" +6283841365567 (Axis)")
	print (R+"------------------------------------")
def reset():
	try:
		print (R+"[!] Me-reset data...")
		os.system("fastboot -w")
		print (G+"[!] Me-reset data selesai")
		sleep(3)
		print (G+"[!] Rebooting....")
		os.system("fastboot reboot")
		print (G+"[!] Rebooting selesai")
	except:
		pass
def splash():
	try:
		print (G+"[!] Menginstall splash...")
		masukan = raw_input("Masukan nama file splash : ")
		os.system("fastboot flash splash SPLASH/"+masukan+".img")
		print (G+"[!] Install splash selesai")
		sleep(3)
		print (G+"[!] Rebooting....")
		os.system("fastboot reboot")
		print (G+"[!] Rebooting selesai")
	except SyntaxError:
		pass
	except:
		pass
def update():
	try:
		print (G+"[!] Updating tools...")
		sleep(3)
		os.system("git pull")
		print (G+"[!] Update success")
	except:
		print (R+"[!] Koneksi/File Error")
def menu():
	try:
		try:
			if not os.path.exists("TWRP"):
				os.mkdir("TWRP")
			elif not os.path.exists("ROM"):
				os.mkdir("ROM")
			elif not os.path.exists("ADB"):
				os.mkdir("ADB")
			elif not os.path.exists("SPLASH"):
				os.mkdir("SPLASH")
			else:
				pass
		except OSError:
			pass
		print (R+"-----------------------------")
		print (banner)
		print (R+"--------"+G+"| {}/{}/{} |"+R+"--------").format(hari,bulan,tahun)
		print ("")
		print (G+"[1] Check Device        [5] TWRP")
		print (G+"[2] Check & Lock OEM    [6] About Tool")
		print (G+"[3] Flash ROM           [7] Reset")
		print (G+"[4] Install ADB         [8] SPLASH")
		print (G+"[0] Exit                [9] Update Tools")
		print (R+"--------"+G+"|  {}:{}:{}  |"+R+"--------").format(jam,menit,detik)
		menu = input(W+"Pilih menu : ")
		if menu > 9:
			print (R+"\n[!] Pilih menu dengan benar\n")
		elif menu == 1:
			port()
		elif menu == 2:
			oem()
		elif menu == 3:
			flash()
		elif menu == 4:
			adb()
		elif menu == 5:
			twrp()
		elif menu == 6:
			about()
		elif menu == 7:
			reset()
		elif menu == 8:
			splash()
		elif menu == 9:
			update()
		elif menu == 0:
			print (R+"\n[!] Selamat tinggal\n")
			exit()
		else:
			print (R+"\n[!] Pilih menu dengan benar\n")
	except NameError:
		print (R+"\n[!] Pilih menu dengan benar\n")
	except SyntaxError:
		print (R+"\n[!] Pilih menu dengan benar\n")
if __name__ == "__main__":
	while(True):
	 menu()