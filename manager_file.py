

class StructCours:

    def __init__(self, cours) -> None:
        self._name = cours[0]
        self._isin = cours[1]
        self._symbol = cours[2]
        self._market = cours[3]

        self._currency = cours[4]
        self._openprice = float(cours[5].replace(',','.'))
        self._highprice = float(cours[6].replace(',','.'))
        self._lowprice = float(cours[7].replace(',','.'))
        self._lastprice = float(cours[8].replace(',','.'))
        self._last_trade_mic_time = cours[9]
        self._timezone = cours[10]
        self._volume = float(cours[11].replace(',','.'))
        self._turnover = cours[12]
        self._closing_price = float(cours[13].replace(',','.'))
        self._closing_price_dateTime = cours[14]



filename = "C:\\Users\\HP\\Desktop\\Euronext_Equities_2023-10-11.csv"

cours = {}
cpt = 0
with open(filename, 'r') as file:
    for line in file:
        if cpt > 3:
            c = line.replace('"', '').split(';')
            if not "-" in c:
                cours[c[1]] = StructCours(c)

        cpt += 1

p = cours['FR0000033409']._openprice
print(p)
print(type(p))



