""" List """
# list = array

# list adalah kumpulan data

# kumpulan data numbers
data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ['ucup', 'otong', 'odah']
print(data_string)

# kumpulan data boolean
data_bool = [True, False, True, True]
print(data_bool)

# kumpulan data campuran
data_campuran = [1, 'bala-bala', 2, 'cireng', 'ucup', True]
print(data_campuran)


""" cara alternatif membuat list """
data_range = range(0, 10, 2)  # ( start, stop, step )
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list
list_pake_for = [i ** 2 for i in range(0, 10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
# tidak akan mecetak angka 5
print(list_pake_for_if)

# genap dan ganjil
list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)
# list_pake_for_if = [i for i in range(0, 10) if i % 2 != 0]
# atau
list_pake_for_if = [i for i in range(0, 10) if i % 2 == 1]
print(list_pake_for_if)
