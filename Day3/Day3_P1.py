answer = 0
with open('Day3_input.txt', encoding='utf8') as f:
  for line in f:
    l1, l2 = line[:len(line)//2], line[len(line)//2:] 
    a=list(set(l1)&set(l2))
    n = ord(a[0])
    if 96 < n < 123:
      n = n- 96
    else:
      n = n-64+26
    print(a[0], n)
    answer += n
print(answer)
    