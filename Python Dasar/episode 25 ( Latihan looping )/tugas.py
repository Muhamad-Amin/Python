# membuat ketupa menggunakan looping

sisi = 9


count = 0
spasi = int(sisi / 2)

while True:

    if count % 2:
        print(' ' * spasi + '+' * count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

# print(spasi) = -1
# print(count) = 10


# while True:
#     if spasi % 2:
#         print(' ' * spasi + '+' * count)
#         print('%' * spasi)
#         count -= 1
#         spasi += 1
#     else:
#         spasi += 1
#         continue

#     if spasi >= sisi:
#         break

print('+' * 10)
print(' ' + '+' * 9)
print(' ' + '+' * 7)
print(' ' * 2 + '+' * 5)
print(' ' * 3 + '+' * 3)
print(' ' * 4 + '+' * 1)

print('akhir program')
