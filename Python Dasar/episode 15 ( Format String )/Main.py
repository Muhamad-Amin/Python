# format string

# contoh generic
print('<===== generic =====>')

nama = 'marlin'
str = 'hello ' + nama
print(str)


format_str = f"hello {nama}"
print(format_str)
print('')


# boolean
print('<===== boolean =====>')

boolean = True
format_str = f'boolean = {boolean}'
print(format_str)
print('')

# angka
print('<===== angka =====>')

angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)
print('')

# bilanga bulat
angka = 15
format_str = f'bilangan bulat = type{angka:d}'
# :d = biasanya untuk bilangan bulat. :d = bisa juga gak di bikin
print(format_str)
print('')

# bilangan dengan ordo ribuan
angka = 2000
format_str = f'ribuan = {angka:,}'
# :, = otomastis menambahkan , setelah 3 angka seperti ribuan pada umumnya
print(format_str)
print('')

# bilangan desimal
angka = 2005.54321
format_str = f'desimal = {angka:.2f}'
# :. = menandakan koma di dalam matematika
# :.2f = mengambil dua angka setelah . dengan type data float
print(format_str)
print('')

# menampilkan leading zero
angka = 2005.54321
format_str = f'desimal = {angka:09.3f}'
# :8.3f = akan kegeser 1 atau lebih ( tergantung ) angka jika jumlah angka di var kurang
# :09.3f = akan menambahkan 0 di depan jika kurang 9 angka ( . di hitung )
print(format_str)
print('')

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f'minus = {angka_minus}'
format_plus = f'plus = {angka_plus:+}'
# :+ = akan menampilkan tanda + ( bisa di kombinasikan dengan cara di atas )
print(format_minus)
print(format_plus)
print('')

# memformat persen
persentase = 0.045
format_persen = f'persen = {persentase:.2%}'
# :.2% = hanya menampilkan 2 angka belakang . dengan jenis persen
print(format_persen)
print('')

# melakukan operasi aritmatika di dalam flaaceholder
harga = 10000
jumlah = 5

format_string = f'harga total = Rp. {harga * jumlah:,}'
print(format_string)
print('')

# format angka lain ( binary, octal, hexadecimal )
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hexadicimal = {hex(angka)}'
print(angka)
print(format_binary)
print(format_octal)
print(format_hex)
