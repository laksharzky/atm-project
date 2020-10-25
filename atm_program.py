import random
import datetime
from customer import Customer

cust1 = Customer(id)


while True:
    id = int(input('Masukkan nomor pin anda: '))
    trial = 0

    while (id != int(cust1.infoPin()) and trial < 3):
        id = int(input('Pin anda salah. Silahkan masukkan lagi: '))
        trial +=1
        
        if trial == 3:
            print('Error, maaf silahkan ambil kartu anda dan coba lagi')
            exit()
    while True:
        print('Selamat Datang')
        print('Pilihan Menu')
        print('1. Check Saldo')
        print('2. Debet')
        print('3. Simpan')
        print('4. Ganti Pin')
        print('5. Keluar')



        user = int(input('Silahkan Pilih Opsi: '))

        if user == 1:
            print("saldo anda sekarang: " + str(cust1.infoBalance()))
        elif user == 2:
            nominal = float(input('Masukkan nominal: '))
            verify_withdraw = input('Anda akan melakukan debet dengan nominal berikut ? y/n ' + str(nominal) + " ")
            if verify_withdraw == "y":
                print('Saldo awal anda adalah: Rp ' + str(cust1.infoBalance()))
            else:
                break
            if nominal < cust1.infoBalance():
                cust1.withdrawBalance(nominal)
                print('Tranksaksi anda berhasil dilakukan')
                print('Saldo anda sekarang: Rp ' + str(cust1.infoBalance()))
            else:
                print('Maaf saldo anda tidak mencukupi')
        elif user == 3:
            nominal = int(input('Masukkan nominal: '))
            verify_deposit = input('Anda akan melakukan deposit dengan nominal berikut ? y/n ' + str(nominal) + " ")
            if verify_deposit == "y":
                 cust1.saveDeposit(nominal)
                 print('saldo anda sekarang: Rp ' + str(cust1.infoBalance()))
            else:
                break
        elif user == 4:
            verifikasi = int(input('Masukkan PIN Anda sekarang: '))
            while verifikasi != int(cust1.infoPin()):
                print('Maaf PIN anda salah, silahkan masukkan lagi: ')
            newPin = int(input('Masukkan PIN baru: '))
            print('Pin Anda berhasil diubah')

            verify_newPin = int(input('Silahkan masukkan PIN baru: '))
            if verify_newPin == newPin:
                print('PIN terkonfirmasi')
            else:
                print('Maaf pin anda salah')
           
        elif user == 5:
            resi = random.randint(100000,1000000)
            print('==================================')
            print('No. Resi : ' + str(resi))
            print('==================================')
            print('Tanggal: ',datetime.datetime.now()) 
            print('Sisa saldo Anda: ' + str(cust1.infoBalance()))
            exit()
            


    
        
