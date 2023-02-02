def falseCharKiller(input:str):
    input = input.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    for i in range(len(input)):
        if(input[i] in alphabet):
            output += input[i]
    return output

def prepText(ptext:str):
    prepptext = falseCharKiller(ptext.upper())
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
    key = falseCharKiller(key)
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

def searchCoor(input:chr, key):
    '''
    nyari posisi huruf dalam key
    '''
    coor = [1,1]
    for i in range(5):
        for j in range(5):
            if(input[0] == key[i][j]):
                coor[0] = j
                coor[1] = i
                return coor
    return None

def processorEnc(input:str, key):
    '''
    proses enc disini uwu!, cuman boleh dua pasang huruf nya!
    '''
    coor1 = searchCoor(input[0], key)
    coor2 = searchCoor(input[1], key)

    if(coor1[0] == coor2[0]):
        coor1[1] = (coor1[1] + 1) % 5
        coor2[1] = (coor2[1] + 1) % 5
    elif(coor1[1] == coor2[1]):
        coor1[0] = (coor1[0] + 1) % 5
        coor2[0] = (coor2[0] + 1) % 5
    else:
        temp = [coor1[0], coor1[1]]
        coor1 = [coor2[0], coor1[1]]
        coor2 = [temp[0], coor2[1]]
    
    output = key[coor1[1]][coor1[0]] + key[coor2[1]][coor2[0]]
    return output

def playfairEnc(ptext:str, key:str):
    '''
    encrypt text pakai playfair nya
    '''
    processed_ptext = prepText(ptext)
    arrkey = playfairChiperKeyArr(key)
    output = ''

    for pair in processed_ptext:
        output += processorEnc(pair, arrkey)
    return output

def playfairDec(cptext:str, key:str):
    '''
    decrypt text pakai playfair nya
    '''
    processed_cptext = prepText(cptext)
    arrkey = playfairChiperKeyArr(key)
    output = ''

    for pair in processed_cptext:
        output += processorDec(pair, arrkey)
    return output

def processorDec(input:str, key):
    '''
    proses dec disini uwu!, cuman boleh dua pasang huruf nya!
    '''
    coor1 = searchCoor(input[0], key)
    coor2 = searchCoor(input[1], key)

    if(coor1[0] == coor2[0]):
        coor1[1] = (coor1[1] - 1) % 5
        coor2[1] = (coor2[1] - 1) % 5
    elif(coor1[1] == coor2[1]):
        coor1[0] = (coor1[0] - 1) % 5
        coor2[0] = (coor2[0] - 1) % 5
    else:
        temp = [coor1[0], coor1[1]]
        coor1 = [coor2[0], coor1[1]]
        coor2 = [temp[0], coor2[1]]
    
    output = key[coor1[1]][coor1[0]] + key[coor2[1]][coor2[0]]
    return output


#testing
enc = playfairEnc("saya adalah manusia super uwu 222!!", "schwarzuwu")
print(enc)
print(playfairDec(enc, "schwarzuwu"))