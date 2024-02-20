# zadanie nr 1
# napisz funkcję, która policzy pole rombu, podane w cm i wywołaj ją

# zalecany output z twojej aplikacji:
# Romb o przekątnych długości: 7cm oraz 8cm ma pole równe 28cm^2

def funkcja():
    policzPoleIŁadnieWyswietl(7, 8)
    return

def policzPoleRombu(przekątna_pierwsza, przekątna_druga):
    pole = (przekątna_pierwsza * przekątna_druga) / 2
    return pole


def policzPoleIŁadnieWyswietl(przekątna_pierwsza, przekątna_druga):
    pole = policzPoleRombu(przekątna_pierwsza, przekątna_druga)
    print("Romb o przekątnych długości:", przekątna_pierwsza, "cm oraz",
          przekątna_druga,"cm", "ma pole równe", pole, "cm^2")


# policzPoleIŁadnieWyswietl(7, 4)


funkcja()
