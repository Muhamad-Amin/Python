import datetime
import os
import string
import random

# templet dictionary mmahasiswa
mahasiswa_templet = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 11, 1)
}

data_mahasiswa = {}

while True:
    os.system('cls')  # cls = windows
    # os.system('clear')  # clear = MacOs
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print('-'*20)

    mahasiswa = dict.fromkeys(mahasiswa_templet.keys())

    mahasiswa['nama'] = input('Nama Mahasiswa : ')
    mahasiswa['nim'] = input('NIM Mahasiswa : ')
    mahasiswa['sks_lulus'] = int(input('SKS Lulus : '))
    TAHUN_LAHIR = int(input('Tahun lahir (yyyy) : '))
    BULAN_LAHIR = int(input('Bulan lahir (1 - 12) : '))
    TANGGAL_LAHIR = int(input('Tahun lahir (1 - 31) : '))
    mahasiswa['lahir'] = datetime.datetime(
        TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    # dari tutorial sebelum nya, hilangkan beasiswa
    print(f'\n{"KEY":<6} {"NAMA":17} {"NIM":<8} {"SKS":^10} {"LAHIR":^10} ')
    print('-'*60)
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

        print(f'{KEY:<6} {NAMA:17} {NIM:<8} {SKS:^10} {LAHIR:^10} ')
    print('\n')
    is_done = input('Mau tambah lagi bro (y/n) ? : ')
    if is_done == 'n':
        break


print('Akhir dari program, Terima kasih')
