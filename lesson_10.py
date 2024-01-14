# while

number = 0
while number < 6:
    print(number)
    number += 1

i = 1
while i < 6:
    print('Semih')
    if i == 3:
        print('Ekrem')
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
      break
    i += 1

my_list = ["a", "b", "c", "d", "e", "f"]
a = 0
while a < len(my_list):
    print("square of {} is {}".format(a, a**2))
    a += 1

listem = range(0,10)
print(listem)

a = ("Ali", "Veli", "Selim")
b = ("Kamil", "Salih", "Hakkı")

x = zip(a, b)
print(dict(x))

list_1 = [1, 2, 3, 4]
list_2 = ["a", "b","c", "d"]
for x, y in zip(list_1, list_2):
    print(x, ":", y)

list_1 = [1, 2, 3, 4]
list_2 = ["a", "b","c", "d"]
print(dict(zip(list_1, list_2)))

expl_list = [1, 2, 45, 65, 24, 33, 87, 96, 102]
even_num = []
odd_num = []

for i in expl_list:
    if i % 2 == 0:
        odd_num.append(i)
    else:
        even_num.append(i)
    
print(f" even numbers: {even_num}")
print(f" odd numbers: {odd_num}")

expl_list = [1, 2, 45, 65, 24, 33, 87, 96, 102]
even_num = 0
odd_num = 0

for i in expl_list:
    if i % 2 == 0:
        odd_num += 1
    else:
        even_num += 1
print(f"the numbers of even numbers: {even_num}")
print(f"the numbers of odd numbers: {odd_num}")

for i in range(1, 10):
    print(str(i)*i)
    
print('ali'*3)

print(sum(range(1, 75)))

sum = 0
for i in range(1, 75):
    sum += i
print(sum)

sum = 0
for i in range(1, 100):
    sum += i
print(sum)

names= ("Ali", "Veli", "Selim")
nick_name = ("Good", "Better", "Helpful")
for i in names:
    for ii in nick_name:
        print(i, 'is', ii)

# asal sayı
sayi = int(input('Bir sayı giriniz : '))

for i in range(2, sayi):
    if sayi % i == 0:
        print(sayi, 'asal değil')
        break
else:
    print(sayi, 'asaldır')


sayi = 6
sonuc = 1
while sayi > 0:
    sonuc *= sayi
    sayi -= 1
print(sonuc)





        
