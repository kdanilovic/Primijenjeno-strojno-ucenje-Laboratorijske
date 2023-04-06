import numpy as np
import matplotlib.pyplot as plt

def stvori_polje(vel_kv, br_kv_v, br_kv_s):

    

    crni_kv = np.zeros((vel_kv,vel_kv,3), dtype=np.uint8)
    crni_kv[:,:,:1]=255
    bijeli_kv=np.zeros((vel_kv,vel_kv,3), dtype=np.uint8)
    bijeli_kv[:,:,2]=255


    red1 = np.hstack([crni_kv, bijeli_kv] * int(br_kv_s / 2))
    red2 = np.hstack( [bijeli_kv,crni_kv] * int(br_kv_s/2) )

    polje=np.vstack( [red1,red2] * int(br_kv_v/2) )

    if br_kv_v % 2 == 1:
        zadnji_red = np.hstack([crni_kv, bijeli_kv] * int(br_kv_s/2))
        polje=np.vstack([polje,zadnji_red])

    if br_kv_s %2 ==1:
        zadnji_stupac = np.vstack( [crni_kv, bijeli_kv] * int(br_kv_v/2) )
        polje=np.hstack([polje,zadnji_stupac])

    return polje



vk = int(input("Unos velicine kvadrata u pikselima: "))
brkv_v=int(input("Unos broja kvadrata po visini: "))
brkv_s=int(input("Unos broja kvadrata po sirini: "))



img = stvori_polje(vk,brkv_v,brkv_s)
plt.imshow(img, vmin=0, vmax=255)
plt.show()
