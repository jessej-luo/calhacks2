from flask import Flask, render_template, g, request, redirect, jsonify
import sqlite3
import json
import models as m
import sentiment as s

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
DATABASE = 'database/database.db'

def get_db():
	db = getattr(g, "_database", None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db
#routes
@app.route("/")
def main():
	return render_template("index.ejs")
	
@app.route("/review", methods=["POST"])
def receive_review():
	review = request.form['review']
	prediction = review_prediction(review)
	return str(prediction)

@app.route("/review_add", methods=["POST"])
def receive_review_add():
	review = request.form['review']
	stars = request.form['stars']
	length = len(m.Review.query.all())
	sentiment = s.indi_sentimentR(s.singularTokenize(review))
	reviewAdd = m.Review(length, review, stars, sentiment)
	m.db.session.add(reviewAdd)
	m.db.session.commit()
	return ('', 202)

def review_prediction(review):
	sent_tok = s.singularTokenize(review)
	average = s.indi_sentimentR(sent_tok)
	return s.predictor(average)

#review handling
with open('reviews.json') as reviews_file:
	reviews = json.load(reviews_file)

def setupDB():
	for index in range(0, len(reviews)):
		review = m.Review(reviews[index]['id'], 
			reviews[index]['text'], 
			reviews[index]['stars'], 
			s.indi_sentimentR(s.singularTokenize(reviews[index]['text'])))
		m.db.session.add(review)
		m.db.session.commit()

def removeItem(id):
	m.Review.query.filter(Review.id == id).delete()
	m.Review.commit()

def readDB():
	print(m.Review.query.all())

if __name__ == "__main__":
	app.run()
