# Zadanie 3: Przetestujcie logikę biznesową za pomocą instrukcji
# assert, wykonując polecenia ukryte w tagach TODO.

# ===========================================================================================

def dodaj_podatek(kwota_netto: float) -> float:
    return kwota_netto * 1.23


def test_dodaj_podatek():
    # --- PRZYPADEK 1: Standardowa kwota ---
    kwota = 100.0

    # TODO: Zweryfikuj za pomocą instrukcji assert, czy podatek dla zdefiniowanej wyżej
    #  kwoty został wyliczony poprawnie (powinno wyjść 123.0).

    # --- PRZYPADEK 2: Wartość brzegowa (zero) ---
    # TODO: Przetestuj przypadek brzegowy – upewnij się (najlepiej w jednej linijce),
    #  że podatek od kwoty 0.0 to nadal poprawne 0.0.

    # REMINDER: Usuń instrukcję 'pass' po dodaniu własnego kodu!
    pass


if __name__ == "__main__":
    test_dodaj_podatek()
    print("Gratulacje! Zadanie 3 wykonane poprawnie, obie asercje przeszły bez błędu.")