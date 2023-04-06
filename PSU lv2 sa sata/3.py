import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")

imgbr = img*3 #brigtness++
plt.subplot(3,3,2)
plt.imshow(imgbr,cmap='gray')

img = img[:,:,0].copy()
plt.subplot(3,3,1)
plt.imshow(img, cmap='gray') 





(height, width) = img.shape
img_rot=np.zeros((width,height))

for i in range(0,height):
    img_rot[:,height-1-i]=img[i,:]       



plt.subplot(3,3,3)
plt.imshow(img_rot, cmap='gray')

#zrcaljenje
img_zrc=np.zeros((height,width))
for i in range(0,height):
    img_zrc[height-1-i,:]=img[i,:]


plt.subplot(3,3,4)
plt.imshow(img_zrc, cmap='gray')



print("Slika prije smanjenja: ", img.shape)
img = img[::10,::10] #rezolucija
plt.subplot(3,3,5)
plt.imshow(img, cmap='gray')
print("Slika nakon smanjenja dim: ", img.shape)

# prikazati samo drugu četvrtinu slike po širini, a prikazati sliku
# cijelu po visini; ostali dijelovi slike trebaju biti crni.


visina,sirina= img.shape
img[:,:sirina//4]=0
img[:,sirina//2:]=0


plt.subplot(3,3,6)
plt.imshow(img, cmap='gray')
plt.show()
