import hashlib
from Crypto.Cipher import AES

# Bloque AES de 16 bytes todo 00
textoPlano_bytes = bytes.fromhex('00000000000000000000000000000000')

# Clave AES (hex)
clave = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

# IV de 16 bytes todo 00
iv_bytes = bytes.fromhex('00000000000000000000000000000000')

# Cifrado AES CBC SIN padding
cipher = AES.new(clave, AES.MODE_CBC, iv_bytes)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)

print("KCV AES:", texto_cifrado_bytes.hex()[0:6].upper())
print("AES ciphertext:", texto_cifrado_bytes.hex().upper())

# SHA-256 de la clave
m = hashlib.sha256()
m.update(clave)
print("KCV SHA256:", m.digest().hex()[0:6].upper())
