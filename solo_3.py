class Mieszkanie:
    def __init__(self, panstwo,miasto,dzielnica,metraz,cena_za_metr,ilosc_pokoi,typ_zabudowania):
        self.panstwo = panstwo
        self.miasto = miasto
        self.dzielnica = dzielnica
        self.metraz = metraz
        self.cena_za_metr = cena_za_metr
        self.ilosc_pokoi = ilosc_pokoi
        self.typ_zabudowania = typ_zabudowania

    def __str__(self):
        if self.metraz > 100:
            return "Duze " + str(self.ilosc_pokoi) + " - pokojowe mieszkanie w mieście " + str(self.miasto)
        else:
            return "Male " + str(self.ilosc_pokoi) + " - pokojowe mieszkanie w mieście " + str(self.miasto)

    def oblicz_cene_mieszkania(self):
        return "Cena za mieszkanie: " + str(self.cena_za_metr * self.metraz)

    def odleglosc_od_centrum(self):
        if self.miasto == "Poznan":
            if self.dzielnica == "Wilda" or self.dzielnica=="Łazarz":
                return "Blisko centrum"
            elif self.dzielnica == "Piatkowo" or self.dzielnica=="Debiec":
                return "Daleko od centrum"
        else:
            return "brak danych"

    def miesieczny_czynsz(self):
        mnoznik_dla_bloku = 16
        mnoznik_dla_kamienicy = 10
        if self.typ_zabudowania == "blok":
            return "Miesięczny czynsz wynosi: " + str(self.metraz*mnoznik_dla_bloku)
        elif self.typ_zabudowania == "kamienica":
            return "Miesięczny czynsz wynosi: " + str(self.metraz * mnoznik_dla_kamienicy)
        else:
            return "brak danych"



mieszkanie_A = Mieszkanie("Polska", "Poznan", "Wilda", 30, 8000, 3, "blok")
print(mieszkanie_A)
print(mieszkanie_A.miesieczny_czynsz())
print(mieszkanie_A.odleglosc_od_centrum())
print(mieszkanie_A.oblicz_cene_mieszkania())