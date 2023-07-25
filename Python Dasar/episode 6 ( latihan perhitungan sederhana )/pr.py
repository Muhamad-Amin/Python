"""  pr """
""" mengonversi fahrenheit ke kelvin dan kelvin ke fahrenheit """


""" konversi fahrenheit ke kelvin """

# rumus secara matematika : 5 / 9 x ( fahrenheit - 32 ) + 273

# fahrenheit - 32 / 9 x 5 + 283


suhu_fahrenheit = float(input('Masukkan suhu fahreheit : '))
# kelvin = 5 / 9 x ( fahrenheit - 32 ) + 273
kelvin = (suhu_fahrenheit - 32) / 9 * 5 + 273
print('suhu fahrenheit adalah', kelvin, 'kelvin')

""" konversi kelvin ke fahrenheit """
suhu_kelvin = float(input('Masukkan suhu kelvin : '))

# fahrenheit = 9/5 x ( kelvin - 273 ) + 32
fahrenheit = 9/5 * (suhu_kelvin - 273) + 32
print('suhu kelvin adalah', fahrenheit, 'fahrenheit')
