number = [360, 553, 195, 13, 519, 33, 135]

for numbers in number:

  if numbers % 2 == 0:
    print(f"The number {numbers} it's pair")
    break
  else:
    continue
    print(f"The number {numbers} is odd")
