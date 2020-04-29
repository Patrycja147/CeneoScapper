#import bibliotek
from flask import Flask

#utworzenie obiektu klasy Flask
app = Flask(__name__)

#impors views
from app import views

if __name__=='__main__':
    app.run(debug=True)

