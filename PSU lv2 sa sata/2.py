import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt(open ("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows = 1)
plt.figure("zad 2")
plt.title("Ovisnost potrosnje automobila mpg o hp")
plt.ylabel("MPG")
plt.xlabel("HP")
print(data)

x=np.array(data [:,0])
y=np.array(data [:,3])
wt = np.array(data [:,5])
print(x)
print(y)
print("")
print("min MPG: ", np.min(x))
print("max MPG: ", np.max(x))
print("avg MPG: ", np.mean(x))

print("")
print("automobili sa 6 cilindra: ")

idx=data[:,1]==6
data=data[idx,:]
x6=data[:,0]
print(data)


print("6 CYL min MPG: ", np.min(x6))
print("6 CYL max MPG: ", np.max(x6))
print("6 CYL avg MPG: ", np.mean(x6))

print("")
plt.scatter(x,y, marker='.', s=wt*200)
for i, txt in enumerate(wt):
    plt.annotate(txt, ( x[i],y[i] ))
plt.show()
