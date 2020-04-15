#import bibliotek
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#wyswietl to co w katalogu opinions.json
print(*os.listdir("./opinions_json"))

#wczytanie produkty i analiza
product_id = input("Podaj kod produktu: ")

#wczytanie do ramki danych opinii
opinions = pd.read_json("./opinions_json/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))

#częstość występowania liczby gwiazdek
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.1,0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color="darkorange")
plt.xticks(rotation=0)
ax.set_title("Częstość występowania ocen")
ax.set_xlabel("Liczba gwiazdek")
ax.set_ylabel("Liczba opinii")
plt.savefig("./figures_png/"+product_id+"_bar.png")
plt.close()

#udział poszczególnych w ogólnej liczbie
recommendation = opinions["recommendation"].value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label="",autopct="%.1f%%", colors=["purple","gold"])
ax.set_title("Częstość występowania ocen")

plt.savefig("./figures_png/"+product_id+"_pie.png")
plt.close()

#statystyki
stars_everage = opinions['stars'].mean()
pros = opinions['pros'].count()
cons = opinions['cons'].count()
purchased = opinions['purchased'].sum()

print(stars)

stars_purchased = pd.crosstab(opinions['stars'],opinions['purchased'])

#poszukaj jak procenty wyprowadzić pod "polecam, nie polecam" 