def trueVignereChipherKey(ptext, key):
    true_key = []
    for i in range(len(ptext)):
        true_key.append(key[i % len(key)])
    return true_key

def vignereExtEncrypt(ptext, key):
    true_key = trueVignereChipherKey(ptext, key)
    cptext = ''

    for i in range(len(ptext)):
        enc_char = chr((ptext[i] + ord(true_key[i]))%256)
        cptext += enc_char
    return cptext

def vignereExtDecrypt(cptext, key):
    true_key = trueVignereChipherKey(cptext, key)
    ptext = ''

    for i in range(len(cptext)):
        enc_char = chr((cptext[i] - ord(true_key[i])) %256)
        ptext += enc_char
    return ptext


def spaceKiller(ptext:str):
    output = ''
    for i in range(len(ptext)):
        if(ptext[i] != ' '):
            output += ptext[i]
    return output

# test
f1 = open("sussy_gavial.gif", 'rb')
ptext = f1.read()
f1.close()

f2 = open("sussy_gavial_enc.gif", 'wb')
cptext = vignereExtEncrypt(ptext,'uwu')
cpenctext = cptext.encode()
f2.write(ptext)

f2.close()
f2 = open("sussy_gavial_enc.gif", 'rb')
cptext2 = f2.read()

print(ptext[0], ord(cptext[0]), cpenctext[0], cptext2[0])

# for i in range(len(cptext)):
#     if(cptext2[i] != cptext[i]):
#         print('T', end=', ')

# f2.close()

# pcptext = vignereExtDecrypt(cptext, 'uwu')