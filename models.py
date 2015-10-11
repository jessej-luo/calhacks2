from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

#Reset Database to empty
def reset():
	db.drop_all()
	db.create_all()

#Review DB model 
class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	review = db.Column(db.String(5000), primary_key=True)
	stars = db.Column(db.Integer, primary_key=True)
	sentiment = db.Column(db.Integer, primary_key=True)

	def __init__(self, id, review, stars, sentiment):
		self.id = id
		self.review = review
		self.stars = stars
		self.sentiment = sentiment

	def __repr__(self):
		return '<ID: {} Stars: {} Sentiment: {} Review: {}>'.format(
			self.id, self.stars, self.sentiment, self.review[0:100])

	def __init__(self, id, review, stars):
		self.id = id
		self.review = review
		self.stars = stars

	def __repr__(self):
		return '<ID: {} Stars: {} Review: {}>'.format(self.id, self.stars, self.review[0:100])

