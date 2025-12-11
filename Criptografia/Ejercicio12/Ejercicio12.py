#Nos debemos comunicar con una empresa, para lo cual, hemos decidido usar un
#algoritmo como el AES/GCM en la comunicación. Nuestro sistema, usa los
#siguientes datos en cada comunicación con el tercero:
#Key:E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74
#Nonce:Si
#¿Qué estamos haciendo mal?
#Cifra el siguiente texto:
#'He descubierto el error y no volveré a hacerlo mal'
#Usando para ello, la clave, y el nonce indicados. El texto cifrado presentalo en'
#hexadecimal y en base64.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
# AES-GCM --> (Datos Asociados + Datos a cifrar) + key + nonce

textoplano = ('He descubierto el error y no volveré a hacerlo mal'.encode('utf-8'))
clave  = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = b64decode('9Yccn/f5nJJhAt2S')#Decodificamos en b64
print('Nonce hex=', nonce.hex())

cifrador = AES.new(clave,AES.MODE_GCM,nonce=nonce)

texto_cifrado,mac = cifrador.encrypt_and_digest(textoplano)


print('texto_cifrado HEX :', texto_cifrado.hex())
print('texto_cifrado B64 :', b64encode(texto_cifrado).decode())
print('Tag (MAC) HEX  :', mac.hex())
print('Tag (MAC) B64  :', b64encode(mac).decode())


#El problema de este ejercicio es que en el enunciado ya nos estas diciendo que nuestro sistema usa los mismos datos en cada comunicacion con el tercero , con AES-GCM el nonce tiene que ser unico y no se si la clave tambien xd, eso hace que sea inseguro