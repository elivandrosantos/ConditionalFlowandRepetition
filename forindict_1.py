credit = {'123': 750, '456': 812, '789': 980}

for key in credit.keys():
  print(key)
  print(credit[key])
  print(f'PFor the document {key}, the credit score value is {credit[key]}.')
  print('\n')
