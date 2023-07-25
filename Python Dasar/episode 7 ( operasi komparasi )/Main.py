""" Operasi komparasi """
# operasi komparasi adalah operasi untuk membandingkan nilai

# setiap hasil dari operasi komparasi adalah boolean ( true / false )
# berikut beberapa operator dari operasi komparasi

""" > , <, >=, <=, ==, !=, is, is not """

a = 4
b = 2
print('a =', a)
print('b =', b)
print('')

# lebih besar dari ( > )
print('===== LEBIH BESAR DARI ( > ) =====')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)
print('')

# lebih kecil dari ( < )
print('===== LEBIH KECIL DARI ( < ) =====')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)
print('')

#  lebih dari sama dengan ( >= )
print('===== lebih dari sama dengan ( >= ) =====')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)
print('')

#  kurang dari sama dengan ( <= )
print('===== kurang dari sama dengan ( <= ) =====')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)
print('')

# sama dengan ( == )
print('===== sama dengan ( == ) =====')
hasil = a == 3
print(a, '==', 3, '=', hasil)
hasil = b == 3
print(b, '==', 3, '=', hasil)
hasil = b == 2
print(b, '==', 2, '=', hasil)
print('')

# tidak sama dengan ( != )
print('===== tidak sama dengan ( != ) =====')
hasil = a != 3
print(a, '!=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
hasil = b != 2
print(b, '!=', 2, '=', hasil)
print('')


print('===== object identify ( is ) =====')
"""" is berfungsi untuk membandingkan memori atau objeck """

# is sebagai komparasi objeck identify

x = 5  # ini adalah assigment membuat object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is y  # ==
print('x is y =', hasil)

x = 5  # ini adalah assigment membuat object
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is y  # ==
print('x is y =', hasil)
print('')

print('===== object identify ( is not ) =====')
"""" is berfungsi untuk membandingkan memori atau objeck """

# is sebagai komparasi objeck identify

x = 5  # ini adalah assigment membuat object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is not y  # !=
print('x is not y =', hasil)

x = 5  # ini adalah assigment membuat object
y = 6
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(y)))
hasil = x is not y  # !=
print('x is not y =', hasil)
