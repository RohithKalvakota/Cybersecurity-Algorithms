
print("Kalvakota Rohith")
print("Enter 3 keys")
keys = []
for n in range(0,3):
    ele = int(input("Enter key:"))
    keys.append(ele)
print("The Keys are:",keys)
choice = input("Do you want to perform Encryption(E) or Decryption(D)?")
word = input("Enter word to be converted:")

list1 = []
for i in word:
    if ord(i) in range(65,91):
        list1.append(ord(i))
    elif ord(i) in range(97,123):
        list1.append(ord(i))
    elif ord(i)<65 or ord(i)>90 or ord(i)<97 or ord(i)>122:
        list1.append(ord(i))
newlist = list1
print("ASCII values of each character in plan text:",newlist,"\n")

trans = []

if choice.upper() == "E":
    for char in newlist:
        if char in range(65,91):
            if newlist.index(char)%3 == 0:
                ele = ((((char-65)+keys[0])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-65)+keys[1])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-65)+keys[2])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
        elif char in range(97,123):
            if newlist.index(char)%3 == 0:
                ele = ((((char-97)+keys[0])%26)+97)
                if ele > 122:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-97)+keys[1])%26)+97)
                if ele > 122:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-97)+keys[2])%26)+97)
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
            if newlist.index(char)%3 == 0:
                ele = ((((char-65)-keys[0])%26)+65)
                if ele < 65:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-65)-keys[1])%26)+65)
                if ele < 65:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-65)-keys[2])%26)+65)
                if ele < 65:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
        elif char in range(97,123):
            if newlist.index(char)%3 == 0:
                ele = ((((char-97)-keys[0])%26)+97)
                if ele < 97:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-97)-keys[1])%26)+97)
                if ele < 97:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-97)-keys[2])%26)+97)
                if ele < 97:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)              
        elif char<65 or char>90 or char<97 or char>122:
            trans.append(char)

elif choice != "E" or choice != "D" or choice != "e" or choice != "d":
    print("Enter Option As E,e,D or d!!!")

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

