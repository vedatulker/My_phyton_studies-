def my_fuction():
    print('Hello')

my_fuction()

def pozitif_sayi(sayi):
    return sayi > 0

liste = [-2, -1, 0, 1, 2, 3, 4]

filtrelenmis_liste = list(filter(pozitif_sayi, liste))

print(filtrelenmis_liste)

#filter
def odd_number(a):
    return a % 2 ==0

numbers = list(range(1,33))
print(list(filter(odd_number, numbers)))

def negative_num(a):
    return a < 0

numbers_1 = list(range(-5, 35))
print(list(filter(negative_num, numbers_1)))

def adult(b):
    return b >= 18

ages = [ 5, 12, 18, 21, 36, 42 ,17]
print(list(filter(adult, ages)))

x = ('apple', 'orrange', 'banana')
print(list(enumerate(x)))
print(list(enumerate(x, 10)))

numbers= [3, 5, 28]
print(sum(numbers))
print(sum(numbers, 10))

def toplam(a, b):
    print(a + b)

toplam(15,35)

def kareal(a, b):
    print(a**2 + b**2)
 
kareal(2, 4)


def calculator(num1, num2, opr):
    if opr == '+':
        print(num1 + num2)
    elif opr == '*':
        print(num1 * num2)
    elif opr == '-':
        print(num1 - num2)
    elif opr == '/':
        print(num1 / num2)
    else:
        print("enter valid argument")


calculator(88, 22, '+')
calculator(88, 11, '-')
calculator(15 ,5, '/')
calculator(8, 2, '*')




