count = 0
with open('Day4_input.txt', encoding='utf8') as f:
  for line in f:
    elf1Start, elf1End, elf2Start, elf2End = tuple(map(int, line.strip().replace('-',',').split(',')))
    print(elf1Start, elf1End, elf2Start, elf2End)
    elf1 = set(range(elf1Start, elf1End+1))
    elf2 = set(range(elf2Start, elf2End+1))
    count += 1 if (elf1.issubset(elf2)) else 0
    count += 1 if (elf2.issubset(elf1) and elf1 != elf2) else 0
    print(count)