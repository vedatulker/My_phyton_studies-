print("Hello World")
def karesini_al(x):
    print(x**2)

karesini_al(5)
sayılar = [1, 2, 3, 4, 5, 6]
list(map(karesini_al, sayılar))

def my_func(a):
    print(len(a))

my_func('asim')
[*map(my_func, ('Ahmet', 'Ali', 'Hanim'))]

def cift_sayi(b):
    print(b) if b % 2 == 0 else None

b = list(range(20)) 
[*filter(cift_sayi, b)]    

x = lambda a : a + 100
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))


q = lambda a : a**2
print(q(10))

numbers = list(range(11))
k = [*map(lambda a : a**2, numbers)]
print(k)

e = list(map(lambda a : a + 10, numbers))
print(e)

h = list(filter(lambda a : a%2==0, numbers))
print(h)

