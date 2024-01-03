a = 10
b = 12
print("A") if a > b  else print("B") 

set1 = set("TWELVE PLUS ONE")
set2 = set("ELEVEN PLUS TWO")

print("We are the same") if set1 == set2 else print("We are not same")

set3 = set("TWELVE PLUS ONE")
set4 = set("ELEVEN PLUS THREE")
print('we are same') if set3 == set4 else print("we are not same")

answer = input("Please write Yes or No: ")
if answer == 'yes':
    print(f"You entered True")
else:
    print(f"You entered False")

sayı = int(input("Please enter a number: "))

if sayı % 2 == 0:
    print(f"{sayı} is even.")
else:
    print(f"{sayı} is odd.")

sayı = int(input("Please enter a number: "))
if sayı >= 0:
    print("{0} is positive".format(sayı))
else:
    print("{0} is negative".format(sayı))

sayı1 = int(input("Please enter first number: "))
sayı2 = int(input("Please enter second number: "))
if sayı1 > sayı2:
    print("{0} is The large number ".format(sayı1))
else:
    print(f"The large number is {sayı2}")


