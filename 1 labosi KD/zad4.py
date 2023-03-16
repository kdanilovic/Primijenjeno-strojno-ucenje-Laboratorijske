
ime_datoteke = input("Unos imena datoteke: ")

numberList = []

lista = []
fhand = open(ime_datoteke)
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        print(line)
        line_r = line.rsplit()
        numberList.append(line_r[1])

print(numberList)

numberList = [eval(i) for i in numberList]
average = sum(numberList)/len(numberList)
print("Average X-DSPAM-Confidence: ", average)
fhand.close()

