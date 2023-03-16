fhand = open("song.txt")
words = []
for line in fhand:
    line = line.rstrip()
    
print(words)
fhand.close()