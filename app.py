from flask import Flask, render_template, g, request, redirect
import models as m
import sqlite3
import json
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

@app.route("/", methods=['POST'])
def main():
	return render_template('index.ejs')

if __name__ == "__main__":
	app.run()

#Set up Database by opening Json File

# def db_addReview(stars, review):
# 	id = m.Review.id.property.columns[0].type.length
# 	stars = #input
# 	review = m.Review(id, review, )

def review_prediction(review):
	sent_tok = s.singularTokenize(review)
	average = indi_sentimentR(sent_tok)
	

with open('reviews.json') as reviews_file:
	reviews = json.load(reviews_file)

def setupDB():
	for index in range(0, len(reviews)):
		review = m.Review(reviews[index]['id'], 
			reviews[index]['text'], 
			reviews[index]['stars'], s.indi_sentimentR(s.singularTokenize(reviews[index]['text'])))
		m.db.session.add(review)
		m.db.session.commit()

def readDB():


	

