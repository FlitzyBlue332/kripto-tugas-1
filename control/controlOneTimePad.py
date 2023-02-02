import random
import controlVignere

def keyGenerator():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''
    for i in range(69420):
        key += alphabet[random.randint(0,25)]
    return key

def oneTimePadEncrypt(ptext:str):
    key = keyGenerator()
    cptext = controlVignere.vignereChiperEncrypt(ptext, key)
    print(key)
    print(cptext)
    return cptext

oneTimePadEncrypt("a quick brown fox jumps over a lazy dog")