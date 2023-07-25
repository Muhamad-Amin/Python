""" tutorial membaca file external """

print(3 * "=", " Membaca file txt ", 3 * "=")
file = open("data.txt", mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

""" baca seluruh file """
# print(file.read())


""" baca perbaris """
# print(file.readline(), end="")  # membaca baris pertama
# print(file.readline(), end="")  # membaca baris kedua
# print(file.readline(), end="")  # baca baris selanjutnya


""" baca semua baris sebagai list """
print(file.readlines())


""" close file """
print(f"apakah file sudah di close : {file.closed}")

file.close()
print(f"apakah file sudah di close : {file.closed}")
print("")
print("")


""" salah satu tehnik membuka file di python """

print(3 * "=", " Membaca file txt dengan with ", 3 * "=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
