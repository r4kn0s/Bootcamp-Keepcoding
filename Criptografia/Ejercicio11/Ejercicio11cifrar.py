from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

clave_simetrica_hex = "E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
clave_simetrica = bytes.fromhex(clave_simetrica_hex)

with open("clave-rsa-oaep-publ.pem", "rb") as f:
    key_pub = RSA.import_key(f.read())

encryptor = PKCS1_OAEP.new(key_pub, SHA256)

nuevo_cifrado = encryptor.encrypt(clave_simetrica)

print("Texto de vuelto en hex:")
print(nuevo_cifrado.hex().upper())