import json, operator, indicoio, re, string, sqlite3
from nltk import sent_tokenize
from nltk.corpus import stopwords
import models as m

with open('reviews_small.json') as reviews_file:
	reviews = json.load(reviews_file)

#Load api key
indicoio.config.api_key = 'b7053e769d8d561cd1c1f5c1636010f0'

#Splits each review into a list of sentences, split by period
def reviewTokenize(reviews):
	return [(review['stars'], sent_tokenize(review['text'])) for review in reviews]

#Splits each sentence in review into a bunch of words
def splitSentence(split_reviews):
	lst = []
	for review in split_reviews:
		lst.append((review[0], [sentence.split() for sentence in review[1]]))
	return lst

#Retrieves SENTENCE at designated review INDEX and sentence INDEX
def getSentence(reviews, rindex, index):
	return reviews[rindex][index]

#Retrieves REVIEW at designated INDEX
def getReview(reviews, index):
	return reviews[index]

#Tokenizes only one review
def singularTokenize(review):
	return sent_tokenize(review)

#Checks for repetition in given REVIEW sentence list, returns dictionary of frequency
def repetitionCheck(reviews):
	freq_dict = {}
	for review in reviews:
		for sentence in review:
			for word in sentence:
				if word not in freq_dict:
					freq_dict[word] = 1
				else:
					freq_dict[word] += 1
	freq_tup = sorted(freq_dict.items(), key=operator.itemgetter(1))
	return freq_tup

#Analysis of each reviews sentiment, and returns a dict of key: review id
#and value: sentiment average
def indi_sentimentR(review):
	sum = 0 
	count = 0
	for sentence in review:
		sum += indicoio.sentiment(sentence)
		count += 1
	average = sum/count
	return average

#average sentiment of different reviews
def averageSentiment(reviews):
	stars_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
	stars_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
	for review_cluster in reviews:
		stars_count[review_cluster[0]] += 1
		average = indi_sentimentR(review_cluster[1])
		stars_dict[review_cluster[0]] += average
	for key in stars_dict:
		stars_dict[key] = stars_dict[key]/stars_count[key]
	return stars_dict

def averageDBsentiment():
	stars_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
	stars_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
	for item in m.Review.query.all():
		stars_count[item.stars] += 1
		stars_dict[item.stars] += item.sentiment
	for key in stars_dict:
		stars_dict[key] = stars_dict[key]/stars_count[key]
	return stars_dict

def predictor(sentiment_value):
	sentiment_dict = averageDBsentiment()
	if sentiment_value in range(sentiment_dict['1'] - 0.05,
								sentiment_dict['1'] + 0.05):
		return 1
	if sentiment_value in range(sentiment_dict['2'] - 0.05,
								sentiment_dict['2'] + 0.05):
		return 2
	if sentiment_value in range(sentiment_dict['3'] - 0.10,
								sentiment_dict['3'] + 0.08):
		return 3
	if sentiment_value in range(sentiment_dict['4'] - 0.05,
								sentiment_dict['4'] + 0.05):
		return 4
	if sentiment_value in range(sentiment_dict['5'] + 0.02, 1):
		return 5
	else:
		return 3








