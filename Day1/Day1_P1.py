maxTotal = 0
with open('Day1_input.txt', encoding='utf8') as f:
  for list in f.read().strip().split('\n\n'):
    count = sum([int(item) for item in list.split("\n")])
    if count > maxTotal:
      maxTotal = count
print(maxTotal)