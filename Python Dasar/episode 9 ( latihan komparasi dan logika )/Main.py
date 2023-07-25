# Episode latihan komparasi dan logika

# membuat gabungan area rentang dari angka

# ++++++3 -------- 10++++++ ( di daerah 3 true )

inputUser = float(
    input('Masukkan angka nilai \nkurang dari 3 \natau \nlebih besar dari 10 \n: '))

# ++++++3--------
# memeriksa angka yang kurang dari 3
isKurangDari = (inputUser < 3)
print('kurang dari 3 =', isKurangDari)


# ---------10++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('lebih dari 10 =', isLebihDari)

# ++++++3 -------- 10++++++

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukkan :', isCorrect)


# -------3+++++++10---------
# kasus irisan
print('\n', 10*'=', '\n')
inputUser = float(
    input('Masukkan angka nilai \nlebih dari 3 \ndan \nkurang dari 10 \n: '))

# --------3++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print('lebih dari 3 =', isLebihDari)

# ++++++++10-------
# kurang dari 10
isKurangDari = inputUser < 10
print('kurang dari 10 =', isKurangDari)

# ------ 3+++++++10 ------

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan :', isCorrect)
