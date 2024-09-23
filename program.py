'''
    Program to prosty kalkulator, obsługuje 4 działania; dodawanie, odejmowanie, mnożenie, dzielenie oraz opcję wyjścia.
    Użytkownik wpierw wybiera opcję, następnie wpisuje dwie liczby a program wykonuje obliczenia.
'''

def main(): # glowna funkcja programu, wykonywana jako pierwsza
    while True: # tworzy nieskonczona petle
        try: # rozpoczyna blok kodu
            a = int(input("Wybierz działanie (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 0 - wyjście): ")) # wybór opcji przez użytkownika i przypisanie jej do zmiennej

            if a == 0: # sprawdzenie czy użytkownik wybrał zero, jeśki tak, przerwij program;
                break

            z = float(input("Wpisz pierwszą liczbę: ")) # zmienna pierwszej liczby
            x = float(input("Wpisz drugą liczbę: ")) # zmeinna drugiej liczby

            if a == 4 and x == 0: # warunek w którym występuje dzielenie przez 0
                print("Nie można dzielić przez zero!")  #komunikat
            else: 
                if a == 1: # dla dodawania
                    output = z + x
                elif a == 2: # dla odejmowania
                    output = z - x
                elif a == 3: # dla mnozenia 
                    output = z * x
                else: # dla dzielena
                    output = z / x

                print(f"Wynik: {output}") # wyswietlenie wyniku

        except ValueError: # gdy napotyka błąd
            print("Błędne dane. Podaj liczby.") # komunikat blędu

if __name__ == "__main__": # sprawdza czy plik jest uruchamiany bezpośrednio, a nie jako moduł, jeśli tak - odpala funkcję main().
    main()