#Load Core Package
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
#init app
app = Flask(__name__)

#DB
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/users.db'

#model schema
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))

#Routing
@app.route('/')
def wazzup():
    return 'Wazzup wazzup Abhiraman'

@app.route('/home')
def home():
    message = 'Welcome Home'
    return render_template('home.html',message = message)

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        single_user = User(firstname = firstname,lastname = lastname)
        db.session.add(single_user)
        db.session.commit()

    return render_template('home.html',firstname = firstname,lastname = lastname)

@app.route('/allusers')
def allusers():
    userslist = User.query.all()
    print(userslist)
    return render_template('results.html',userslist = userslist)

@app.route('/profile/<firstname>')
def profile(firstname):
    user = User.query.filter_by(firstname = firstname).first()
    return render_template('profile.html',user = user)


if __name__ == '__main__':
	app.run(debug=True)
