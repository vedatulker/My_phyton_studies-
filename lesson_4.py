#string.format()
print("{0} {1} {2} {3}".format('Welcome', 'to', 'your', 'home'))
print("{2} {1} {0} {3}".format('Welcome', 'to', 'your', 'home'))



city = 'Istanbul'
print('a' in city)
print('c' in city)

print(city.endswith('bul'))
print(city.endswith('bulz'))
print(city.startswith('Is'))
print(f"Istanbul kelimesinin ilk 3 harfi:{city.startswith('Ist')} ")
print(f"Istanbul kelimesinin ilk 3 harfi:{city[:3]} ")
print(f"Istanbul kelimesinin hatf sayısı:{len(city)}")
print(f"Istanbul kelimesinde t sarfi sayısı:{city.count('t')} ")
print(f"Istanbul kelimesinde a sarfi sayısı:{city.count('a')} ")

name = input('Please enter your name: ')
print(f"İsminizde geçen harf sayısı: {len(name)}")
print(f"İsminizde geçen  a harfi sayısı: {name.count('a')}")
print(f"İsminizde geçen son  üç harfi sayısı: {name[-3:]}")
print(name.replace('a', '*'))

name = input('Please enter yor name: ')

for i in name:
    print(f"My name is {name.capitalize()}")

metin = 'elma, armut, elma, not, not, elma'
print(metin.replace('elma', 'portakal', 2))
print(metin.replace('elma', 'şeftali'))
print(metin.replace('not', 'hot', 1))