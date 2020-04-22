# CeneoScapper
## Etap 1 - pobranie składowych pojedynczej opinii
- opinia: li.review-box
- identyfikator: li.review.box["data-entry-id"]
- autor: div.reviewer-name-line
- rekomendacja: div.product-review-summary > em
- gwiazdki: span.review-score-count
- potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.review-time > time["datetime"] - pierwszy element listy
- data zakupu: span.review-time > time["datetime"] - drugi element listy
- przydatna: span[id="vote-yes]
             button.vote-yes["data-total-vote"]
             button.vote-yes > span
- nieprzydatna: span[id="vote-yes]
                button.vote-no["data-total-vote"]
                button.vote-no > span

- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
## Etap 2 - pobranie składowych wszystkich opinii z pojedynczej strony
- zapisanie składowych opinii w złożonej strukturze danych
## Etap 3 - pobranie wszystkich opinii o pojedyńczym produkcie
- przechodzenie po stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)
## Etap 4 
- tranformacja danych
- refaktoryzacja
## Etap 5
- Zapis danych do obiektu dataframe(ramka danych)
- obliczenia na danych w ramce danych
- wykonanie wykresów na podstawie danych z ramki
## Etap 6 - przygotowanie interface'u webowego aplikacji (Flask)
-/yourapp  
        /run.py  
        /config.py  
        /app  
            /__init__.py
            /views.py  
            /models.py  
            /static/  
                /main.css
            /templates/  
                /base.html  
        /requirements.txt  
        /yourappenv