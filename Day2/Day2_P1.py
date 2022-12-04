round = 0
score = 0
with open('Day2_input.txt', encoding='utf8') as f:
  for line in f:
    o, p = [ord(x)-64 for x in line.strip().split()]
    p = p-23
    n = o-p
    round = p
    
    if n == 1 or n == -2:
      round += 0
    if n == 2 or n == -1:
      round += 6
    if n == 0:
      round += 3
    print(o, p, n, round)
    score += round
print(score)