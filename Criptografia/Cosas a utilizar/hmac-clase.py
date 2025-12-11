from Crypto.Hash import HMAC, SHA256


clave_bytes = bytes.base64()
datos = bytes(, "utf8")
hmac256 = HMAC.new(clave_bytes, msg=datos, digestmod=SHA256)
print(hmac256.hexdigest())