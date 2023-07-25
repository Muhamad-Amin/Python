# operasi logika atau boolean

# operasi logika ada beberapa yaitu :
""" not, or, and, xor """

""" NOT ( not ) """
# not akan selalu menjadi kebalikannya

print('===== NOT =====')
a = True
c = not a

print('nilai data a =', a)
print('------- NOT')
print('nilai data c =', c)
print('')

""" OR ( or ) """
# Jika salah satu true maka akan menjadi true ( akan false jika semua false )

print('===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)
print('')

""" END ( end ) """
# jika salah satu false maka akan menjadi false ( akan true jika semua true )

print('===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
print('')

""" XOR ( ^ ) """
# akan true jika salah satu saja yang true, sisanya false

print('===== XOR =====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
