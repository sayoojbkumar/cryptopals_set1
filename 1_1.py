import codecs

hex = input()
b64 = codecs.decode(hex, 'hex')
b64=codecs.encode(b64,'base64')
print(b64)

