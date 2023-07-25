# operator bitwise atau operasi biner, binary
""" operasi bitwise berarti operasi masing-masing byte """

a = 9
b = 5

""" bitwise OR ( | )"""
# akan false jika semuanya false
c = a | b
print('\n===== OR ( | ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('------------- ( | )')
print('nilai :', c, ', binary :', format(c, '08b'))
print('')

""" bitwise AND ( & ) """
# akan true jika semuanya true
c = a & b
print('\n===== AND ( & ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('------------- ( & )')
print('nilai :', c, ', binary :', format(c, '08b'))
print('')

""" bitwise XOR ( ^ ) """
# akan true jika salah satunya true, sisanya akan menjadi false
c = a ^ b
print('\n===== XOR ( ^ ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('------------- ( ^ )')
print('nilai :', c, ', binary :', format(c, '08b'))
print('')

""" bitwise NOT ( ~ ) """
#
c = ~a
print('\n===== NOT ( ~ ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('------------- ( ~ )')
print('nilai :', c, ', binary :', format(c, '08b'))
print('------------- ( ^ )')
d = 0b00001001
e = 0b111111111
print('nilai :', e ^ d, ', binary :', format(e ^ d, '08b'))
print('')


# shifting

""" shift right ( >> ) """
c = a >> 2
print('\n===== shift right ( >> ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('------------- ( >> )')
print('nilai :', c, ', binary :', format(c, '08b'))
print('')

""" shift left ( << ) """
c = a << 2
print('\n===== shift left ( << ) =====\n')
print('nilai :', a, ', binary :', format(a, '08b'))
print('------------- ( << )')
print('nilai :', c, ', binary :', format(c, '08b'))
