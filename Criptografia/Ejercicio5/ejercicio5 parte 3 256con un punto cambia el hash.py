import hashlib


s = hashlib.sha3_256()
s.update("En KeepCoding aprendemos cómo protegernos con criptografía.".encode("utf-8"))
print(s.hexdigest())
