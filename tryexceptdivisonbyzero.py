price = 132.85
people = 0

try:
  value_per_people = price / people
  print(value_per_people)
except ZeroDivisionError:
  print('Invalid number of people. A value greater than 0 is expected and a value equal to ' + str(pessoas))
