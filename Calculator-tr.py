while True:

    print("İşlem Türleri: \n1-Toplama \n2-Çıkarma \n3-Çarpma \n4-Bölme \n5-Kuvvet alma   ")

    islem = input("Yapacağınız işlemi seçiniz. ")

    if islem != "1" and islem != "2" and islem != "3" and islem != "4" and islem != "5":
        print("Bilinmeyen işlem   ")
        continue
    
    a = float(input("Birinci sayı: "))
    b = float(input("İkinci sayı: "))
    
    if islem == "1":
        print(a + b)
    
    elif islem == "2":
        print(a - b)
    
    elif islem == "3":
        print(a * b)
    
    elif islem == "4":
        if b != 0:
            print(a / b)
        elif b == 0:
            print("Hiçbir sayı 0 a bölünemez.   ")
        
    elif islem == "5":
        if b == 0 and a == 0:
            print("0'ın 0'ıncı kuvveti alınamaz.   ")
        else:
            try:
                print(a ** b)
            except OverflowError:
                print("Fazla büyük bir sayı çıktı. Bundan dolayı hesaplayamadık ;(   ")
                continue
