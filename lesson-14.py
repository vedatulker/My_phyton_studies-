import random

def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set()

    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))

    return sayılar
  
print(sayı_üret())
print(*sayı_üret(0, 100, 10), sep='-')

isim_listesi = []

def fonk():  # hata verir.
    isim_listesi += ['Fırat Özgül', 'Orçun Kunek']
    return isim_listesi

print(fonk())

isim = 'Fırat'

def fonk():
    global isim
    isim += ' Özgül'
    return isim

print(fonk())