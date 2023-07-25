import time

print("Helo world")

# ini adalah coment
""" ini adalah coment  jika kita ingin membuat coment multi line dengan tanda titik
dua sebanyak tiga kali di awal dan di akhir """

# kita bisa mengcompile python ke yang namanya bytecode
# Cara mengcompile, buka terminal dan tulis
# python -m py_compile cara.py ( cara.py itu adalah nama filenya )

start_time = time.time()

for i in range(1, 100):
    print(f" angka {i}")


print(time.time() - start_time, " detik")
