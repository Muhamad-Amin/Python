""" String adalah """

data = 'ini adalah string'

print(data)
print(type(data))

#  '''1. Membuat string'''

'''
    1 dengan menggunakan single quote ( '...' )
    2 dengan menggunakan double quote ( "..." )
'''

data = 'ini menggunakan singgle quote'
print(data)


data = "ini menggunakan double quote"
print(data)

# anda bisa menggabungkan keduanya
print('"Halo apa kabar"')
print("'Halo apa kabar'")
print("ini adalah hari jum'at")


# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')

# backlash
print('C::\\user\\amin')

# tab
print('Ucup \t otong')

# backspace
print('ucup \b otong')

# newline
print('baris pertama. \n baris kedua.')  # LF -> line feed ( MacOs / Linux )
# CR -> carriage return ( khusus yang lama)
print('baris pertama. \r baris kedua.')
# CRLF -> line feed carriage return ( windows )
print('baris pertama. \r\n baris kedua.')


# 3. string literal atau raw

# hati-hati
print('C:\new folder')  # akan salah

# menggunakan raw
print(r'C:\new folder')
# apapun yang ada dalam tanda petik akan menjadi string

# multiline literal string
print("""
Nama : Amin
Kelas : X-RPL 1
""")
# akan menulis semuanya termasuk enternya

# multiline literal string dan raw
print(r"""
Nama : Amin
Kelas : X-RPL 1
Website : www.amin.com/newID
""")
