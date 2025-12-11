import hashlib


s = hashlib.sha512()
print(s.name)
print(s.digest_size)
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","UTF-8"))
print(s.hexdigest())