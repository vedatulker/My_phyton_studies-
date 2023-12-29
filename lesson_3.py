name1 = 'Ali'
name2 = 'Veli'
name3 = 'Salih'
print(f"Sınıfın en akıllısı, {name1}\n"
      f"Sınıfın en delisi, {name2}\n"
      f"Sınıfın en yaraması, {name3}")

name1 = 'Ali'
name2 = 'Veli'
name3 = 'Salih'
print(name1, name2, name3, sep='**')

print(True and True and False or True and True and False)
print(bool(0))
print(bool({0}))
print(bool([]))
print(bool('ali'))

print('Ali' and 'Veli' or False and 0 and 28)

name = ['ali', 'vali', 'sali']
a, b, c = name
print(a, b, c)

city = 'Ankara'
print(city[0:5:2])

city = 'Istanbul'
print(city[::-1])
print(city[-5:])
print(city[:-4])
print(city[-6:-3])

print(*city)
print(len(city))

x = 'Sabri '
y = 'topu '
z = 'dışarı attı'
print(x, y, z)
print(x+ y + z)
a = (x + y + z)
print(len(a))
print(a[0:6])
print(f"{x} {y} {z}")

print(z[0:2] + z[2:5] + z[5:10])

print('wee\b \n\tare \n\t\tphyton \n\t\t\tdeveloper')

print(*city, sep='-')
text = "Clarusway,Clarusway,Clarusway, \n\tClarusway, Clarusway, Clarusway, \n\t\tClarusway, Clarusway, Clarusway"
print(text)
print(False and {0} or [])

string1 = 'I am hungry...'
string2 = '1453'
print(*string1, sep='_')
print(string2*3)
print(*string2, sep='-')

s_1 = 'upper'
s_1 += 'case'
print(s_1)
s_1 += 'letter'
print(s_1)
s_1 += 'end'
print(s_1)

#string.format()
print('{name} {yer} {meyve} aldı.'.format(name='Ahmet', yer= 'market ten', meyve= 'armut'))

name = input('please enter your name: ')
print('Welcome to my home :{}'.format(name.upper()))

faculty = input('Please faculty name: ')
student_no = int(input('Pelase enter study_no: '))
name = input('Please enter your name: ')
print('Mr.{}, {} numarası ile {} bölümüne kayıt yaptırınız.'.format(name, student_no, faculty))
print('Mr.{1}, {2} numarası ile {0} bölümüne kayıt yaptırınız.'.format(name, student_no, faculty))
