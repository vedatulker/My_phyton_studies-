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

listem1

      