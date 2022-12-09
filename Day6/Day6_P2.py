markerSize = 14
with open('Day6_input.txt', encoding='utf8') as f:
  stream = f.readline();
  for x in range(len(stream)-markerSize):
    if (len(set(stream[x:x+markerSize])) == markerSize):
      print(x+markerSize, stream[x:x+markerSize])
      break;