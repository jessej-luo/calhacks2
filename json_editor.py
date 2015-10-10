import json

with open('reviews.json', 'r+') as reviews:
	data = json.load(reviews)
	for i in range(0, len(data)):
		data[i]['id'] = i
	reviews.seek(0)
	json.dump(data, reviews, indent=4)