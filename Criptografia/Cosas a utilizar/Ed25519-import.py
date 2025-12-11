from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
mensaje_bytes = mensaje.encode("utf-8")

f = open("clave-rsa-oaep-priv.pem", "rb")
clave_privada_pem = f.read()

key_priv = RSA.import_key(clave_privada_pem)

h = SHA256.new(mensaje_bytes)

signer = pkcs1_15.new(key_priv)
firma = signer.sign(h)

print("Firma RSA PKCS#1 v1.5 (HEX):")
print(firma.hex().upper())
