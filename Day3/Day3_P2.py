answer = 0
with open('Day3_input.txt', encoding='utf8') as f:
  for line in f:
    l1 = line.strip()
    l2 = f.readline().strip()
    l3 = f.readline().strip()
    a=list(set(l1)&set(l2)&set(l3))
    n = ord(a[0])
    if 96 < n < 123:
      n = n- 96
    else:
      n = n-64+26
    print(a[0], n)
    answer += n
print(answer)
    