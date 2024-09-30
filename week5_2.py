###########ödev1############3

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

print(liste[3])
print(liste[5])
print(liste[7])
s = slice(2,8,1)
print(liste[s])
s2 = slice(5,8,1)
print(liste[s2])

###############ödev2###########


liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

yeni_liste = []

for indeks in liste:
    if type(indeks) == str:
        yeni_liste.append(indeks)

print(yeni_liste)



##############ödev3############

meyveler = ["elma", "armut", "çilek", "muz"]
enum = enumerate(meyveler)

for index, meyve in enum:
    print(f"{index}. indexte bulunan meyve: {meyve}")