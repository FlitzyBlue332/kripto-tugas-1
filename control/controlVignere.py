# Nama: Muhammad Raihan Aulia (Fletz)
# NIM: 18220031

def trueVignereChipherKey(ptext, key):
    true_key = []
    for i in range(len(ptext)):
        true_key.append(key[i % len(key)])
    return true_key

def vignereChiperEncrypt(ptext:str, key:str):
    prepp_ptext = spaceKiller(ptext).upper()
    prepp_key = spaceKiller(key).upper()
    true_key = trueVignereChipherKey(prepp_ptext, prepp_key)
    cptext = ''

    for i in range(len(prepp_ptext)):
        enc_char = chr((ord(prepp_ptext[i]) + ord(true_key[i]))%26 + ord('A'))
        cptext += enc_char
    return cptext

def vignereChiperDecrypt(cptext:str, key:str):
    prepp_key = spaceKiller(key).upper()
    prepp_cptext = spaceKiller(cptext).upper()
    true_key = trueVignereChipherKey(prepp_cptext, prepp_key)
    ptext = ''

    for i in range(len(prepp_cptext)):
        enc_char = chr((ord(prepp_cptext[i]) - ord(true_key[i]))%26 + ord('A'))
        ptext += enc_char
    return ptext


def spaceKiller(ptext:str):
    output = ''
    for i in range(len(ptext)):
        if(ptext[i] != ' '):
            output += ptext[i]
    return output




    
# test
print(vignereChiperDecrypt('UMOCYEVNIQJZITDOIJMKPYNUFWTSZIA','uwu'))
print(vignereChiperEncrypt('a quick brown fox jumps over a lazy dog','uwu'))


