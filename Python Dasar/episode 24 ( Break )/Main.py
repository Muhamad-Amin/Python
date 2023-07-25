# break -> ketika kondisi true maka akan keluar dari loop

angka = 0

while angka < 5:
    angka += 1
    print(f'angka sekarang -> {angka}')

    if angka == 3:
        print('nice!')
        break

    print('wasssapp!')

print('cukup finish! \n')

data_int = int(input('hitung sampai berapa : '))

angka = 0

while angka <= data_int:
    angka += 1
    print(f'angka sekarang -> {angka}')

    if angka == data_int:
        print('nice!')
        break

    print('wasssapp!')

print('cukup finish!')
