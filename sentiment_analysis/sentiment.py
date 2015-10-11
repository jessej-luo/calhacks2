import json, operator, indicoio
from nltk import sent_tokenize
from nltk.corpus import stopwords
import re
import string

with open('reviews_med.json') as reviews_file:
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

#Takes in split in sentences, 
#Removes stop words, then rejoins String into sentences
# def removeStop(splitSentence):
# 	for review in splitSentence:
# 		for i in range(0, len(review)):
# 			filtered_words = [word for word in review[i] if 
# 						word not in stopwords.words('english')]
# 			review[i] = filtered_words
# 			review[i] = ' '.join(review[i])
# 	return splitSentence 


#webapp functions

#TEST FILES
<<<<<<< HEAD
# splitReviews = reviewTokenize(reviews)
# splitSentence = splitSentence(splitReviews)
# print(splitSentence)
# dict = repetitionCheck(splitSentence)
# sentiment = indi_sentiment(splitReviews)
# print(sentiment)
#Types of different word lists needed
#sentences are split up into words
splitSentence = 0
#reviews are split up into sentences
splitReviews = 0
#sentences are cleaned
cleanedSentence = 0
=======
splitReviews = reviewTokenize(reviews)
splitSentence = splitSentence(splitReviews)
print(splitSentence)
#sentiment = indi_sentiment(splitReviews)
#print(sentiment)

# print(punctuation_counter(splitReviews))
# #Punctuation 
# punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
# #split_punctuation_words = re.findall(r"[\w']+|[.,!?;]", sentence)
# def punctuation_counter(splitReviews):
# 	for sentence in splitReviews:
# 		print(sentence)

#print(punctuation_counter(punctuation,reviewTokenize(reviews)))

# def punctuation_counter(splitReviews):
# 	count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
# 	punctuationDict = {}
# 	for review in splitReviews:
# 		for sentence in review:
# 			punctuationList.append(count(sentence, string.punctuation))
# 	return punctuationList
>>>>>>> sentiment

