''' Operator dalam bentuk method '''

# 1. merubah case ( besar kecil huruf ) dari string
print('<===== Merubah case dari string =====>')

# merubah semua ke upper case ( huruf besar )

salam = 'bro!'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)
# print('upper = ' + salam.upper()) = lebih singkat

# merubah semua ke lower case ( huruf kecil )
alay = 'aKu keCe AbiezzZZzzz'
print('nornal = ' + alay)
alay = alay.lower()
print('lower = ' + alay)
print('')


# 2. pengecekan menggunakan isX method
print('<===== Pengecekan dengan isX method =====>')

# contoh pengecekan lower case
apakah_lower = salam.islower()  # hasil bool
# di atas akan mengecek apakah var salam adalah lower
print(salam + ' is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper()  # hasil bool
# di atas akan mengecek apakah var salam adalah ipper
print(salam + ' is upper = ' + str(apakah_upper))

# berikut beberapa macam-macam is
# isalpha = mengecek semuanya huruf dan tidak kosong
# isalnum = huruf dan angka
# isdecimal = angka saja
# isspace = ngecek string kosong, bisa spasi, tab, newline
# capitalize = membuat huruf awal besar
# casefold = membuat semua huruf kecil
# istitle = semua kata di mulai dengan huruf besar

judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle()
print(judul + ' is title ' + str(cek_judul))
print('')


# 3. mengecek komponen startswith() dan endswith()
print('<===== mengecek komponen startswith() endswith() =====>')

cek_start = 'Sangjangnim Oppa'.startswith('Sangjangnim')
# kata yang di dalam var harus sama dengan yang ada di startswith
print('start = ' + str(cek_start))

cek_end = 'Sangjangnim Oppak'.endswith('Oppak')
print('end = ' + str(cek_end))
print('')


# 4. penggabungan komponen dengan join() dan split()
# join = menggabung atau menambahkan
# split = pisah
print('<===== penggabungan komponen dengan join() split() =====>')

pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))
print('')


# 5. alokasi karakter rjust(), ljust(), center()
print('<===== alokasi karakter =====>')
'''
ada beberapa alokasi karakter, yaitu :
rjust() = rata kanan
ljust() = rata kiri
center() = rata tengah
'''

kanan = 'kanan'.rjust(10)
print("|" + kanan + "|")

kiri = 'kiri'.ljust(10)
print("|" + kiri + "|")

tengah = 'tengah'.center(10, '-')
print("|" + tengah + "|")
print('')


# 6. strip() -> kebalikan alokasi
print("<===== Strip() atau kebalikan alokasi =====>")

tengah = tengah.strip('-')  # akan menghilang tanda -
print("|" + tengah + "|")
