# looping dari list

# for loop

print('For loop')

kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f'angka = {angka}')

peserta = ['ucup', 'otong', 'dadang', 'diding', 'dudung']

for nama in peserta:
    print(f'nama = {nama}')

print('')

# for loop dan range
print('For loop dan range')

kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

print('')

# while
print('while loop')

kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)

i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

print('')

# List comprehension
print('List comprehension')

data = ['ucup', 1, 2, 3, 'otong']
# [print(i) for i in data]
# atau
[print(f'data = {i}') for i in data]

print('')

print('membuat kuadrat')
# kita juga bisa membuat kuadratnya
kumpulan_angka = [10, 5, 4, 2, 6, 5]
print(kumpulan_angka)

angka_kuadrat = [i ** 2 for i in kumpulan_angka]
print(angka_kuadrat)

print('')

# enumereta -> akan mengambil index dan datanya
print('Enumerate')

data_list = ['ucup', 1, 2, 3, 'otong']

for index, data in enumerate(data_list):
    print(f'index = {index}, data = {data}')
