def trueVignereChipherKey(ptext, key):
    true_key = []
    for i in range(len(ptext)):
        true_key.append(key[i % len(key)])
    return true_key

def vignereExtByteEncrypt(ptext, key):
    true_key = trueVignereChipherKey(ptext, key)
    cptext = b''

    for i in range(len(ptext)):
        enc_char = ((ptext[i] + ord(true_key[i]))%256).to_bytes(1, 'little')
        cptext+=enc_char
    return cptext

def vignereExtByteDecrypt(cptext, key):
    true_key = trueVignereChipherKey(cptext, key)
    ptext = b''

    for i in range(len(cptext)):
        enc_char = ((cptext[i] - ord(true_key[i])) %256).to_bytes(1, 'little')
        ptext += enc_char
    return ptext

def vignereExtEncrypt(ptext, key):
    true_key = trueVignereChipherKey(ptext, key)
    cptext = ''

    for i in range(len(ptext)):
        enc_char = chr((ord(ptext[i]) + ord(true_key[i]))%256)
        cptext+=enc_char
    return cptext

def vignereExtDecrypt(cptext, key):
    true_key = trueVignereChipherKey(cptext, key)
    ptext = ''

    for i in range(len(cptext)):
        enc_char = chr((ord(cptext[i]) - ord(true_key[i])) %256)
        ptext += enc_char
    return ptext


def spaceKiller(ptext:str):
    output = ''
    for i in range(len(ptext)):
        if(ptext[i] != ' '):
            output += ptext[i]
    return output


# test
# f1 = open("sussy_gavial.gif", 'rb')
# ptext = f1.read()
# f1.close()

# f2 = open("sussy_gavial_enc.gif", 'wb')
# cptext = vignereExtByteEncrypt(ptext,'feaFjnhd:Uefjhnw;loeufhefnhleo8iufGbehujewhbfl')
# f2.write(cptext)
# f2.close()

# f2 = open("sussy_gavial_enc.gif", 'rb')
# cptext2 = f2.read()
# print(cptext2[0])
# f2.close()

# deccptext2 = vignereExtByteDecrypt(cptext2, 'feaFjnhd:Uefjhnw;loeufhefnhleo8iufGbehujewhbfl')
# f1 = open("sussy_gavial_dec.gif", 'wb')
# f1.write(deccptext2)

# print(ptext[0], (cptext[0]), cptext2[0], deccptext2[0])
# print(len(ptext), len(cptext), len(cptext2), len(deccptext2))
