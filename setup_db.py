from app import app
from models as m

with open('reviews_small.json') as reviews_file:
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



