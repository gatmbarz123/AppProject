from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

# this line initializes a new flask application
app = Flask(__name__, template_folder='templates', static_folder='static')
#this is the connection to the MYSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'root'),
    os.getenv('DB_PASSWORD', ''),
    os.getenv('DB_HOST', 'db'),
    os.getenv('DB_NAME', 'flask')
)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#what the the table make of
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.String(100))

#this make the table for the database
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

#this is the route that take the template and make it
@app.route('/')
def index():
    vote_count = {
        'Bibi': Person.query.filter_by(vote='Bibi').count(),
        'Ben Gvir': Person.query.filter_by(vote='Ben Gvir').count(),
    }
    return render_template('index.html', vote_count=vote_count)

#this is the submit bottem for the web .
@app.route('/submit', methods=['POST'])
def submit():
    selected_photo = request.form.get('photo')
    if selected_photo:
        new_vote = Person(vote=selected_photo)
        db.session.add(new_vote)
        db.session.commit()
    return redirect(url_for('index'))

# if statment that check if the script that run his the main script
# and after the run the app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)