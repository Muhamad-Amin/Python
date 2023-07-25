data_angka = [1, 435, 433, 3, 56, 7, 3, 7, 4, 3]

print(f'data angka = \n{data_angka}')


""" Count data """
# count data -> menghitung berapa kali suatu data muncul

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f'jumlah angka 4 = {jumlah_data_4}')
print(f'jumlah angka 3 = {jumlah_data_3}')


""" ambil posisi data ( index ) """

data = ['ucup', 'otong', 'dudung', 'ujang']

index_dudung = data.index('dudung')
index_ujang = data.index('ujang')
print(f'index si dudung = {index_dudung}')
print(f'index si ujang = {index_ujang}')


""" Mengurutkan list """
print(f'data angka sebelum sort = \n{data_angka}')
data_angka.sort()
print(f'data angka sort = \n{data_angka}')

print(f'data = {data}')
data.sort()
print(f'data sort = {data}')


""" Membalik list """
data_angka.reverse()
data.reverse()
print(f'data di reverse = \n{data_angka} \n{data}')
