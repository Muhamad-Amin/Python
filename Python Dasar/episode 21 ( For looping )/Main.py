# perulangan ( loop )

# for kondisi :
#     aksi

# ini dengan list
angka_list = [0, 2, 3, 1, 32]

print(angka_list)

for i in angka_list:  # i akan menjadi angka yang ada di dalam var angka_list
    print(f'i sekarang -> {i}')

print('akhir program 1 \n')

# Ini dengan range
angka_range = range(5)

for i in angka_range:
    print(f'i sekarang -> {i}')

print('akhir program 2 \n')

angka_range = range(1, 5)

for i in angka_range:
    print(f'i sekarang -> {i}')

print('akhir program 3 \n')

# Ini dengan string

data_str = 'saya ganteng abbiezzzz'

for huruf in data_str:
    print(huruf)
print('akhir program 4 \n')
