""" Copy dictionary """

teman_teman = {
    'cup': 'ucup surucup',
    'tong': 'otong sorotong',
    'dung': 'dudung surudung',
    'sep': 'asep si kusyep',
    'cuy': 'ucuy urucuy'
}

friends = teman_teman.copy()


print(f'teman - teman: {teman_teman}\n')
print(f'friends : {friends}\n')

teman_teman['cup'] = 'ucup si keren'

print(f'teman - teman: {teman_teman}\n')
print(f'friends : {friends}\n')


""" Pop dictionary ( berdasarkan key ) """
# pop adalah mentrasper dari data dictionary ke var yang kita inginkan
dataAsep = friends.pop('sep')
print(f'data  asep : {dataAsep}\n')
print(f'friends : {friends}\n')


""" Pop item dictionary ( yang trakhir ) """
# Pop item akan mengambil  data yang trakhir
dataTrakhir = friends.popitem()
print(f'data  trakhir : {dataTrakhir}\n')
print(f'friends : {friends}\n')
