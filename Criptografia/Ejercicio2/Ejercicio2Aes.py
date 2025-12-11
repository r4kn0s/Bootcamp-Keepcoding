#Ejercicio 2
#Dada la clave con etiqueta “cifrado-sim-aes-256” que contiene el keystore. El iv estará
#compuesto por el hexadecimal correspondiente a ceros binarios (“00”). Se requiere
#obtener el dato en claro correspondiente al siguiente dato cifrado:
#
#
#Para este caso, se ha usado un AES/CBC/PKCS7. Si lo desciframos, ¿qué
#obtenemos?
#¿Qué ocurre si decidimos cambiar el padding a x923 en el descifrado?
#¿Cuánto padding se ha añadido en el cifrado?
#
#



 #Descifrado
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
claveC = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
#claveC = clave Hexadecimal
#claveP = Clave AES-256 la del keystorePractica
#AES/CBC el IV tiene que ser de 16bytes
claveP = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
clave = bytes.fromhex(claveP)
iv_desc_bytes = bytes.fromhex("00000000000000000000000000000000")#128bits = 16bytes "Explicacion de clase  AES 128bits/8 16 bytes 16letras por bloque de 128bits"
texto_cifrado_bytes = b64decode(claveC)
cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size,"pkcs7")
print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))


# Descifrado : El texto en claro es:  Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.
# tiene 79bytes (Cuidado acentos que cuentan como+1, 79 no es multiplo de 16 yo he multiplicado 16 x5 son 80 es lo mas cerca a79 )
# a la pregunta ¿Cuánto padding se ha añadido en el cifrado? 1

