""" tipe data adalah macam-macam data yang bisa kita pakai di python. misalnya """

# a = 10, a adalah variabe dengan nilai 10

# tipe data : angka satuan yang gak ada komanya ( integer )
from ctypes import c_double, c_char  # dan masih banyak lagi
from ctypes import c_double
data_integer = 1

print(type(data_integer))
print('data :', data_integer)
print('bertipe : ', type(data_integer))
# type di atas agar kita mengetahui type datanya

# tipe data : angka dengan koma ( float )
data_float = 1.5
print(type(data_float))
print('data :', data_float)
print('- bertipe : ', type(data_float))

# tipe data : kumpulan karakter ( string )
data_string = 'amin'
print(type(data_string))
print('data :', data_string)
print('- bertipe : ', type(data_string))

# tipe data : biner true / false ( boolean )
data_bool = True
print(type(data_bool))
print('data :', data_bool)
print('- bertipe : ', type(data_bool))

""" tipe data khusus """

# bilangan kompleks
data_complex = complex(5, 6)
print(type(data_complex))
print('data :', data_complex)
print('- bertipe : ', type(data_complex))

# tipe data dari bahasa C

# berikut cara penulisannya

"""" from ctypes import c_double, c_char # dan masih banyak lagi """

# kita akan menggunakan tipe data double yang ada di C ( di mana double ini lebih panjang dari pada float )

data_c_double = c_double(10.5)
print(type(data_c_double))
print('data :', data_c_double)
print('- bertipe : ', type(data_c_double))
