""" Operasi dan manipulasi string """

# 1. menggabungkan string ( concatente )

print('=====Penggabungan String =====')
nama_pertama = 'ucup'
nama_tengah = 'D'
nama_akhir = 'Fame'

nama_lengkap = nama_pertama + ' ' + nama_tengah + ' ' + nama_akhir
print(nama_lengkap)
print('')


# 2. menghitung panjang string
print('==== Menghitung panjang string =====')
panjang = len(nama_lengkap)  # spasi juga di hitung

print('panjang dari ' + nama_lengkap + ' = ' + str(panjang))
# str(panjang) = panjang adalah int di ubah ke str
print('')


# 3. operasi untuk string
print('===== Operasi untuk string =====')
# mengecek apakah ada komponen char atau string di string
"""
in = ada 
not in = tidak ada
"""
d = 'd'
status = d in nama_lengkap  # mengecek apakah ada huruf d di dalam nama_lengkap
print('string ' + d + ' ada di ' + nama_lengkap + ' = ' + str(status) + '\n')

D = 'D'
# mengecek apakah ada huruf D di dalam nama_lengkap
status = D in nama_lengkap
print('string ' + D + ' ada di ' + nama_lengkap + ' = ' + str(status) + '\n')

d = 'd'
# mengecek apakah tidak ada huruf d di dalam nama_lengkap
status = d not in nama_lengkap
print(d + ' tidak ada di ' + nama_lengkap + ' = ' + str(status) + '\n')

D = 'D'
# mengecek apakah tidak ada huruf D di dalam nama_lengkap
status = D not in nama_lengkap
print(D + ' tidak ada di ' + nama_lengkap + ' = ' + str(status) + '\n')

# ngulang string
print('wk'*10)
print(15*'wk' + '\n')

# indexing ( mencri index yang di inginkan )
print('index ke 0 : ' + nama_lengkap[0])
print('index ke 6 : ' + nama_lengkap[6])
print('index ke -1 : ' + nama_lengkap[-1])  # minus mengambil dari belakang
print('index ke -2 : ' + nama_lengkap[-2])
print('index ke [ 0 : 3 ] : ' + nama_lengkap[0: 4])  # : berarti sampai
# yg terakhir tidak di ambil
print('index ke [0, 2, ,4 , 6, 8, 10] : ' + nama_lengkap[0:11:2])
# mencari 0 sampai 10 dengan meloncati 2 setiap ketemu

# item paling kecil
print('paling kecil : ' + min(nama_lengkap))
# item paling besar
print('paling besar : ' + max(nama_lengkap))

# berikut cara python menghitung yg terbesar dan terkecil
ascii_code = ord(' ')
print('ASCII code untuk spasi adalah ' + str(ascii_code))
data = 117
print('char untuk ASCII 117 adalah ' + chr(data))
print('')


# 4. Operator dalam betuk method

data = 'otong surotong pararotong'
jumlah = data.count('o')  # menghitung berapa jumlah o pada var data
print('jumlah o pada ' + data + ' = ' + str(jumlah))
