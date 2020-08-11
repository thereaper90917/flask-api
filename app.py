from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = APIManager(app,flask_sqlalchemy_db=db)

class Dev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(255),nullable=False)
    image_url = db.Column(db.String(255), nullable=False)




manager.create_api(Dev, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
