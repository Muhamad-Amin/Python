''' Latihan fungsi '''

import os

# program menghitung luas dan keliling persegi panjang

# # membuat header program

# os.system('cls')  # windows / linux
# # os.system('clear') # macOs
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f'-'*40)


# # mengambil input user
# LEBAR = int(input('Masukkan nilai lebar : '))
# PANJANG = int(input('Masukkan nilai panjang : '))

# # program menghitung luas

# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # tampilkan hasil nya
# print(f'hasil perhitung luas = {LUAS}')
# print(f'hasil perhitung keliling = {KELILING}')


def header():
    ''' Fungsi Header '''
    os.system('cls')  # windows / linux
    # os.system('clear') # macOs
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f'-'*40)


def input_user():
    ''' Fungsi input user '''
    lebar = int(input('Masukkan nilai lebar : '))
    panjang = int(input('Masukkan nilai panjang : '))

    return lebar, panjang


def hitung_luas(lebar, panjang):
    ''' Fungsi luas '''
    return lebar * panjang


def hitung_keliling(lebar, panjang):
    ''' Fungsi Keliling '''
    return 2 * (lebar + panjang)


def display(message, value):
    ''' Fungsi display 
    '''
    print(f'hasil perhitungan {message} = {value}')


# program utama
while True:
    header()

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display('luas', LUAS)
    display('keliling', KELILING)

    isContinue = input('apakah lanjut (y/n) ? : ')
    if isContinue == 'n':
        break

print('Program selesai, terima kasih')
