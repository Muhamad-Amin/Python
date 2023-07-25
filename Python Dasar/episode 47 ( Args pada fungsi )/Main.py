''' *args '''

# memasukkan data / argument


def fungsi(nama, tinggi, berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi('ucup', 170, 40)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi(['otong', 100, 120])

# *args = argument


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi('dudung', 120, 120)

# studi kasus


def tambah(*data):  # penamaanya tidak harus *args, bisa yang lain
    # data tipenya adalah tuple dan bisa iterasi
    output = 0
    for angka in data:
        output += angka

    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f'hasil = {hasil}')
hasil = tambah(10, 15, 5)
print(f'hasil = {hasil}')
