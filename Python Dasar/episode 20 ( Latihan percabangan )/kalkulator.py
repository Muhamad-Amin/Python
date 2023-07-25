import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

Window = tk.Tk()
Window.configure(bg="black")
Window.geometry("400x350")
Window.resizable(False, False)
Window.title("Kalkulator")

ANGKA_1 = tk.IntVar()
OPERASI = tk.IntVar()
ANGKA_2 = tk.IntVar()


def button():
    if OPERASI.get() == 1:
        kali = ANGKA_1.get() * ANGKA_2.get()
        pesan = f"{ANGKA_1.get()} x {ANGKA_2.get()} = {kali}"
        showinfo(title="Hasil", message=pesan)
    elif OPERASI.get() == 2:
        bagi = ANGKA_1.get() / ANGKA_2.get()
        pesan = f"{ANGKA_1.get()} / {ANGKA_2.get()} = {bagi}"
        showinfo(title="Hasil", message=pesan)
    elif OPERASI.get() == 3:
        tambah = ANGKA_1.get() + ANGKA_2.get()
        pesan = f"{ANGKA_1.get()} + {ANGKA_2.get()} = {tambah}"
        showinfo(title="Hasil", message=pesan)
    elif OPERASI.get() == 4:
        kurang = ANGKA_1.get() - ANGKA_2.get()
        pesan = f"{ANGKA_1.get()} - {ANGKA_2.get()} = {kurang}"
        showinfo(title="Hasil", message=pesan)
    elif OPERASI.get() == 5:
        modul = ANGKA_1.get() % ANGKA_2.get()
        pesan = f"{ANGKA_1.get()} % {ANGKA_2.get()} = {modul}"
        showinfo(title="Hasil", message=pesan)
    elif OPERASI.get() == 6:
        kali = ANGKA_1.get() * ANGKA_2.get()
        bagi = ANGKA_1.get() / ANGKA_2.get()
        tambah = ANGKA_1.get() + ANGKA_2.get()
        kurang = ANGKA_1.get() - ANGKA_2.get()
        modul = ANGKA_1.get() % ANGKA_2.get()
        pesan = f"""
        {ANGKA_1.get()} x {ANGKA_2.get()} = {kali}
        {ANGKA_1.get()} / {ANGKA_2.get()} = {bagi}
        {ANGKA_1.get()} + {ANGKA_2.get()} = {tambah}
        {ANGKA_1.get()} - {ANGKA_2.get()} = {kurang}
        {ANGKA_1.get()} % {ANGKA_2.get()} = {modul}
        """
        showinfo(title="Hasil", message=pesan)
    else:
        pesan = f"{OPERASI.get()} ini tidak ada dalam pilihan"
        showinfo(title="Hasil", message=pesan)


input_frame = ttk.Frame(Window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

angka_1_label = ttk.Label(input_frame, text="Angka 1")
angka_1_label.pack(padx=10, fill="x", expand=True)
angka_1_entry = ttk.Entry(input_frame, textvariable=ANGKA_1)
angka_1_entry.pack(padx=10, fill="x", expand=True)

operasi_label = ttk.Label(
    input_frame, text="Operasi : \n1. x \n2. / \n3. + \n4. - \n5. % \n6. semuanya"
)
operasi_label.pack(padx=10, fill="x", expand=True)
operasi_entry = ttk.Entry(input_frame, textvariable=OPERASI)
operasi_entry.pack(padx=10, fill="x", expand=True)

angka_2_label = ttk.Label(input_frame, text="Angka 2")
angka_2_label.pack(padx=10, fill="x", expand=True)
angka_2_entry = ttk.Entry(input_frame, textvariable=ANGKA_2)
angka_2_entry.pack(padx=10, fill="x", expand=True)

tombol_hasil = ttk.Button(input_frame, text="button", command=button)
tombol_hasil.pack(pady=10, padx=10, fill="x", expand=True)


Window.mainloop()
