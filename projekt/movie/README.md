# Katalog Kolekcji Filmów

## Opis
Aplikacja internetowa zbudowana w Django, która umożliwia użytkownikowi zarządzanie kolekcją filmów: dodawanie, edytowanie, filtrowanie i przeglądanie filmów według różnych kryteriów. Aplikacja posiada również system rejestracji i logowania użytkowników oraz interfejs graficzny.

## Spis treści
1. [Funkcjonalności](#-funkcjonalności)
2. [Wymagania](#-wymagania)
3. [Instalacja i uruchomienie](#-instalacja-i-uruchomienie)

## Funkcjonalności
1. Rejestracja i logowanie użytkownika
- użytkownicy mogą tworzyć konta, logować się i wylogowywać
2. Dodawanie nowych filmów
- zalogowani użytkownicy mogą dodawać nowe filmy do katalogu
3. Edycja filmów
- możliwość edytowania istniejących wpisów (tytuł, reżyser, ocena, gatunek)
4. Filtrowanie filmów po tytule, reżyserze, gatunku
- filmy można filtrować po tytule, reżyserze, gatunku
5. Sortowanie filmów
- sortowanie listy filmów alfabetycznie oraz według oceny, reżysera, gatunku
6. Interfejs graficzny
- pastelowo-różowy wygląd strony dzięki arkuszowi CSS
7. Ochrona widoków
- dodawanie i edycja filmów dostępne tylko po zalogowaniu (z @login_required)

## Wymagania
- Python 3.12 lub nowszy
- Django 5.1.7 lub nowszy
- Przeglądarka internetowa (do testowania)

## Instalacja i uruchomienie

1. **Sklonuj repozytorium lub pobierz ZIP:**

git clone https://github.com/MariaGalecka/MVC.git
cd MVC/projekt/movie_catalog

2. **(Opcjonalnie) Utwórz i aktywuj środowisko wirtualne:**
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. **Zainstaluj wymagane pakiety:**
pip install django

4. **Wykonaj migracje:**
python manage.py migrate

5. **Uruchom serwer developerski:**
python manage.py runserver

6. **Wejdź w przeglądarkę:**
http://127.0.0.1:8000/
