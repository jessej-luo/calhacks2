# Yelp Review Predictor

Built at Calhacks 2, this is a Yelp review predictor that uses the Indico sentiment analysis API. The backend is built using flask, and the front end using Bootstrap and jQuery. It takes in a review, and using the prediction algorithm returns a # of stars for the review. 

It uses a sqlite3 database which contains all the different reviews and their star rating, and after receiving a star prediction, the user can have the option to submit their review to the database with the correct # of stars and allows the algorithm to get better with a larger sample size. 


