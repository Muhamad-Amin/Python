''' Operasi atau manipulasi pada list '''

data = ['ucup', 'otong', 'dudung']


# mengambil data dari list

data_0 = data[0]
print(f'data pertama ( index 0 ) = {data_0}')

data_terakhir = data[-1]
print(f'data terakhir adalah = {data_terakhir}')

data_ucup = data[-3]
print(f'data ucup = {data_ucup}')


# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data = {panjang_data}')


''' Manipulasi data list '''

# menambahkan item sesuai posisi
print(f'data sebelum di tambah : \n{data}')
# data.insert(posisi, item)
data.insert(1, 'asep')
print(f'data sesudah di tambah : \n{data}')

# menambah di akhir list
data.append('jajang')
print(f'data di tambah lagi : \n{data}')


""" Menambahkan list dengan list """
data_baru = ['ujang', 'usep', 'dadang']
data.extend(data_baru)
print(f'data gabungan : \n{data}')


""" Merubah data """
# kita ubah data ke 2 ( otong ) menjadi michael
data[2] = 'michael'
print(f'data rubah : \n{data}')


""" Mendelete data atau meremove data """
data.remove('ujang')  # akan error jika salah sebut
# huruf juga harus sesuai
print(f'data remove : \n{data}')


""" Meremove data paling belakang """
data_akhir = data.pop()
print(f'data akhir : \n{data}')
print(data_akhir)
