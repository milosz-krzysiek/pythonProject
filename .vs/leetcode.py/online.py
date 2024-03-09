lista = ["szerszeń", "zjadł", "kota", "margharite", "szcypiorek", "zupcia dyniowa jest am am"]
lizak = []
min = len(lista[0])
min_indeks = 0


for słowo in lista:
   długość = len(słowo)
   if długość < min:
      min = długość

#    print(len(słowo))
print(min, min_indeks)