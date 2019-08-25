#Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR
# (^) над символами строки с ключом. Написать также функцию XOR_uncipher, которая по
# зашифрованной строке и ключу восстанавливает исходную строку.

def XOR_cipher(value,key):
    s=''.join(chr(ord(a) ^ ord(b)) for a,b in zip(value,key))
    return s

def XOR_unchiper(value,key):
    s = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(value, key))
    return s


print(XOR_cipher("123","key"))
print(XOR_unchiper("ZWJ","key"))
