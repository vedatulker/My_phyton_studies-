# Dictionary
empty_dict = {}
my_dict = dict() 

my_dict = {"name" : "vedat", 
           "surname" : "ulker",
            "age" : "42",}
print(my_dict)
my_dict["educated"] = "Chemistry"
print(my_dict)

grocer1 = {"fruit" : "apple",
           "drink" : "water"}
grocer2 = dict(fruit = "orange",
               drink = "water")
print(grocer1)
print(grocer2)

state_capital = {"Arkansas": "LIttle Rock",
                 "Colorado": "Denver",
                 "Califonia":"Sacramento",
                 "Georgia": "Atlanta"}
print(state_capital["Arkansas"])
print(state_capital['Califonia'])
state_capital['Turkey'] = "Ankara"
print(state_capital)
state_capital["Bursa"] = "Yıldırm"
print(state_capital)

my_dict1 = dict(animal = ('lion', 'cat'), planet = 'Moon', number = 40) 
print(my_dict1)
print(my_dict.items(), "\n")
print(my_dict.keys(), "\n")
print(my_dict.values(), "\n")
print(my_dict.update({"year" : 2023}))
print(my_dict)
print(my_dict1.update({"age" : 20}))
print(my_dict1)
del my_dict1["planet"] 
print(my_dict1)
del my_dict["age"]
print(my_dict)
del state_capital["Bursa"]
print(state_capital)
state_capital.pop("Arkansas")
print(state_capital)
print(state_capital.get("Turkey"))
grocer1 = {"fruit" : "apple",
           "drink" : "water"}
grocer1['vegetable'] = "brokoli"
print(grocer1)
grocer1.update({"meal" : "eat"})
print(grocer1)
print(list(grocer1.keys()))
print(list(grocer1.values()))
print(list(grocer1.items()))
grocer1["drink"] = "orange juise"
print(grocer1)
grocer1 = {'fruit': 'apple', 
           'drink': 'orange juise', 
           'vegetable': 'brokoli', 
           'meal': 'eat'}

if "fruit" in grocer1:
    print("Yes, 'fruit' i one of the order.")
print('meal' in grocer1)
print('meat' in grocer1)
print("vete" not in grocer1)
print('drink' in grocer1)
print('fruit' not in grocer1)

print(grocer1)

for i in grocer1:
    print(i)

for i in grocer1.values():
    print(i)


for i in grocer1.items():
    print(i)

for x, y in grocer1.items():
    print(x, y, sep=':')

myfamily = {
  "child1" : {
            "name" : "Emil",
            "year" : 2004
            },
  "child2" : {
            "name" : "Tobias",
            "year" : 2007
            },
  "child3" : {
            "name" : "Linus",
            "year" : 2011
             }
            }

print(myfamily)
print(myfamily['child1']['name'])
print(myfamily['child2']['name'])
print(myfamily['child3']['name'])

school_records = {
    'personal_info':
        {'kid':{'tom':{'class':'intermediate', 'age':10},
                'sue':{'class':'elemantary', 'age':8}
               },
         'teen':{'joseph': {'class':'college', 'age':19},
                 'marry': {'class':'high school', 'age':16}
                },
        },
    'grades_info':
        {'kid':{'tom':{'math':88, 'speech':69},
                'sue':{'math':90, 'speech':81}
               },
         'teen':{'joseph':{'coding':80, 'math':89},
                 'marry':{'coding':70, 'math':96}
                },
        }
}


print(f"Grade of Joseph: {school_records['grades_info']['teen']['joseph']}")
print(f"Grade of Joseph: {list(school_records['grades_info']['teen']['joseph'])}")

print(grocer1.clear())
print(grocer1)

# set, {}, set()
empty_set = set()
my_set = {1, 2, 3.14, (4, 5, 48), False}
print(my_set)

my_set = {1, 2, 2, 3, 5, 3.14, (4, 5, 48), False}
print(my_set)
print(list(my_set))
my_set.add(358)
print(my_set)
my_set.add((2, 3, 6))
print(my_set)

text = 'Vedattt Ulkerrrr'
a = set(text)
print(list(text))
print(tuple(text))
print(set(text))

text = 'Vedattt Ulkerrrr'
text1 = 'Sedatt Tekkii'

b = set(text1)
print(a.intersection(b))  # a & b
print(a.union(b))  # a | b
print(a.difference(b))  # a - b

a = set('01/01/2024')
b = {'01/01/2024'}
print(a, b)

c1 = set('Washinghton')
c2 = set('Istanbul')
print(c1 | c2)
print(c1 & c2)
print(c1 - c2)


