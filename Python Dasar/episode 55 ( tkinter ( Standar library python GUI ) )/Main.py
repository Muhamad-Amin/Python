# GUI -> Grafhical User Interface

import tkinter as tk
# tk biasanya untuk window utamanya
from tkinter import ttk
# ttk = tema untuk tkinter
from tkinter.messagebox import showinfo

window = tk.Tk()


window.configure(bg="black")  # background
window.geometry("300x200")  # ukuran
window.resizable(False, False)  # bisa di ubah atau tidak ukuran GUI
window.title("Sapa dia")  # judul dari GUI

'''frame input'''
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

'''komponen-komponen'''

# 1. label untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
# (window, text="ucup") = penempatan labelnya
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. entry nama depan ( tempat ketik )
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
# (window, text="ucup") = penempatan labelnya
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. entry nama belakang ( tempat ketik )
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. tombol


def tombol_click():
    ''' Ini akan di panggil oleh tombol '''
    pesan = f'Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Gantenggggg'
    # .get() = untuk menampilkan pesannya secara keseluruhan
    showinfo(title="Infomassez", message=pesan)


tombol_sapa = ttk.Button(input_frame, text="button", command=tombol_click)
tombol_sapa.pack(pady=10, padx=10, fill="x", expand=True)


# main loop window
window.mainloop()
