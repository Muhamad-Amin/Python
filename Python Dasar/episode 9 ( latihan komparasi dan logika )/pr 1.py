""" PR """
""" ------0++++++5-------8+++++++11--------- """

# -----0
inputUser = float(input('Masukkan angka \n kurang dari 0 \n atau \n kurang dari 5 dan lebih dari 0 \n atau \n kurang dari 8 dan lebih dari 5 \n atau \n kurang dari 11 dan lebih dari 8 \n atau \n lebih dari 11 \n :'))

# -------0++++++
LebihDariNol = inputUser > 0
print('Lebih dari 0 =', LebihDariNol)

# ++++++5------

kurangDariLima = inputUser < 5
print('kurang dari 5 =', kurangDariLima)

# 0++++++++5
PersamaanSatu = LebihDariNol and kurangDariLima
print('Lebih dari 0 dan kurang dari 5 =', PersamaanSatu)

# 5---------
LebihDariLima = inputUser > 5
print('Lebih dari 5 =', LebihDariLima)

# 8+++++
LebihDariDelapan = inputUser > 8
print('lebih dari 8 =', LebihDariDelapan)

# -----8
KurangDariDelapan = not LebihDariDelapan
print('Kurang dari 8 =', KurangDariDelapan)

# 5-------8
PersamaanDua = LebihDariLima and KurangDariDelapan
print('Lebih dari 8 dan kurang dari 5 =', PersamaanDua)


# ++++++11
KurangDariSebelas = inputUser < 11
print('Kurang dari 11 =', KurangDariSebelas)

# 8++++++11
PersamaanTiga = LebihDariDelapan and KurangDariSebelas
print('Lebih dari 8 dan kurang dari 11 =', PersamaanTiga)

# 11--------
LebihDariSebelas = not KurangDariSebelas
print('Lebih dari 11 =', LebihDariSebelas)
