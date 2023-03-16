
lista = []
count = 0

while True:

    x = input("Unos broja: ")
    if x == 'Done':
        break
    else:
        if x.isdigit():
            lista.append(x)


lista = [eval(i) for i in lista]
print(lista)
brojac = len(lista)
print("Korisnik je unio: ", brojac, " brojeva")
print("Max vrijednost: ", max(lista))
print("Minimalna vrijednost: ", min(lista))
print("Srednja vrijednost: ", sum(lista)/brojac)
lista.sort()
print("Sortirana lista: ", lista)
