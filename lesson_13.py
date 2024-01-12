# kwargs
def animals(**kwargs):
    for key , value in kwargs.items():
        print(value, 'are', key)

animals(Carni = 'lions', OMni = 'Bears', Herbi = 'Deers', Nomniv = 'Human' )

print('-'*30)

def organizer(**kwargs):
    list_names = []
    list_ages = []
    for key, value in kwargs.items():
        list_names.append(key)
        list_ages.append(value)
    print(list_names, list_ages, sep='\n')
        

organizer(Ali= 42, Veli=36, Sadık= 65)
organizer(Osman=36, Selim = 42, Ayşe = 48, Nazlı = 18)

print('-'*30)
def brothers(bro1, bro2, bro3, bro4):
    print('The names of brothers: ')
    print(bro1, bro2, bro3, bro4, sep='\n')

family = ['Ali', 'veli', 'Sali', 'Kemal']
brothers(*family)
print('-'*30)
family2 = ['Ali', 'veli', 'Sali', 'cafer']
brothers(*family2)
def merger(name1, name2, name3, name4):
    print('For me',name1, name4, 'and', name2, name3, 'are geniuses')

genius = ('Bill', ' Rossum', 'Gido van', 'Gates')
merger(*genius)

def gene(x, y):
    print(x, 'belongs to Generation X')
    print(y, 'belongs to Generation Y')

dict_gene = {'y' : 'Marry', 'x' : 'Balli'}
gene(**dict_gene)

names_friends = {'Ahmet' : 36, 'Mehmet' : 42, 'Cafer' : 56}
def meaner(Ahmet, Mehmet, Cafer):
    avg = (Ahmet + Mehmet + Cafer) // 3
    print('The average of my friends ages is : ', avg)
  
meaner(**names_friends)

def city_population(**cities):
    city_name = []
    city_pop = []
    for key, value in cities.items():
        city_name.append(key)
        city_pop.append(value)
    print(f"City : {city_name}, \nPopulatin : {city_pop}, ")

city_population(Ankara = 20.0000, Paris = 25.000, Londra = 100.000)

import math

print(math.pi)
print(math.factorial(5))

import random
num = random.randint(1,50)
print(num)

import random as rnd
listem = ["Gul", "Papatya","Orkide"]
newer = rnd.choice(listem)
print(newer)

import datetime
print(datetime.date.today())

print(datetime.datetime.today())

def yas_hesapla(dogum_yili, dogum_ayi, dogum_gunu):
  bugun = datetime.today()
  yas = bugun.year - dogum_yili

  if (dogum_ayi, dogum_gunu) < (bugun.month, bugun.day):
    return yas
  else:
    return (yas - 1)

yas_hesapla(1981, 7 ,5)

