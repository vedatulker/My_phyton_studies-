import math  # hazır modüller

sonuc = math.factorial(5)
print(sonuc)
print(math.factorial(6))
print(math.sqrt(36))
print(math.fabs(-5))

from math import factorial  # sadece faktoriyel import ettik
print(math.factorial(6))

from math import sqrt, fabs  # sadece ikisini import ettik
print(math.fabs(-25))

import my_module

sonuc = my_module.cember_cevresi(4)
print(sonuc)

import my_module as my_m  # kısaltma için as kullanılır.
sonuc = my_module.cemberin_alani(5)
print(sonuc)

sonuc = my_module.dikdörtgenin_alanı(30, 40)
print(sonuc)

sonuc = my_module.hypotenüs(30, 40)
print(sonuc)
