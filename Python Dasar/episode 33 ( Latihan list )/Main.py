# Latihan list

# program list buku

""" Membuat daftar buku """

list_buku = []

while True:

    print('Masukkan data buku')
    judul = input("Masukkan judul buku : ")
    penulis = input("Masukkan nama penulis : ")
    print('')
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print('=' * 10 + 'Data buku' + '=' * 10)
    for index, buku in enumerate(list_buku):
        print(f'{index} | {buku[0]} | {buku[1]}')
    print('=' * 20)

    isLanjut = input('Apakah di lanjutkan ? (y / n ) : ')

    if isLanjut == 'n':
        break
    else:
        continue

print('PROGRAM SELESAI')
