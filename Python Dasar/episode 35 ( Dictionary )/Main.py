# list => array, kita akan mengakses data dengan index

data_list = ['ucup', 'otong', 'dudung']

print(data_list[0])

# dictionary ( dict ) => associative array
# identifier atau indentitas => key
# sehingga kita tak perlu index untuk ngakses nya

data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'tg': 'otong',
    'dg': 'dudung',
    'nmbr': 100,
    'list': data_list
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])
