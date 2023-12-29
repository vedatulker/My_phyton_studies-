pi = 3.14
print(type(pi))
a = str(pi)
print(type(a))

x =  39
y = 25.42
v = "25"
z = "I am "
print(x - int(y))
print(x +float(v ))
print(f"{z} {str(x)} years old.")
print(z + str(x) )

print(20 % 3)
print(25 // 3)

a = 5  # 20 olacak
b = 20  # 5 olacak
temp = a
a = b
b = temp
print(a, b)


x = 15  # 42
y = 42  # 15
number = x
x = y
y = number
print(x ,y)

# Üçgenin Alanı:
a = 10
h = 15 
area = a*(h/2)
print("Ucgen'in alanı:",area )

#hipotenüs
x = int(input('Please enter number_1: '))
y = int(input('Please enter number_2: '))

z = (x**2 + y**2)**0.5
print(f"Ucgen'in hipotenüsü: {z}")

#Daire ni alanı:
pi = 3.14
r = int(input('Lütfen daireninin yarıçapını giriniz: '))
alan = pi*(r**2)
print(f"Daire'nin alanı: {alan} dır.")
