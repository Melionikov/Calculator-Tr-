def pangram(eng):
    if len(set("abcdefghijklmnopqrstuvwxyz") - set(eng.lower())) == 0:
        return True
    else:
        return False

a = str(input("Write to check if your sentence is a pangram: "))

if pangram(a):
    print("This sentence is a pangram")

else:
    print("This sentence isn't a pangram")
