import tkinter

main_window = tkinter.Tk()
"""
biasanya di python class di awali dengan huruf besar. 
kalau menggunakan huruf kecil biasanya itu adalah method atau fungsi 
"""

label1 = tkinter.Label(main_window, text="label 1")
label2 = tkinter.Label(main_window, text="label 2")

tombol1 = tkinter.Button(main_window, text="tombol 1")
tombol2 = tkinter.Button(main_window, text="tombol 2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()
