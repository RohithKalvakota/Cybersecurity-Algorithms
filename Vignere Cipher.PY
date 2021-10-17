print("Kalvakota Rohith")
choice = input("Which operation to Perform Encryption(E/e) OR Decryption(D/d)?")
list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if ord(choice.upper()) == 69:
    plaintext = input("Enter Plain Text to be converted into Cipher Text:")
    key = input("Enter key:")
    keystream = ""
    if len(key)> len(plaintext):
        print("ERROR: Enter Key as of equal or of less length of plain text")
    else:
        for i in range(0,len(plaintext)-len(key)):
            key = key+key[i]
            keystream = key
        print("The Keystream is:"+keystream)
    pt = []
    for j in plaintext:
        if ord(j) in range(65,91):
            pt.append(ord(j))
        else:
            print("ERROR: Enter only Capital letters")
    print("ASCII Values of character in plaintext:",pt)
    keylist = []
    for k in keystream:
        if ord(k) in range(65,91):
            keylist.append(ord(k))
        else:
            print("ERROR: Enter only Capital letters")
    print("ASCII Values of character in keystream:",keylist)
    trans = []
    for i in range(0,len(keylist)):
        ele = (pt[i]+keylist[i])%26
        if ele > 25:
            ele = ele - 26
            trans.append(ele)
        else:
            trans.append(ele)        
    print("ASCII values of each character in Cipher text:",trans,"\n")
    result = []
    for i in trans:
        for j in list1:
            if i == list1.index(j):
                result.append(list1[i])
    print(result)
    cipher = "".join(result)
    print("Cipher Text:"+cipher)
 
elif ord(choice.upper()) == 68:
    ciphertext = input("Enter Cipher Text to be converted into Plain text:")
    key = input("Enter key:")
    keystream = ""
    if len(key)> len(ciphertext):
        print("ERROR: Enter Key as of equal or of less length of cipher text")
    else:
        for i in range(0,len(ciphertext)-len(key)):
            key = key+key[i]
            keystream = key
        print("The Keystream is:"+keystream)
    
    ct = []
    for j in ciphertext:
        if ord(j) in range(65,91):
            ct.append(ord(j))
        else:
            print("ERROR: Enter only Capital letters")
    print("ASCII Values of character in ciphertext:",ct)
    
    keylist = []
    for k in keystream:
        if ord(k) in range(65,91):
            keylist.append(ord(k))
        else:
            print("ERROR: Enter only Capital letters")
    print("ASCII Values of character in keystream:",keylist)
    
    trans = []
    for i in range(0,len(keylist)):
        ele = (ct[i]-keylist[i])%26
        if ele < 0:
            ele = ele + 26
            trans.append(ele)
        else:
            trans.append(ele)        
    print("ASCII values of each character in Plain text:",trans,"\n")
    result = []
    for i in trans:
        for j in list1:
            if i == list1.index(j):
                result.append(list1[i])
    print(result)
    plain = "".join(result)
    print("Plain Text:"+plain)

elif ord(choice.upper()) != 68 or 69:
    print("ERROR: Enter Options as E/e for Encryption or D/d for Decryption")