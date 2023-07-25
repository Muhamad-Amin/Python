# latihan perulangan membuat segitiga

sisi = 7

# 1. Menggunakan for

# dummy variabel
print('AWAL DARI FOR')
count = 1

for i in range(sisi):
    print('*' * count)
    count = count + 1

print('AKHIR DARI FOR \n')


# 2. menggunakan while

print('AWAL DARI WHILE')

count = 1
while True:
    print('*' * count)
    count += 1

    if count > sisi:
        break

print('AKHIR DARI WHILE \n')


# 3. hanya genap saja

print('AWAL HANYA GENAP ')

count = 1
while True:
    count += 1
    # akan kembali ke atas jika ganjil
    if count % 2:
        # print('ganjil')
        continue

    # akan print jika genap
    print('*' * count)

    # akan break atau berhenti jika melebihi sisi
    if count > sisi:
        break

print('AKHIR HANYA GENAP \n')


# 4. hanya ganjil

print('AWAL HANYA GANJIL')

count = 1
while True:

    if count % 2:
        print('*' * count)
        count += 1
    else:
        # kembali ke atas jika ganji
        count += 1
        continue

    # akan break atau berhenti jika melebihi sisi
    if count > sisi:
        break

print('AKHIR HANYA GANJIL \n')


# 5. segitiga sama kaki

print('AWAL SEGITIGA SAMA KAKI')

count = 1
spasi = int(sisi / 2)
while True:

    if count % 2:
        print(' ' * spasi + '+' * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print('AKHIR SEGITIGA SAMA KAKI \n')
