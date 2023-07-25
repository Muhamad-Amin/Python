# latihan konversi satuan tempratur

# program konversi celcius ke satua lain

print('\nPROGRAM KONVERSI TEMPRATUR\n')

celcius = float(input('Masukkan suhu dalam celcius : '))
print('suhu adalah', celcius, 'celcius')

# reamur
#  4/5 x celcius
reamur = (4/5) * celcius
print('suhu dalam reamur adalah', reamur, 'Reamur')


# fahrenheit
# 9 / 5 x celcius + 32
fahrenheit = ((9 / 5) * celcius) + 32
print('suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')

# kelvin
# celcius + 273
kelvin = celcius + 273
print('suhu dalam kelvin adalah', kelvin, 'kelvin')
