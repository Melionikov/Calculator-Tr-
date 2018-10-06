a = int(input("How many letters do you want to skip? "))

b = (input("Enter your sentence: "))

b = b.lower()

for char in b:
    c = ord(char)
    if c + a > 122:
        print(chr(c + a - 26),end="")
    elif c + a < 97:
        print(chr(c + a + 26),end="")
    else:
        print(chr(c + a),end="")

print("\n\n") 
