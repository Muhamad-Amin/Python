""" Operator Assignment adalah operasi yang dapat di lakukan dengan penyingkatan """
# operasi di tambah dengan assignment

print('Ini adalah Operasi matematika')
print('')

a = 5  # adalah assignment
print('Nilai a =', a)

a += 1  # artinya a = a + 1
print('Nilai a += 1, maka nilai a menjadi', a)

a -= 2  # artinya adalah a = - 2
print('Nilai a -= 2, maka nilai a menjadi', a)

a *= 5  # artinya adalah a = * 5
print('Nilai a *= 5, maka nilai a menjadi', a)

a /= 2  # artinya adalah a = / 2
print('Nilai a /= 2, maka nilai a menjadi', a)
print('')

print('===== Modulus dan floor division =====')
# Modulus dan floor division

b = 10
print('Nilai b =', b)

b %= 3  # artinya b = b % 3 ( b di bagi 3 dan sisanya berapa )
print('Nilai b %= 3, maka nilai b menjadi', b)
print('')

b = 10
print('Nilai b =', b)

b //= 2  # artinya b = b // 2
print('Nilai b //= 2, maka nilai b menjadi', b)
print('')

print('===== Pangkat atau eksponen =====')
# Pangkat atau eksponen

a = 5
print('Nilai a =', a)
a **= 3  # artinya a pangkat 3
print('Nilai a **= 3, nilai a menjadi', a)
print('')

""" Ini adalah operasi bitwise """

print('Ini adalah operasi bitwise')

print('')

""" OR """
print('===== OR ( | ) =====')
# OR ( | ) atau akan false jika semuanya false
c = True
print('Nilai c =', c)
c |= False  # c = c or false  ( c = c | False)
print('Nilai c |= False, nilai c menjadi', c)

c = False
print('Nilai c =', c)
c |= False  # c = c or false  ( c = c | False)
print('Nilai c |= False, nilai c menjadi', c)
print('')

""" AND """
print('===== AND ( & ) =====')
# AND ( & ) akan true jika keduanya true
c = True
print('Nilai c =', c)
c &= False  # c = c or false  ( c = c & False)
print('Nilai c &= False, nilai c menjadi', c)

c = False
print('Nilai c =', c)
c &= False  # c = c or false  ( c = c & False)
print('Nilai c &= False, nilai c menjadi', c)
print('')

""" XOR """
print('===== XOR ( ^ ) =====')
# XOR ( ^ ) akan true jika salah satunya true
c = True
print('Nilai c =', c)
c ^= False  # c = c or false  ( c = c ^ False)
print('Nilai c ^= False, nilai c menjadi', c)

c = False
print('Nilai c =', c)
c ^= False  # c = c or false  ( c = c ^ False)
print('Nilai c ^= False, nilai c menjadi', c)
print('')

""" geser-geser """
d = 0b0100
print('Nilai d =', format(d, '04b'))
d >>= 2
print('Nilai d >>= 2, nilai d menjadi',  format(d, '04b'))
d <<= 1
print('Nilai d <<= 1, nilai d menjadi',  format(d, '04b'))
