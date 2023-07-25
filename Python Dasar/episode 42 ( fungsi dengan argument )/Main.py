''' Fungsi dengan argument '''

# import os
# os.system("cls")

# templet
'''
def nama_fungsi(argument):
    badan fungsi
'''


def hello_world(nama):
    ''' fungsi hello world menerima input dengan variabel nama '''
    print(f'selamat datang di dunia wahai {nama} ')


hello_world('ucup')


# program tambah


def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')


tambah(1, 5)
tambah(110000, 5)


def say_hi(list_peserta):
    ''' fungsi say hi '''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'yang terhormat {peserta}')


anggota_boyband = ['ucup', 'otong', 'dudung']

say_hi(anggota_boyband)
