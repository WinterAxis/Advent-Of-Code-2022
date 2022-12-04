round = 0
score = 0
with open('Day2_input.txt', encoding='utf8') as f:
  for line in f:
    o, p = [ord(x)-64 for x in line.strip().split()]
    p = p-23
    
    if (p == 1):
      n = o-1
      if n < 1:
        n = 3
      round = 0 + n
    if (p == 2):
      n = o
      round = 3 + n
    if (p == 3):
      n = o+1
      if n > 3:
        n = 1
      round = 6 + n
    
    print(p, o, n, round)
    score += round
print(score)

# A X
# B X
# C X 
# A Y
# B Y
# C Y
# A Z
# B Z
# C Z