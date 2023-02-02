import random
import control.controlVignere as vigenere

def keyGenerator():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''
    for i in range(69420):
        key += alphabet[random.randint(0,25)]
    return key

def oneTimePadEncrypt(ptext:str, key):
    cptext = vigenere.vignereChiperEncrypt(ptext, key)
    return cptext

def oneTimePadDecrypt(ptext:str, key):
    cptext = vigenere.vignereChiperDecrypt(ptext, key)
    return cptext
# test
# oneTimePadEncrypt("a quick brown fox jumps over a lazy dog")