import os


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

    opsi = input(
        'pilih salah satu data berikut \n1 = luas \n2 = keliling \n3 = luas dan keliling\n : ')

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)

    if opsi == '1':
        LUAS = hitung_luas(LEBAR, PANJANG)
        display('luas', LUAS)
    elif opsi == '2':
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display('keliling', KELILING)
    elif opsi == '3':
        KELILING = hitung_keliling(LEBAR, PANJANG)
        LUAS = hitung_luas(LEBAR, PANJANG)
        display('luas', LUAS)
        display('keliling', KELILING)
    else:
        print(f'{opsi} tidak di dalam pilihan')

    isContinue = input('apakah lanjut (y/n) ? : ')
    if isContinue == 'n':
        break

print('Program selesai, terima kasih')
