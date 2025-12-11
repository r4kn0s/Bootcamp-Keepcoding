from cryptography.hazmat.primitives.asymmetric import ed25519
import hashlib


with open("ed25519-priv", "rb") as f:
    sk_bytes = f.read()


sk = ed25519.Ed25519PrivateKey.from_private_bytes(sk_bytes[:32])


mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
mensaje_bytes = mensaje.encode("utf-8")


hash_sha256 = hashlib.sha256(mensaje_bytes).hexdigest()
print("Hash SHA-256 del mensaje:", hash_sha256)


firma = sk.sign(mensaje_bytes)


print("Firma Ed25519 (hex):", firma.hex())
