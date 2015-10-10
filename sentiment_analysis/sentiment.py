import json, operator, indicoio
from nltk import sent_tokenize
from nltk.corpus import stopwords
import re
import string

with open('reviews.json') as reviews_file:
	reviews = json.load(reviews_file)

#Load api key
indicoio.config.api_key = 'b7053e769d8d561cd1c1f5c1636010f0'

#Splits each review into a list of sentences, split by period
def reviewTokenize(reviews):
	return [sent_tokenize(review['text']) for review in reviews]

#Splits each sentence in review into a bunch of words
def splitSentence(split_reviews):
	return [[sentence.split() for sentence in review] for review in split_reviews]

#Retrieves SENTENCE at designated review INDEX and sentence INDEX
def getSentence(reviews, rindex, index):
	return reviews[rindex][index]

#Retrieves REVIEW at designated INDEX
def getReview(reviews, index):
	return reviews[index]

#Removes stop words, then rejoins String into sentences
# def removeStop(splitSentence):
# 	for review in splitSentence:
# 		for i in range(0, len(review)):
# 			filtered_words = [word for word in review[i] if 
# 						word not in stopwords.words('english')]
# 			review[i] = filtered_words
# 			review[i] = ' '.join(review[i])
# 	return splitSentence

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
def indi_sentiment(reviews):
	sentiment_dict = {}
	id = 0
	for review in reviews:
		sum = 0
		count = 0
		for sentence in review:
			sum+= indicoio.sentiment(sentence)
			count += 1
		average = sum/count
		sentiment_dict[id] = average
		id += 1
	return sentiment_dict

def cleanText(reviews):
	return [[sentence.translate().lower() 
			for sentence in review] for review in reviews]
# def punctuation_counter(splitReviews):
# 	count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
# 	punctuationDict = {}
# 	for review in splitReviews:
# 		for sentence in review:
# 			punctuationList.append(count(sentence, string.punctuation))
# 	return punctuationList

#TEST FILES
splitReviews = reviewTokenize(reviews)
splitSentence = splitSentence(splitReviews)
dict = repetitionCheck(splitSentence)
sentiment = indi_sentiment(splitReviews)
print(sentiment)

# print(punctuation_counter(splitReviews))
# #Punctuation 
# punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
# #split_punctuation_words = re.findall(r"[\w']+|[.,!?;]", sentence)
# def punctuation_counter(splitReviews):
# 	for sentence in splitReviews:
# 		print(sentence)

#print(punctuation_counter(punctuation,reviewTokenize(reviews)))



