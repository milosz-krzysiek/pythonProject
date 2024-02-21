

def poleProstokąta(bok_1, bok_2):
    pole = bok_1 * bok_2
    obwód = 2 * (bok_1 + bok_2)
    print(pole)
    return pole, obwód

poleP, obwódP = poleProstokąta(bok_1 = 3, bok_2 = 4 )

print(poleP, obwódP)