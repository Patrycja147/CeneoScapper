#import bibliotek
import os
import pandas as pd

#wyswietl to co w katalogu opinions.json
print(*os.listdir("./opinions_json"))

#wczytanie produkty i analiza
product_id = input("Podaj kod produktu: ")

#wczytanie do ramki danych opinii
opinions=pd.read_json("./opinions_json/"+product_id+".json")
opinions = opinions.set_index("opinion_id")


print(opinions)