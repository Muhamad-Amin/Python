""" Write """

""" 1. mode write """
# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa isinya

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("joni si jhonny")

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("overwrite")


""" 2. mode append """
# tidak akan di timpa

with open("data_2.txt", "w", encoding="utf-8") as file:
    file.write("joni si jhonne\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt", "a", encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")


""" mode r+ """

with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris 1\n")
    file.write("baris 2\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("otong")  # akan menimpa isi text dengan panjang data
