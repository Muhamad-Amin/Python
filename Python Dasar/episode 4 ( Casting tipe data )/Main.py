""" Casting tipe data adalah merubah tipe data ke tipe data yang lain"""
# Belajar casting
# merubah dari satu tipe ke tipe lain
# tipe data = in, float, str, bool


""" INTEGER """
print('===== INTEGER =====')
data_int = 9
print('data =', data_int, 'tipe =', type(data_int))
# berikut cara merubahnya
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan false jika nilai int = 0
print('data =', data_float, 'tipe =', type(data_float))
print('data =', data_str, 'tipe =', type(data_str))
# untuk boolean kalau nilainya 0 maka akan false tapi jika nilainya bukan dari 0 maka akan true
print('data =', data_bool, 'tipe =', type(data_bool))

print('')

""" FLOAT """
print('===== FLOAT =====')
data_float = 9.5
print('data =', data_float, 'tipe =', type(data_float))
# berikut cara merubahnya
data_int = int(data_float)  # akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai float = 0
# untuk integer maka nilai dari float itu akan di bulatkan ke bawah
print('data =', data_int, 'tipe =', type(data_int))
print('data =', data_str, 'tipe =', type(data_str))
print('data =', data_bool, 'tipe =', type(data_bool))

print('')

""" BOOLEAN """
print('===== BOOLEAN =====')
data_bool = True
print('data =', data_bool, 'tipe =', type(data_bool))
# berikut cara merubahnya

# jika nilai bool = true maka menghasilkn 1 kalau bool = false maka akan menghasilkan 0
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
# jika nilai bool = true maka menghasilkn 1.0 kalau bool = false maka akan menghasilkan 0.0
print('data =', data_int, 'tipe =', type(data_int))
print('data =', data_str, 'tipe =', type(data_str))
print('data =', data_float, 'tipe =', type(data_float))

print('')

""" STRING """
print('===== STRING =====')
data_str = '10'
print('data =', data_str, 'tipe =', type(data_str))
# berikut cara merubahnya
# untuk kata - kata tidak bisa di ubah ke int. hanya angka yang bisa di ubah
data_int = int(data_str)
# untuk kata - kata tidak bisa di ubah ke float. hanya angka yang bisa di ubah
data_float = float(data_str)
# bool akan tetap true selama string nya tidak kosong
data_bool = bool(data_str)
print('data =', data_int, 'tipe =', type(data_int))  # string harus angka
print('data =', data_float, 'tipe =', type(
    data_float))  # false jika string kosong
print('data =', data_bool, 'tipe =', type(data_bool))  # string harus angka

print('')
