name = 'Elivandro Santos'
age = 40

try:
    presentation = 'Hey guys, my name is' + name + 'i have' + age + 'years'
    print(presentation)
except TypeError:
    age = str(age)
    print('Second chance')
    presentation = 'Hey guys, my name is ' + name + ' i have ' + age + ' years'
    print(presentation)
