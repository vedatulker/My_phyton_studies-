# kwargs
def animals(**kwargs):
    for key , value in kwargs.items():
        print(value, 'are', key)

animals(Carni = 'lions', OMni = 'Bears', Herbi = 'Deers', Nomniv = 'Human' )

print('-'*30)

def organizer(**kwargs):
    list_names = []
    list_ages = []
    for key, value in kwargs.items():
        list_names.append(key)
        list_ages.append(value)
    print(list_names, list_ages, sep='\n')
        

organizer(Ali= 42, Veli=36, Sadık= 65)
organizer(Osman=36, Selim = 42, Ayşe = 48, Nazlı = 18)

print('-'*30)
def brothers(bro1, bro2, bro3):
    print('The names of brothers: ')
    print(bro1, bro2, bro3, sep='\n')

family = ['Ali', 'veli', 'Sali']
brothers(*family)