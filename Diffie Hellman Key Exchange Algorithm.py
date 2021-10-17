print("Kalvakota Rohith")
p = int(input("Enter a modulus:"))
g = int(input("Enter a base:"))
sec1 = int(input("Select secret integer 1:"))
a = (g ** sec1) % p
print(f"First person sends {a} to second person.")
sec2 = int(input("Select secret integer 2:"))
b = (g ** sec2) % p
print(f"Second person sends {b} to first person.\n")
s1 = (b ** sec1) % p
print("Secret for first person:",s1)
s2 = (a ** sec2) % p
print("Secret for second person:",s2,"\n")
if s1 == s2:
    print(f"{s1} is the shared secret.")
else:
    print("The secret is different.")