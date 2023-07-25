""" Looping dictionary """

teman_teman = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
    'sep': 'asep si kusyiep',
    'cuy': 'ucuy surucuy'
}

# loping first try

for teman in teman_teman:
    print(teman)


# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)
# jika menggunakan key yang di tampilkan hanya key nya saja

for key in teman_teman.keys():
    print(teman_teman.get(key))


values = teman_teman.values()
print(values)
# jika menggunakan values yan di tampilkan hanya value nya saja

for value in teman_teman.values():
    print(value)


items = teman_teman.items()
print(items)
# Jika mengambil menggunakan items maka yang di tampilkan seluruh item yang ada di list dictionary

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f'key = {key}, value  {value}')
