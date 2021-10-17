print("Kalvakota Rohith")
word = input("Enter Plain Text to be converted into Cipher text:")
key = int(input("Enter Key for Rail Fence(Enter only 3 or 4):"))
list1=[]
for ch in word:
    list1.append(ch)
list2=''
length = len(word)
flag = 0

if key==3:
    while flag<length:
        if flag%4==0:
            list2 += word[flag]
        flag+=1
    flag=0
    while flag<length:
        if flag%2==1:
            list2 += word[flag]
        flag+=1
    flag=0
    while flag<length:    
        if flag%4==2:
            list2 += word[flag]
        flag+=1
    flag=0
    print("The cipher text of the plain text",word,"is:",list2)
    
elif key==4:
    while flag<length:
        if flag%6==0:
            list2 += word[flag]
        flag+=1
    flag=0
    while flag<length:
        if flag%2!=0 and flag%3!=0:
            list2 += word[flag]
        flag+=1
    flag=0
    while flag<length:    
        if flag%2==0 and flag%3!=0:
            list2 += word[flag]
        flag+=1
    flag=0
    while flag<length:    
        if flag%3==0 and flag%6!=0:
            list2 += word[flag]
        flag+=1
    flag=0
    print("The cipher text of the plain text",word,"is:",list2)
    
elif key != 3 or key != 4:
    print("!!!!! Enter Key Input as only 3 or 4 !!!!!")
    



 
 
 
 
 
 
 
 
 