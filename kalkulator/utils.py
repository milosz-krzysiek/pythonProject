
def round_number(liczba):
    czesc_calkowita = liczba[0]
    czesc_dziesietna = liczba[1]
    czesc_dziesietna = czesc_dziesietna[0:3]

    ostatnia_liczba = int(czesc_dziesietna[2])
    liczba_do_zaokraglenia = int(czesc_dziesietna[0:2])

    if(ostatnia_liczba >= 5):
        liczba_do_zaokraglenia += 1

    if(liczba_do_zaokraglenia == 100):
        czesc_dziesietna = "000"
        liczba_do_zaokraglenia = 0


    result = [str(czesc_calkowita), str(liczba_do_zaokraglenia)]
    return result
    


def simplify_output(liczba: float):
    tmp_liczba = str(liczba)
    podzielona_liczba = tmp_liczba.split('.')
    
    zaokraglona_liczba = round_number(podzielona_liczba)
    czesc_calkowita, czesc_dziesietna = zaokraglona_liczba

    if(czesc_dziesietna == '0'):
        return czesc_calkowita
    
    return czesc_calkowita + '.' + czesc_dziesietna


print(simplify_output(3.999))

