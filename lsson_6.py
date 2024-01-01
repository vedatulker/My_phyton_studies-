#list
city = ['Ankara', "Istanbul", 'Paris', 'London', 'Bursa']
city.append('Çorum')
print(city)
city.insert(1, 'Kars')
print(city)
print(city[1:4])
print(city[2])
print(city.index('Kars'))
print(city.index('Çorum'))

a = city.pop(1)
print(list(a))
print(city)
b = city.remove('Ankara')
print(b)
print(city)
print(city.append('Kars'))
num = list(range(1,5))
print(num)
num.insert(4, 5)
print(num)

del num[3]  # 3 indeksi siler
print(num)

listem = [15, -1, 1, 2, 41, 25, 52, 254, 0, 25, 49]
listem.sort()
print(listem)
listem.sort(reverse=True)
print(listem)
print(listem[0])
listem.sort()
print(listem[0])

listem = [15, -1, 1, 2, 41, 25, 52, 254, 0, 25, 49]
print(sorted(listem))
print(listem)
print(sorted(listem, reverse=True))

listem2 = [15, 12, -4, 36, 42, 458, 1, 0]
listem2.sort()
print(listem2)
listem2.sort(reverse = True)
print(listem2)
print(listem2[0])
listem2 = [15, 12, -4, 36, 42, 458, 1, 0]
print(sorted(listem2))
reveerse_num = sorted(listem2, reverse = True)
print(reveerse_num)
print(reveerse_num[0])
      
b_list = []
b_list.append(listem2)
print(b_list)
print(len(b_list))

print(city)
print(city[0])
new_list = []
new_list.append(city)
print(new_list)
print(new_list[0])
print(new_list[0][1])
print(new_list[0][2])
print(new_list[0][3])
print(new_list[0][2][2])
print(new_list[0][1][0:3])

team = 'Galatasaray'
a = team.center(25, '*')  # center stringle beraber 25 karakter olur ve stringi ortalayıp sağ ve soluna * koyar.
print(a)
new_list = list(range(1, 21))
print(new_list[0:20:2])
x = list(range(1, 10))
print(x[0:10:2])

mix_list = [1, [1, 'one', 2, 'two', 3, 'three'], 4]
print(mix_list[1][1:6:2])

# tuple
my_tuple = ()  # içi boş tuple
my_tuple = tuple()

text = 'evening'
new_list = list(text)
print(new_list)
new_tuple = tuple(text)
print(new_tuple)

print(city)
t = tuple(city)
print(t)
l = list(t)
print(l)
print(city)
x = city[1]
print(tuple(x))
print(x,)

my_tuple = ('solar')
print(my_tuple, type(my_tuple), sep='\n')

solar = 'Earth', 'Moon', 'Mars'
print(type(solar))
solar = ('Earth', 'Moon', 'Mars')
print(type(solar))

name = 'Ali bugün okula gelmedi'
d = name.split()
print(d)
print(type(d))  # list
e = tuple(d)
print(e)
print(type(e))  # tuple
t1 = tuple(range(1, 10))
print(t1)

city_list = ['Tokyo', 'Ankara', 'Bursa', 'Gazze']
city_tuple= tuple(city_list)
print(city_tuple)
print(city_tuple[0])
mix_tuple = ('11', 11, [2,'two', ('six', 6)], (5, 'fair'))
print(mix_tuple[2][2][0])
print(mix_tuple[-2][-1][-2])
print(mix_tuple[3][1])
print(mix_tuple[-1][-1])

x = ' kazım  hartal   '
y =  x.upper().split()[0][0]
z = x.upper().split()[1][0]
print(z)
print(y)
print(y + '.' + z)


name = input('Please enter your name: ')
print(f"İsminizin Başharfleri: {name.upper().split()[0][0]}.{name.upper().split()[1][0]}. ")


