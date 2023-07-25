""" program managment kontak """

import function
import os

if __name__ == "__main__":
    sistem_operasi = os.name


match sistem_operasi:
    case "posix":
        os.system("clear")
    case "nt":
        os.system("cls")
# list of dictionary
daftar_kontak = []
daftar_kontak.append(
    {"nama": "Amin", "email": "amin@gmail.com", "telepon": "081234567890"}
)

# menu program
while True:
    print("#Menu")
    print("0. Keluar program")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")

    menu = input("Pilih menu : ")

    match menu:
        case "0":
            break
        case "1":
            function.display_kontak(daftar_kontak)
        case "2":
            kontak = function.new_kontak()
            daftar_kontak.append(kontak)
        case "3":
            function.hapus_kontak(daftar_kontak)
        case "4":
            function.cari_kontak(daftar_kontak)
        case other:
            print("Menu tidak tersedia")

    # if menu == "0":
    #     break
    # elif menu == "1":
    #     function.display_kontak(daftar_kontak)
    # elif menu == "2":
    #     kontak = function.new_kontak()
    #     daftar_kontak.append(kontak)
    # elif menu == "3":
    #     function.hapus_kontak(daftar_kontak)
    # elif menu == "4":
    #     function.cari_kontak(daftar_kontak)
    # else:
    #     print("Menu tidak tersedia")


print("program selesai berjalan, sampai jumpa")
