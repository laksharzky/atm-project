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

        user = int(input('Menu: '))

        if user == 1:
            print(cust1.infoBalance())
        elif user == 2:
            nominal = int(input('Jumlah: '))
            if nominal < int(cust1.infoBalance()):
                print('Saldo Anda: ' + str(cust1.withdrawBalance(nominal)))
        elif user == 3:
            nominal = int(input('Masukkan Jumlah: '))
            print(cust1.saveDeposit(nominal))
        elif user == 4:
            verifikasi = int(input('Masukkan PIN Anda sekarang: '))
            if verifikasi == int(cust1.infoPin()):
                newPin = int(input('Masukkan PIN baru: '))
                print('Pin Anda berhasil diubah')
            else:
                print('Maaf pin anda salah')
        elif user == 5:
            resi = random.uniform(100000,1000000)
            print('==================================')
            print('No. Resi : ' + str(resi))
            print('==================================')
            dateToday = datetime.datetime.now()
            print(dateToday)
            print('Sisa saldo Anda: ' + str(cust1.infoBalance()))
            exit()
            


    
        
