while True:
    kelime = input("Write something to check for if it is an isogram: ")
    kelime = kelime.lower()

    def is_isogram(kelime):
        for char in kelime:
            if kelime.count(char) >1:
                print(char, "occurs multiple times")
                return False
            
        return True

    print(is_isogram(kelime))
