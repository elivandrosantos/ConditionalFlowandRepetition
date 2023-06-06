years = [2019, 2020, 2021]

try:
  current_year = years[10]
  print(current_year)
except IndexError:
  print('List of years is less than the chosen value. A value between 0 and 0 is expected. ' + str(len(anos) - 1))
except Exception as exc:
  print(exc)
  print('Generic Error')
