menu_glowne = ("utworz", "zarzadzaj", "koniec")
menu_utworz = ("uczen", "nauczyciel", "wychowawca", "koniec")
menu_zarzadzaj = ("klasa", "uczen", "nauczyciel", "wychowawca", "koniec")

uczen = {}
nauczyciel = {}
wychowawca = {}
while True:
    print(f'Uzytkowniku masz do wyboru następujace opcje: {menu_glowne}')
    wybor = input('Podaj opcje: ')
    if wybor not in menu_glowne:
        print('Wybrales niewłasciwa opcje!')
        continue
    if wybor == "koniec":
        print('Zakonczyles dzialanie programu!')
        break
    elif wybor == "utworz":
        print('Wybrales opcje utworz.')
        while True:
            print(f'Uzytkowniku masz do wyboru następujace opcje: {menu_utworz}')
            wybor = input('Podaj opcje: ')
            if wybor not in menu_utworz:
                print('Wybrales niewłasciwa opcje!')
                continue
            if wybor == "koniec":
                print('Zakonczyles dzialanie opcji utworz!')
                break
            elif wybor == "uczen":
                print('Wybrales opcje uczen.')
                dane_ucznia = input('Podaj imie i nazwisko ucznia:')
                klasa_ucznia = input("Podaj klasę ucznia: ")
                if klasa_ucznia not in uczen:
                    uczen_do_dopisdania = []
                    uczen_do_dopisdania.append(dane_ucznia)
                    uczen[klasa_ucznia] = uczen_do_dopisdania
                    print(f'Lista uczniow: {uczen}')
                else:
                    sklad_klasy = uczen.get(klasa_ucznia)
                    sklad_klasy.append(dane_ucznia)
                    uczen[klasa_ucznia] = sklad_klasy
                    print(f'Lista uczniow: {uczen}')
            elif wybor == "nauczyciel":
                print('Wybrales opcje nauczyciel.')
                dane_nauczyciel = input('Podaj imie i nazwisko nauczyciela: ')
                prowadzony_przedmiot = input('Podaj prowadzony przedmiot: ')
                list_klas = []

                while True:
                    prowadzone_klasy = input('Podaj prowadzone klasy: \n')
                    if prowadzone_klasy == "":
                        break
                    else:
                        list_klas.append(prowadzone_klasy)
                        print(f'Lista klas: {list_klas}')
                        continue
                nauczyciel[dane_nauczyciel] = {'przedmiot': prowadzony_przedmiot, 'klasy': list_klas}
                print(f'Zestawienie nauczycieli: {nauczyciel}')

            elif wybor == "wychowawca":
                print('Wybrales opcje wychowawca.')
                dane_wychowawca = input('Podaj imie i nazwisko wychowawcy: ')
                klasa_wychowawcy = input('Podaj klase wychowawcy: ')
                wychowawca[dane_wychowawca] = klasa_wychowawcy
                print(f'Wychowawcy z klasami: {wychowawca}')
    elif wybor == "zarzadzaj":
        print('Wybrales opcje zarzadzaj.')
        while True:
            print(f'Uzytkowniku masz do wyboru następujace opcje: {menu_zarzadzaj}')
            wybor = input('Podaj opcje: ')
            if wybor not in menu_zarzadzaj:
                print('Wybrales niewłasciwa opcje!')
                continue
            if wybor == "koniec":
                print('Zakonczyles dzialanie opcji zarzadzaj!')
                break
            elif wybor == "klasa":
                print('Wybrales opcje klasa.')
                klasa = input('Podaj klase:')
                sklad_klasy = uczen.get(klasa)
                for k, v in wychowawca.items():
                    if v == klasa:
                        przypisany_nauczyciel = k
                        print(f'Dla {klasa}: \n skład klasy: {sklad_klasy}\n wychowawca klasy:{przypisany_nauczyciel} ')

            elif wybor == "uczen":
                print('Wybrales opcje uczen')
                dane_ucznia = input("Podaj imie i nazwisko ucznia: ")
                for k, v in uczen.items():
                    if dane_ucznia in v:
                        klasa = k
                        print(f'Uczeń jest w klasie:  {klasa}\n'
                              f'Uczeń ma nastepujące leckcje:')
                        for k, v in nauczyciel.items():
                            if klasa in v['klasy']:
                                lekcje_nauczyciel = nauczyciel.get(k)
                                przedmiot = lekcje_nauczyciel['przedmiot']

                                print(f'<{przedmiot.strip("[]")}> prowadzony przez <{k}>')

            elif wybor == "nauczyciel":
                print('Wybrales opcje nauczyciel.')
                dane_nauczyciel = input('Podaj imie i nazwisko nauczyciela: ')
                if dane_nauczyciel not in nauczyciel:
                    print('Nie ma takiego nauczyciela.')
                else:
                    klasy = nauczyciel[dane_nauczyciel]['klasy']
                    print(f'Nauczyciel prowadzi nastepujace klasy: {klasy}')

            elif wybor == "wychowawca":
                print('Wybrales opcje wychowawca.')
                dane_wychowawca = input('Podaj imię i nazwisko wychowacy: ')

                klasa = wychowawca[dane_wychowawca]
                print(klasa)
                uczniowie_wychowawcy = uczen.get(klasa)
                print(f'W klasie wychowawcy są następujący uczniowie:\n {uczniowie_wychowawcy}')
