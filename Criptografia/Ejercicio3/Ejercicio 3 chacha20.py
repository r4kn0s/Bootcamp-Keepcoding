#Ejercicio 3
#Se requiere cifrar el texto “KeepCoding te enseña a codificar y a cifrar”. La clave para
#ello, tiene la etiqueta en el Keystore “cifrado-sim-chacha-256”. El nonce
#“9Yccn/f5nJJhAt2S”. El algoritmo que se debe usar es un Chacha20.
#¿Cómo podríamos mejorar de forma sencilla el sistema, de tal forma, que no sólo
#garanticemos la confidencialidad sino, además, la integridad del mismo? Se requiere
#obtener el dato cifrado, demuestra, tu propuesta por código, así como añadir los
#datos necesarios para evaluar tu propuesta de mejora.




from Crypto.Cipher import ChaCha20

from base64 import b64decode, b64encode



textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')

#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = b64decode('9Yccn/f5nJJhAt2S')
print("nonce = ", nonce_mensaje.hex())


#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano)

print('Mensaje cifrado en HEX = ', texto_cifrado.hex())

#La version chachapoly1305, tienee lo bueno del cifrado de chacha y ademas el poly1305 nos va a añadir un tag de autentificacion.
#Es decir se mejora el sistema de cifrado con poly para añadir integridad y autenticacion.
#


