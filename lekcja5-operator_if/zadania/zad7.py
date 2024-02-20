#liczba w przedziale <1,10> lub <17,21>

liczba = int(input("Podaj liczbe z przedzialu 1-10 lub 17-21\n"))

if((liczba >= 1 and liczba <= 10) or (liczba >= 17 and liczba <= 21)):
	print("znaleziono skarb")
else:
	print("falszywy trop")