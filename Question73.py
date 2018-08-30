'''
Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

'''

#help(zlib)
import zlib
import binascii
data = 'Hello World'.encode('utf-8')
len_data = len(data)
compressed_data = zlib.compress(data, 9)
len_compressed_data = len(compressed_data)
print('Original Data: ', data)
print('Compressed data: ', binascii.hexlify(compressed_data))
print('Compressed data lenght: ', len_compressed_data)
print('Original Data lenght: ', len_data)






