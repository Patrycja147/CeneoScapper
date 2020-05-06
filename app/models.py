class Product:
    def __init__(self, product_id, name, opinions = []):
        self.product_id = product_id
        self.name = name
        self.opinions = opinions
    def __str__(self):
        return f'Product_id: {self.product_id}\nName {self.name}\nOpinions:'.join(str(opinion) for opinion in self.opinions)
        #return (f'Product_id: {self.product_id}\nName {self.name}\nOpinions:{[str(opinion) for opinion in self.opinions]}'
        

class Opinion:
    #słownik
    tags = {
        "recommendation":["div","product-review-summary","em"],
        "stars":["span", "review-score-count"],
        "content":['p','product-review-body'],
        "author":["div", "review-name-line"],
        "pros":["div","pros-cell",'ul'],
        "cons":["div","cons-cell",'ul'],
        "usefull":['button','vote-yes', "span"],
        "useless":['button','vote-no',"span"],
        "purchased":["div","product-review-pz","em"],
    }
    #definicja inicjalizatora
    def __init__(self, opinion_id=None, author=None, recommendation=None, stars=None, content=None,cons=None,pros=None, usefull=None, useless=None, purchased=None, purchase_date=None, review_date=None):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.cons = cons
        self.pros = pros
        self.usefull = usefull
        self.useless = useless
        self.purchased = purchased
        self.purchase_date = purchase_date
        self.review_date = review_date

    def __str__(self):
        return f'Opinion_id: {self.opinion_id}\nAuthor {self.author}\nStars: {self.stars}\n'
    def extract_opinion(self):
        pass


opinion = Opinion()
opinion2 = Opinion()
product=Product(None,None, opinions=[opinion],)
print(product)

