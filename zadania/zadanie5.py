# Zadanie 5: Skonfigurujcie wirtualny serwer testowy za pomocą
# fikstur, realizując krok po kroku zadania z komentarzy TODO.

# ===========================================================================================

import pytest


# TODO: Oznacz tę funkcję jako fiksturę o zasięgu całego modułu, dzięki czemu serwer
#  testowy odpali się tylko raz dla tego pliku.
def konfiguracja_serwera():
    print("\n[Uruchamianie serwera testowego... (to powinno pojawić się tylko raz!)]")

    # TODO: Zmodyfikuj sposób zwracania tego słownika tak, aby środowisko testowe
    #  pozwoliło wykonać kod "sprzątający" zdefiniowany na samym dole tej funkcji.
    return {
        "host": "127.0.0.1",
        "port": 8000,
        "debug": True
    }

    # TODO: Dodaj print informujący o zamykaniu serwera testowego (wykona się on dopiero, gdy
    #  wszystkie testy zostaną zakończone).
    pass


# --- TEST 1 ---
# TODO: Wstrzyknij przygotowaną wyżej fiksturę do tego testu.
def test_sprawdz_port(  # TODO: Tu wpisz argument ):
        # TODO: Upewnij się asercją, że w konfiguracji serwera ustawiono port 8000.

    pass

# --- TEST 2 ---
# TODO: Napisz od zera nowy test o nazwie 'test_sprawdz_pozostale_parametry',
    #  korzystający z tej samej fikstury. Upewnij się w nim (dwiema osobnymi asercjami), że
    #  tryb 'debug' jest aktywny (True), a 'host' odpowiada wartości localhosta (127.0.0.1).