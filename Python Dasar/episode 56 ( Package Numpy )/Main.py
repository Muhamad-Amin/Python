import numpy as np


''' membuat matrix '''
list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f'list a = {list_a}')
# print(list_a ** 2) # akan gagal
print(f' vector a = {vector_a}')
print(f'vector a pangkat 2 = {vector_a ** 2}')
print(f'vector a kali 5 = {vector_a * 5}')


''' membuat matrix lebih dari satu baris '''
matrix_b = np.array([(1, 2), (3, 4)])
print(f'matrix b = {matrix_b}')

print(f'matrix b^2 = {matrix_b**2}')


''' membuat matrix kosong '''
zeros_c = np.zeros((2, 2))
# (2, 2) = dimensi nya
print(f'zeros c = \n{zeros_c}')


''' satu matrix satu '''
ones_d = np.ones((2, 2))
print(f'ones d = \n{ones_d}')


''' operasi matrix '''
jumlah = matrix_b + matrix_b ** 2 + ones_d
print(f'jumlah = \n{jumlah}')
