# Zadanie 4: Wykorzystajcie parametryzację w Pytest do przetestowania
# wielu danych naraz, zgodnie z wytycznymi w komentarzach TODO.

# ===========================================================================================

import pytest


def czy_pelnoletni(wiek: int) -> bool:
    return wiek >= 18


# TODO: Zastosuj mechanizm parametryzacji z biblioteki Pytest, aby "nakarmić" ten
#  test listą różnych przypadków i odpowiadających im wyników (przetestuj minimum
#  wiekowe, wartości pod/nad progiem oraz skrajności jak 0 czy 150 lat).
def test_czy_pelnoletni(wiek, oczekiwany_wynik):
    # TODO: Zbuduj uniwersalną asercję, która dynamicznie porówna wynik funkcji z
    #  wartością oczekiwaną przekazaną przez dekorator.

    # REMINDER: Usuń instrukcję 'pass' po dodaniu własnego kodu!
    pass