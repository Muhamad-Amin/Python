from . import Operasi

DB_NAME = "data.txt"
TEMPLET = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-aa",
    "judul": 255 * " ",
    "penulis": 255 * " ",
    "tahun": "yyyy",
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("database tersedia")
    except:
        print("database tidak tersedia, silahkan buat dataase baru")
        Operasi.create_first_data()
