print("Kalvakota Rohith")
choice = input("Do you want to perform Encryption(E) or Decryption(D)?")
word = input("Enter word to be converted:")
key = int(input("Enter the key:"))
print("\n")

list1=[]
for ch in word:
    if ord(ch) in range(65,90):
        list1.append(ord(ch))
    elif ord(ch)<65 or ord(ch)>90 or ord(ch)<97 or ord(ch)>122:
        list1.append(ord(ch))
newlist = list1
print("ASCII values of each character in plan text:",newlist,"\n")

trans = []
if choice.upper() == "E":
    for char in newlist:
        if char in range(65,91):
            ele = ((((char-65)+key)%26)+65)
            if ele > 90:
                ele = ele - 26
                trans.append(ele)
            else:
                trans.append(ele)
        elif char in range(97,123):
            ele = ((((char-97)+key)%26)+97)
            if ele > 122:
                ele = ele - 26
                trans.append(ele)
            else:
                trans.append(ele)
        elif char<65 or char>90 or char<97 or char>122:
            trans.append(char)
elif choice.upper() == "D":
    for char in newlist:
        if char in range(65,91):
            ele = ((((char-65)-key)%26)+65)
            if ele < 65:
                ele = ele + 26
                trans.append(ele)
            else:
                trans.append(ele)
        elif char in range(97,123):
            ele = ((((char-97)-key)%26)+97)
            if ele < 97:
                ele = ele + 26
                trans.append(ele)
            else:
                trans.append(ele)
        elif char<65 or char>90 or char<97 or char>122 :
            trans.append(char)
else:
    print("Enter Option As E or D!!!")
print("ASCII values of each character in Cipher text:",trans,"\n")

result=[]
for value in trans:
    if value == " ":
        result.append(" ")
    else:
        result.append("".join(chr(value)))
print("Characters which will form Cipher String:",result,"\n")

final=""
for ch in result:
    final += ch
print("The Converted Cipher Text:",final)