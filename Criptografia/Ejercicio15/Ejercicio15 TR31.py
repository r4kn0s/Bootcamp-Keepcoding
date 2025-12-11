""" EJERCICIO 15 TR31

Nos envían un bloque TR31:
D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B

Donde la clave de transporte para desenvolver (unwrap) el bloque es:
A1A10101010101010101010101010102
¿Con qué algoritmo se ha protegido el bloque de clave? AES con clave derivada
¿Para qué algoritmo se ha definido la clave? AES
¿Para qué modo de uso se ha generado? Cifrar y descifrar un WRAP UUNWRAP
¿Es exportable? Si
¿Para qué se puede usar la clave? para wrap y unwrap
¿Qué valor tiene la clave? c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1 """


from psec import tr31




header, key = tr31.unwrap( kbpk=bytes.fromhex("A1A10101010101010101010101010102"), key_block="D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B")
print(key.hex())


print("Key Version ID: " + header.version_id )
print("Algoritmo: " + header.algorithm)
print("Modo de uso: " + header.mode_of_use)
print("Uso de la clave: " + header.key_usage)
print("Exportabilidad: " + header.exportability)


#Tmb lo he probrado con https://paymentcardtools.com/key-block

