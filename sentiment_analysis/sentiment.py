import json, operator, indicoio
from nltk import sent_tokenize
import re

with open('reviews_small.json') as reviews_file:
	reviews = json.load(reviews_file)

#Load api key
indicoio.config.api_key = 'b7053e769d8d561cd1c1f5c1636010f0'

#Splits each review into a list of sentences, split by period
def reviewTokenize(reviews):
	return [sent_tokenize(review['text']) for review in reviews]
print(reviewTokenize(reviews))

#Splits each sentence in review into a bunch of words
def splitSentence(split_reviews):
	return [[sentence.split() for sentence in review] for review in split_reviews]

#Retrieves SENTENCE at designated review INDEX and sentence INDEX
def getSentence(reviews, rindex, index):
	return reviews[rindex][index]

#Retrieves REVIEW at designated INDEX
def getReview(reviews, index):
	return reviews[index]

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


#TEST FILES
splitReviews = reviewTokenize(reviews)
splitSentence = splitSentence(splitReviews)
print(splitSentence)
dict = repetitionCheck(splitSentence)
sentiment = indi_sentiment(splitReviews)
print(sentiment)
#Types of different word lists needed
#sentences are split up into words
splitSentence = 0
#reviews are split up into sentences
splitReviews = 0
#sentences are cleaned
cleanedSentence = 0

#Punctuation 
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
#split_punctuation_words = re.findall(r"[\w']+|[.,!?;]", sentence)
def punctuation_counter(l1,l2):
	return sum(a==b for a,b in zip(l1,l2))
#print(punctuation_counter(punctuation,reviewTokenize(reviews)))
print(re.split('(\W+)', 'Words, words, words.'))




