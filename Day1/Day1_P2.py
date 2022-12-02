totals = []
with open('Day1_input.txt', encoding='utf8') as f:
  for list in f.read().strip().split('\n\n'):
    totals.append(sum([int(item) for item in list.split("\n")]))
totals.sort(reverse=True)
print(sum(totals[0:3]))