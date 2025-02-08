from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__,template_folder='template')  #instance of flask class

ENV = 'dev'  #environment variable

if ENV == 'dev':            #development database
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Alok%402000@localhost/Lexus' # -> it’s a database connection string b/w frontend http request and our backend database, also @ = %40 for uri decoding

else:                      #production database -> do nothing
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   #to not entertain any modifications 

db = SQLAlchemy(app)   # we need this to interact with our database

class Feedback(db.Model):          # class corresponds to a table in db 
    __tablename__ = 'feedback'     #tablename  and  below are its column

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):  # The constructor initializes objects when they are created.
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

@app.route('/')  #defines root for root url
def index():
    return render_template('index.html') # Renders and returns an HTML file called index.html from the templates folder. 

@app.route('/submit', methods=['POST']) #defines root for submit url
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)

        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')

        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:  # if customer does not exist in db then take feedback
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')

        return render_template('index.html', message='You have already filled the feedback')

if __name__ == '__main__':
    app.debug = True  # automatic reloading if code changes or server keeps reloading
    app.run()         # Starts the Flask development server. By default, it runs on http://127.0.0.1:5000/