ocjena = 5.0

while ocjena > 1.0 or ocjena < 0.0:
    try:
        ocjena = float(input("Unos ocjene: "))
        if ocjena > 1.0 or ocjena < 0.0:
            print("Broj izvan intervala!")
        if ocjena >= 0.9:
            kategorija = 'A'
        elif ocjena >= 0.8:
            kategorija = 'B'
        elif ocjena >= 0.7:
            kategorija = 'C'
        elif ocjena >= 0.6:
            kategorija = 'D'
        elif ocjena < 0.6:
            kategorija = 'F'
    except:
        print("greska u unosu, nije broj!")

print(ocjena, " : ", kategorija)
