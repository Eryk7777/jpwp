# Zadanie 2: Zbudujcie klasę z automatyczną walidacją w bibliotece Pydantic,
# realizując kroki wskazane w komentarzach TODO.

# ===========================================================================================

from pydantic import BaseModel, ValidationError


class Uzytkownik(BaseModel):
    # TODO: Zdefiniuj strukturę modelu (imię, wiek, aktywny) pamiętając o odpowiednich typach danych.
    #  Zadbaj o to, by użytkownik domyślnie był traktowany jako "aktywny".
    # REMINDER: Usuń poniższą instrukcję 'pass' po dodaniu własnego kodu!
    pass


# Kod testowy
try:
    poprawny_user = Uzytkownik(imie="Anna", wiek=22)
    print("Poprawny użytkownik:", poprawny_user)

    # TODO: Zweryfikuj asercją, czy mechanizm przypisywania wartości domyślnej zadziałał
    #  prawidłowo dla nowo utworzonego obiektu 'poprawny_user'.

    # Próba utworzenia błędnego użytkownika
    bledny_user = Uzytkownik(imie="Jan", wiek="dwadzieścia")
except ValidationError as e:
    print("Złapano błąd walidacji, zgodnie z oczekiwaniami!")