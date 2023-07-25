''' Type hants pada fungsi '''
import os
import string

# bentuk standar fungsi yang telah kita pelajari


# Studi kasus

''' 
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil)
    
fungsi(1)
fungsi('ucup')
fungsi(True)
'''


# penggunaan type hints

def fungsi_dengan_hints(argument: int) -> int:
    ''' fungsi dengan hints '''
    output = 10**argument
    return output


hasil = fungsi_dengan_hints(2)
print(hasil)


def display(argument: string):
    print(argument)


display('ucup')
