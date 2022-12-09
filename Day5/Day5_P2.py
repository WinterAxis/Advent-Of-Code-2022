# input modified to add 1st part added below
stacks = [[],["D", "T", "W", "N", "L"],["H", "P", "C"],["J", "M", "G", "D", "N", "H", "P", "W"],["L", "Q", "T", "N", "S", "W", "C"],["N","C","H","P"],["B","Q","W","M","D","N","H","T"],["L","S","G","J","R","B","M"],["T","R","B","V","G","W","N","Z"],["L","P","N","D","G","W"]]
with open('Day5_input.txt', encoding='utf8') as f:
  for l in f:
    nums = [int(x) for x in l.split()]
    claw = []
    for _ in range(nums[0]):
      claw.append(stacks[nums[1]].pop(0))
    for _ in range(nums[0]):
      stacks[nums[2]].insert(0, claw.pop())
for stack in stacks[1:]:
  print(stack[0], end="")
