def spaceKiller(ptext:str):
    output = ''
    for i in range(len(ptext)):
        if(ptext[i] != ' '):
            output += ptext[i]
    return output

def playfairArrptextPrepp(ptext:str):
    prepptext = spaceKiller(ptext).upper()
    filler = 'X'
    output = []
    n = len(prepptext)
    i = 0
    while(i < n-1):
        if(prepptext[i] == prepptext[i+1]):
            output.append(prepptext[i] + filler)
            i+=1
        else:
            output.append(prepptext[i] + prepptext[i+1])
            i+=2
            
    if(n-i == 1):
        output.append(prepptext[i] + filler)
    return output

def playfairChiperKeyArr(key:str):
    keyArr = [[],[],[],[],[]]
    arr = []
    for i in range(len(key)):
        if(key[i] not in arr and key[i] != 'J'):
            (arr).append(key[i])

    #append rest of alphabet
    if(len(arr) < 25):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for i in range(len(alphabet)):
            if(alphabet[i] not in arr and alphabet[i] != 'J'):
                (arr).append(alphabet[i])
    
    # patah arr jadi 5x5
    for i in range(25):
        keyArr[i//5].append(arr[i])
    
    return keyArr

# def playfairChiperEncoder(ptext:str, key:str):
#     prepp_ptext = spaceKiller(ptext).upper
#     prepp_key = spaceKiller(key).upper
#     arrKey = playfairChiperKeyArr(prepp_key)
    
#     cptext = ''

#     #chipering
#     for i in

a = playfairArrptextPrepp('ASADAYOO')
for couple in a:
    print(couple, end=', ')