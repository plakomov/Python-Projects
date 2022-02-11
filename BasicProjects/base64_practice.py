import base64 as b

message = "Yay! Hurray!"
message_bytes = message.encode("ascii")
bs4_encrypt = b.b64encode(message_bytes)
bs4_decrypt = b.b64decode(bs4_encrypt)

print(bs4_encrypt, bs4_decrypt.decode("ascii"))