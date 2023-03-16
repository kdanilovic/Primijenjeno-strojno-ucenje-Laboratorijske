
def total_euro(rsati, placen):
    ukupno = rsati*placen
    return ukupno


rsati = int(input("Unos radnih sati: "))
placen = float(input("Unesite koliko ste placeni po satu: "))


print("Radni sati: ", rsati, " h")
print("eura/h: ", placen)
print("Ukupno", total_euro(rsati, placen), " eura")
