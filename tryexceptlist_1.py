years = [2019, 2020, 2021]

try:
  current_year = years[3]
  print(current_year)
except Exception as exc:
  print('Exception description: ' + str(exc))
  print('Exception type: ' + str(type(exc)))
  print('List of years is less than the chosen value. A value between 0 and 0 is expected. ' + str(len(anos) - 1))
