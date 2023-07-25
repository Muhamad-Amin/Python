import io
from collections import Counter
import datetime

data_waktu = datetime.datetime.now()
# datetime. = module
# datetime = filenya
# now() = fungsinya
print(f' date time now : {data_waktu}')
print(f'tahun : {data_waktu.year}')
print(f'hari : {data_waktu.strftime("%A")}')


# collections = kumpulan data atau array
data = ['a', 'b', 'c', 'a', 'f', 'a', 'b', 'c']

# mengularkan jumlah a
data_count = Counter(data)
print(f'data counter : {data_count}')
print(f'jumlah a = {data_count["a"]}')

# io = standar imput output di python

file = io.open('file_text.txt', 'r')
# file_text.txt = nama file yang ada simpan
# r = baca atau read
print(file.read())
