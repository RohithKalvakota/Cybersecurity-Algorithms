print("Kalvakota Rohith")
choice = input("Do you want to perform Encryption or Decryption?")

if choice.upper() == "E":
    cipher = "" 
    word = input("Enter plain text for Encryption:")
    for ch in word:
        ascii = ord(ch)
        if ascii in range(65,91):
            flag = ascii - 65
            flag = 25 - flag
            ascii = flag + 65
            character = chr(ascii)
            
        elif ascii in range(97,123):
            flag = ascii - 97
            flag = 25 - flag
            ascii = flag + 97
            character = chr(ascii)
        
        elif ascii<65 or ascii>90 or ascii <97 or ascii>122:
            character = chr(ascii)
        cipher += character
        
    print(cipher)
    
elif choice.upper() == "D":
    plain = ""
    word = input("Enter cipher text for Decryption:")
    for ch in word:
        ascii = ord(ch)
        if ascii in range(65,91):
            flag = ascii - 65
            flag = 25 - flag
            ascii = flag + 65
            character = chr(ascii)
            
        elif ascii in range(97,123):
            flag = ascii - 97
            flag = 25 - flag
            ascii = flag + 97
            character = chr(ascii)
        
        elif ascii<65 or ascii>90 or ascii <97 or ascii>122:
            character = chr(ascii)
        plain += character
        
    print(plain)

elif choice.upper() != "E" or choice.upper() != "D":
    print("!!!!! Enter Input as E for Encryption or as D for Decryption !!!!!")
    
