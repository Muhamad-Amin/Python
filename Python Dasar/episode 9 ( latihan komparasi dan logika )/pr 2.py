""" PR """
""" ++++++0-------5+++++++8-------11+++++++ """

User = float(input('Masukkan angka \n Kurang dari 0 \n atau \n Lebih dari 0 dan kurang dari 5 \n atau \n Lebih dari 5 dan kurang dari 8 \n atau \n Lebih dari 8 dan kurang dari 11 \n atau \n Lebih dari 11 \n :'))

# +++++ 0

KurangNoll = User < 0
print('Kurang dari 0 =', KurangNoll)

# 0------
LebihNoll = User > 0
print('Lebih dari 0 =', LebihNoll)

# -----5
KurangLima = User < 5
print('Kurang dari 5 =', KurangLima)

# 0-------5
persamaanSatu = LebihNoll and KurangLima
print('Lebih dari 0 dan kurang dari 5 =', persamaanSatu)

# 5+++++
LebihLima = User > 5
print('Lebih dari 5 =', LebihLima)

# +++++8
KurangDelapan = User < 8
print('Kurang dari 8 =', KurangDelapan)

# 5+++++++8
persamaanDua = LebihLima and KurangDelapan
print('Lebih dari 5 dan kurang dari 8 =', persamaanDua)

# 8-------
LebihDelapan = User > 8
print('Lebih dari 8 =', LebihDelapan)

# --------11
KurangSebelas = User < 11
print('Kurang dari 11 =', KurangSebelas)

# 8----------11
persamaanTiga = LebihDelapan and KurangSebelas
print('Lebih dari 8 dan kurang dari 11 =', persamaanTiga)

# 11+++++++
LebihSebelas = User > 11
print('Lebih dari 11 =', LebihSebelas)
