from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Mensaje original
mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
mensaje_bytes = mensaje.encode("utf-8")

# Cargar clave pública
f = open("clave-rsa-oaep-publ.pem", "rb")
clave_publica_pem = f.read()

key_pub = RSA.import_key(clave_publica_pem)

# Hash del mensaje
h = SHA256.new(mensaje_bytes)

# Firma obtenida en la parte 1 (cópiala aquí en bytes)
firma_hex = "A4606C518E0E2B443255E3626F3F23B77B9D5E1E4D6B3DCF90F7E118D6063950A23885C6DECE92AA3D6EFF2A72886B2552BE969E11A4B7441BDEADC596C1B94E67A8F941EA998EF08B2CB3A925C959BCAAE2CA9E6E60F95B989C709B9A0B90A0C69D9EACCD863BC924E70450EBBBB87369D721A9EC798FE66308E045417D0A56B86D84B305C555A0E766190D1AD0934A1BEFBBE031853277569F8383846D971D0DAF05D023545D274F1BDD4B00E8954BA39DACC4A0875208F36D3C9207AF096EA0F0D3BAA752B48545A5D79CCE0C2EBB6FF601D92978A33C1A8A707C1AE1470A09663ACB6B9519391B61891BF5E06699AA0A0DBAE21F0AAAA6F9B9D59F41928D"
firma = bytes.fromhex(firma_hex)

# Verificación
try:
    pkcs1_15.new(key_pub).verify(h, firma)
    print(" La firma ES válida")
except:
    print(" La firma NO es válida")
