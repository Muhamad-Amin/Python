from . import Database
from .Util import random_string
import time


def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            print("Panjang tahun harus 4!!!")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    data = Database.TEMPLET.copy()

    data["pk"] = random_string(6)
    # data['date_add'] = time.strftime("%Y-%m-%d %H:%M")
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLET["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLET["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    print(data_str)
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah, gagal bos")


def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            return content
    except:
        print("membaca database error")
        return False


def create(tahun, judul, penulis):
    data = Database.TEMPLET.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLET["penulis"][len(penulis) :]
    data["judul"] = judul + Database.TEMPLET["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit di tambahkan bosss!, gagal maning")
