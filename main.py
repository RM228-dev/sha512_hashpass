import hashlib
import binascii

password = input("Enter password: ")
salt = input ("Enter salt: ")
dk = hashlib.pbkdf2_hmac(hash_name='sha512',
                         password=b'bad_password34',
                         salt=b'bad_salt',
                         iterations=100000)
                         
result = binascii.hexlify(dk)
print(result)
