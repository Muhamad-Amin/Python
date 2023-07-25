""" Tehnik menduplikat list """

a = ['ucup', 'otong', 'dudung']

print(f'a = {a}')

b = a  # pass by reference ( membuat nama lain dari list )
print(f'b = {b}')


# kita merubah member dari a

# akan merubah kedua list
a[1] = 'michael'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list a dan b
print(f'a = {hex(id(a))}')
print(f'b = {hex(id(b))}')


# menduplikat list dengan copy

print('membuat list c dengan a.copy()')
c = a.copy()  # full duplikat

print(f'a = {hex(id(a))}')
print(f'b = {hex(id(b))}')
print(f'c = {hex(id(c))}')


print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('kita ubah data 0')
c[0] = 'dadang'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('kita ubah data 1')
c[1] = 'otong'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
