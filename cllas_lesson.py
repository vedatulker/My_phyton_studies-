class Ucus():
    havayolu = 'THY'

ucus1 = Ucus()
print(ucus1.havayolu)

class Ucus():
  havayolu = 'THY'

  def  __init__(self, kod,kalkış, varış, süre, kapasite, yolcu):
    self.kod = kod
    self.kalkış = kalkış
    self.varış = varış
    self.süre = süre
    self.kapasite = kapasite
    self.yolcu = yolcu

ucus2 = Ucus('TK123', 'BRS', 'ANK', 55, 180, 150)
print(ucus2.kod)
print(ucus2.kalkış)


class Ucus():
  havayolu = 'THY'

  def  __init__(self, kod,kalkış, varış, süre, kapasite, yolcu):
    self.kod = kod
    self.kalkış = kalkış
    self.varış = varış
    self.süre = süre
    self.kapasite = kapasite
    self.yolcu = yolcu
  
  def anons_yap(self):
    print(f"{self.kod}, sefer sayılı uçağımız {self.kalkış} dan {self.varış} a {self.süre} dakika sürecektir.")

ucus3 = Ucus('TK54', 'USA', 'IST', 240, 220, 150)
ucus3.anons_yap()

class Person():
  sube = '3/C'

  def __init__(self, name, surname, age, interest_in):
    self.name = name
    self.surname = surname
    self.age = age
    self.interest_in = interest_in

p1 = Person('Vedat', 'Ulker', 41, 'IT')
print(p1.name)
print(p1.age)
print(p1.surname)

