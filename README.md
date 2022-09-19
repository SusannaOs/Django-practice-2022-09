# Django-practice-2022-09
First django practice project

## Asennus

1. Luo virtuaaliympäristö: ´python -m venv venv´
2. Aktivoi virtuaaliympäristö
    - VSCode avaa python-tiedosto -> ctrl+shift+p -> change interpreter -> python venv
    -muista käynnistää terminaali uudestaan ja tarkistaa että siinä lukee venv että se on aktiivinen.
3. Asenna Django ´pip install django´

## Django-tutoriaali

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

## Projektin luonti

1. Aja ´django-admin startproject varaukset´
2. Siirä varaukset kansion sisältö yhden tason ylemmäksi hakemistossa.

## Kehityspalvelimen ajaminen

1. Aja ensin migraatiot: ´python manage.py migrate´
2. Käynnistö kehityspalvelin: ´python manage.py runserver´

## Kehityspalvelin tipsit

ctrl - c poistuu serveristä