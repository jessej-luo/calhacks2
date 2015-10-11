from flask import Flask, render_template, g, request, redirect
import models as m
import sqlite3
import json

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
DATABASE = 'database/database.db'

def get_db():
	db = getattr(g, "_database", None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":
	app.run()

#Set up Database by opening Json File

with open('reviews.json') as reviews_file:
	reviews = json.load(reviews_file)

def setupDB():
	for index in range(0, len(reviews)):
		review = m.Review(reviews[index]['id'], 
			reviews[index]['text'], 
			reviews[index]['stars'])
		m.db.session.add(review)
		m.db.session.commit()

def readDB():
	print(m.Review.query.all())

