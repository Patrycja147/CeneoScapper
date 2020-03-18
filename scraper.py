#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres url strony z opiniami
url="https://www.ceneo.pl/49541116#tab=reviews"

#podanie kodu html
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')
opinions = page_tree.find_all('li','review-box')

for opinion in opinions:
    opinion_id=opinion["data-entry-id"]
    author = opinion.find('div', 'reviewer-name-line').string
    recomendation = opinion.find('div',"product-review-summary").find('em').string
    stars = opinion.find('span','review-score-count').string
    try:
        purchased = opinion.find('div',"product-review-pz").string
    except AttributeError:
        purchased= None

    dates = opinion.find("span","review-time").find_all("time")
    review_date = dates.pop(0)["datetime"]
    try:
        purchase_date= dates.pop(0)["datatime"]
    except IndexError:
        purchased= None

    useful = opinion.find('button','vote-yes').find('span').string
    useless = opinion.find('button','vote-no').find('span').string
    content = opinion.find('p','product-review-body').get_text()

    try:
        pros = opinion.find("div","pros-cell").find('ul').get_text()
    except AttributeError:
        pros= None

    try:
        cons = opinion.find("div","cons-cell").find('ul').get_text()
    except AttributeError:
        cons = None

print(cons)