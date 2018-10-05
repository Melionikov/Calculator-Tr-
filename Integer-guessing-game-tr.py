import random

x = 0

y = 3

a = (random.randint(0,10))

while True:

    print("Rastgele bir sayı söyle ama 0 ile 10 arasında olsun.")
    
    try:
        b = int(input())
    except ValueError:
        print("Lütfen sayı gir.")
        continue

    if b < 0 or b > 10:
        print("Çok büyük veya küçük sayı girdin.")
        continue

    if a == b:
        print("Doğru bildin!")
        x = x + 1
        print("Puanın:")
        print(x)
        y = 3
        print("Hakların tekrar 3 oldu!")
        
    elif b > a:
        print("Maalesef yanlış yaptın. \nYazdığın sayı biraz büyük.")
        print("Puanın:")
        print(x)
        y = y - 1
        print("Hakkın:")
        print(y)
        
    elif b < a:
        print("Maalesef yanlış yaptın. \nYazdığın sayı biraz küçük.")
        print("Puanın:")
        print(x)
        y = y - 1
        print("Hakkın:")
        print(y)
        
    if y == 0:
        print("Hakkın bitti! \nPuanın sıfırlandı.")
        x = 0
        y = 3
        cevap1 = input("Tekrar oynamak ister misin?")
        if cevap1 == "Evet" or cevap1 == "evet":
            a = (random.randint(0,10))
            continue
        elif cevap1 == "Hayır" or cevap1 == "hayır":
            break
        elif cevap1 != "Evet" and cevap1 != "Hayır" and cevap1 != "evet" and cevap1 != "hayır":
            print("Evet ya da hayır yaz.")
            break
        
    print("Evet? Hayır?")
    cevap = input("Bu kadar yeter mi?   ")

    if cevap == "Evet" or cevap == "evet":
        break
        
    if cevap != "Evet" and cevap != "Hayır" and cevap != "evet" and cevap != "hayır":
        print("Evet ya da hayır yaz.")
        break
