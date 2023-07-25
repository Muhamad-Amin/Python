# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # tidak akan di eksekusi
#     print(angka)


# continue -> membuat langsung loncat ke awal loop ( step selanjutnya )

angka = 0

print(f'angka sekarang -> {angka}')

while angka < 5:
    angka += 1
    print(f'angka sekarang -> {angka}')

    if angka == 3:
        print('nice!')
        # akan membuat langsung loncat ke awal loop ( step selanjutnya )
        continue
    print('wassap!')  # ini tidak akan di jalankan jika angka 3

print('finish!!!')
