import ed25519
import hashlib

publickey = open("mypublickey-ed25519","rb").read()

myhash = hashlib.sha256()
myhash.update(bytes("Firmamos esto con la curva 25519", "utf8"))
msg_hasheado=myhash.digest()
signature = "53bec6cafc7190c25fc180421cfaed2129c20008f62331dfe35d466c1d1e1e41c9c929a3c6a6cf5492f6945b73503eb7371b5b3b77d6bcf647db5d4264b19003"

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg_hasheado, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
