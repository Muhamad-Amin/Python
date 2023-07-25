''' import '''

# import berfungsi untuk mengambil program dari file external  .py

# 1. untuk menyambung program dari external dan menjalankannya
import Matematika
import program_print
import program_ucup

# 2. import dengan data
import variabel
import kucuy

# data ada di namespace variabel
print(variabel.data)
print(kucuy.data)

# 3. import dengan fungsi

hasil = Matematika.tambah(4, 5)
print(hasil)
