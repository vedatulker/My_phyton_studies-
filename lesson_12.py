print('hello')
def who(first, last):
    print("First name is: ", first)
    print("Last name is: ",last)

who('Ali', 'Kaya')  #positional
who('Ahmet', 'Selim')

a = 'I'
b = 'love'
c = 'you'
def texter(c, a, b):
    print(a, b, c)

texter('you', 'I', 'love')
texter(c, a, b)

who(first = 'Hasan', last = 'Kaplan')  # kwargs

def texter(text1, text2, text3):
    print(f"{text2} {text3} {text1}")

texter(text1= 'you', text2= 'I', text3= 'love')

def introduce(name = 'Ali', age = 25, city = 'Çorum'):
    print(f"My name is {name}\n",
        f"I am {age} years old.\n",
        f"I am from {city}")
    
introduce()
introduce(name = 'Veli')
introduce(name = 'Semih', age = 9)
introduce(name = 'Semih', age = 9, city = 'Şırnak')

def city(capital, country = 'Turkey'):
    print(capital, 'in', country)

city('Ankara')
city('Bursa', 'Ankara')
city('Cape Town', 'Africa')
city('Hakkari', country = 'Irak')

def form(name, e_mail, tel, address, city, country = 'Turkey'):
    print(f"Name : {name}\n",
        f"e_mail: {e_mail}\n",
        f"tel : {tel}\n"
        f"address : {address}\n",
        f"city : {city}\n",
        f"country : {country}")

form('Ali', 'vedatsek@', '+90542445225', 'eflak cad.', 'Bursa', 'Turkey')

def cities(city1, city2):
    print('I want to move from', city1, 'to', city2)

cities('Bursa', 'Medine')
cities('Ankara', 'Africa')

def my_function(*city):
    print('cities where ı want to live:')
    for i in city:
        print('-', i)

my_function('Ankara', 'Bursa')

def meyveler(*meyve):
    print('I want to get : ')
    for i in meyve:
        print('*', i)

meyveler('elma', 'armut', 'muz', 'kavun')

list_evens = []
list_odds = []

def slicer(*numbers):
    for i in numbers:
        if i % 2 == 0:
            list_odds.append(i)
        else:
            list_evens.append(i)
    print('evens number: ',list_evens)
    print('odds number: ',list_odds)

slicer(1, 2, 3, 4, 5 , 6, 7, 8, 9)
print('-'*30)
slicer(15, 18, 22, 46, 54, 67, 82, 102)


c = 0
for s in "istihza":
    c += 1
print(c)

def karakter_sayısı(a):
    c = 0
    for i in a:
        c += 1
    print(c)

karakter_sayısı('Kahramanmaraş')

def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

    print("-"*30)

kayıt_oluştur('Ali', 'Kaya', 'w10', 'Bursa')

print("-"*30)

def kur(kurulum_dizini="/usr/bin/"):
    print("Program {} dizinine kuruldu!".format(kurulum_dizini))

kur()
kur('C/vd/scc/lile')

def kur(kurulum_dizini=''):
    if not kurulum_dizini:
        print("Lütfen programı hangi dizine kurmak istediğinizi belirtin!")
    else:
        print("Program {} dizinine kuruldu!".format(kurulum_dizini))
kur()
kur('C//dya')

def fonksiyon(*args):
    print(args)

fonksiyon(1, 2, 3, 4, 5)

print('-'*30)

def çarpma(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    print(sonuc)

çarpma(1, 2, 3, 4, 5, 6)

total = 1
for i in range(1, 6):
    total *= i
print(total)

def city(*args):
    print(args)

city('Ankara', 'Bolu', 'kars')
print('-'*30)

def katilim(**kisiler):
    print(kisiler)

katilim(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")




