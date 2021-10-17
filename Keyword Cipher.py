import sys
def key():
    print("Kalvakota Rohith")
    print("Keyword must contain each letter of A-Z exactly once, no letter should repeat itself")
    keyword = input("Enter keyword: ").upper()
    for i in range(len(keyword)):
        pos = i
        for j in range(len(keyword)):
            if pos == j:
                continue
            elif keyword[i] == keyword[j]:
                print("Letter {} repeating in keyword".format(keyword[i]))
                sys.exit()

    temp = ""
    for i in range(len(keyword)):
        temp += keyword[i]
    for i in range(26):
        temp += chr(i+65)

    alpha_with_key = ""
    for i in range(len(temp)):
        found = False
        for j in range(len(alpha_with_key)):
            if temp[i] == alpha_with_key[j]:
                found = True
                break
    
        if not found:
            alpha_with_key += temp[i]
    return alpha_with_key

def encryption(alpha_key, alpha):
    message = input("Enter message: ").upper()
    encrypted_text = ""
    for i in range(len(message)):
        if message[i] < chr(65) or message[i] > chr(90):
            encrypted_text += message[i]
        else:
            counter = 0
            for j in range(len(alpha)):
                if message[i] == alpha[j]:
                    encrypted_text += alpha_key[counter]
                    break
                else:
                    counter += 1
      
    print("Encrypted Message: {}".format(encrypted_text))

def decryption(alpha_key, alpha):
    message = input("Enter Encrypted Message: ").upper()

    decrypted_text = ""
    for i in range(len(message)):
        if message[i] < chr(65) or message[i] > chr(90):
            decrypted_text += message[i]
        else:
            counter = 0
            for j in range(len(alpha)):
                if message[i] == alpha_key[j]:
                    decrypted_text += alpha[counter]
                    break
                else:
                    counter += 1

    print("Decrypted Text: {}".format(decrypted_text))

def main():

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_key = key()
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        encryption(alpha_key, alpha)

    elif choice == 2:
        print("---Decryption---")
        decryption(alpha_key, alpha)

    else:
        print("Incorrect Choice")

if __name__ == "__main__":
    main()