# Operator untuk dictionary

data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung'
}

"""Menghitung panjang dictionary"""
lendict = len(data_dict)
print(f'panjang dictionary : {lendict}')


"""Mengecek key ada ( exist ) atau tidak"""
key = 'cup'
checkkey = key in data_dict

print(f'apakah {key} ada di data_dict : {checkkey}')


""" Mengecek value ( read ) dengan get """
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kiss'))
print(data_dict.get('kiss', 'key tidak di temukan'))
# cek key dengan message key tidak di temukan


""" Mngupdate data dan menambah """
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)

data_dict['sep'] = 'asep si kasyep'
print(data_dict)

data_dict.update({'cup': 'ucup surucup'})
print(data_dict)
data_dict.update({'amin': 'amin si ganteng dan keren'})
# kalau gak ada di add ( tambahkan ) saja
print(data_dict)

""" Mendelete data """
del data_dict['amin']
print(data_dict)
