# Latiihan

# Membuat kalkulator sederhana

print(10 * '=')
print('KALKULATOR SEDERHANA')
print(10 * '=' + '\n')

angka_1 = float(input('Masukkan angka 1 : '))
operator = input('operator ( +, -, x, / ) : ')
angka_2 = float(input('Masukkan angka 2 : '))

# percabangan

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == 'x' or operator == '*':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '/' or operator == ':':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah {hasil}')
else:
    print(f'{operator} ini bukan operator yang ada di sini')

print('Akhir dari program penerima gaji!')
