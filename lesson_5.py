city = '   Kahramanmaraş   '
print(city.strip())
city = 'Hakkari'
x = city.strip('k')
print(x)
y = city.strip('ari')
print(y)
print(city.strip('ak'))
print(city.strip('Hak'))
city1 = ' Ankaragücü    '
a = city1.strip()
print(a.strip('cü'))
print(len(city1))
print(len(a))

txt = 'welcome to hospital in my town'
print(txt.split())
a = txt.split()
for i in a:
    print(i)

address = 'my toen near street on the boxet nex tı hope'
print(address.title())
print(address.split())
print(address[::2])
print(address.replace('on', 'and'))

sayı = '123545'
print(sayı.isdigit())

 
text = 'tyou can learn almost everything in pre-classz'
print(text.strip('tz').upper())

# list
list_1 = [1, 2, 3, 4, 5]
word = 'angry'
list_2 = list(word)
print(list_1)
print(list_2)
name = 'Abdullah'
z = list(name)
print(z)
print(list(range(10)))

my_list = ['ali', 'veli', 2020]
new_list =  list(my_list)
new_list2 = [new_list]
print(new_list)
print(new_list2)
print(len(new_list))
print(len(new_list2))

year = "2023's perfect"
new = list(year)
print(new)
print(len(new))
new2 = [year]
print(new2)

city = ['Addis', 'Konya', 'Ankara', 'Corum', 'Hakkari']
print(len(city))
print(city[0::2])
print(city[2])
print(len(city[2:3]))
a = city[2:3]
name = 'Ali bugün okula gelmedei'
print(name.split())
print(list(name))
name2 =  name.split()
print(name2)
print(name2[-4:-1])
print(name2[2:3])
print(type(name2))
name2.append('veli')
print(name2)

listem = [1, 2, 3, 4]
listem.append(5)
print(listem)
city = ['Addis', 'Konya', 'Ankara', 'Corum', 'Hakkari']
city.append('Bursa')
print(city)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

empty_list = []
empty_list.append('I')
empty_list.append('love')
empty_list.append('you')
print(empty_list)

empty_list.insert(2, 'her family')
print(empty_list)
city.insert(3, 'Samsun')
print(city)
for i in city:
       if i == 'Corum':
        print('Ben benim memleketim',city[4])
        continue
       print(i)

print(city.index('Samsun'))
# isimi a ile başlayanları sıralama
name_list = ['ali', 'veli', 'ahmet', 'asım', 'vedat']
result_list1 = [name for name in name_list if name.startswith('a')]
result_list2 = [name for name in name_list if name.startswith('v')]
print(result_list1)
print(result_list2)

name_list = ['ali', 'veli', 'ahmet', 'asım', 'vedat']

for name in name_list:
    if name.startswith('a'):
        print(name, end=' ')