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
- nieprzydatna: span[id="vote-yes]
                button.vote-no["data-total-vote"]
- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
