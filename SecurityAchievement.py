def enc(msg):
    c = []
    for char in msg:
        c.append(chr(ord(char)^0x69))
    return ''.join(c)


message1 = "Oregon State University is the best"
message2 = "Mastery Challenges are fun"
print message1,message2
print enc(message1), enc(message2)
print enc(enc(message1)), enc(enc(message2))