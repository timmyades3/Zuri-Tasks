 
# [assignment] add your code here 
with open("zuri assignment/./story.txt", "r") as f:
  print(f.readline())
  print(f.readline())
  print(f.readline())


try:
    fhand = open("zuri assignment/./story.txt")
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts)
except:
    print('File cannot be opened:', error)

  
