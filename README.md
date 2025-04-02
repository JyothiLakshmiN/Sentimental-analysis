**Sentiment Analysis: Amazon products Reviews**
**Problem statement**
Amazon-based retailer Kozmos, specializing in home textiles and casual wear, 
aims to enhance its products by analyzing customer feedback and addressing complaints. 
The goal is to perform sentiment analysis on reviews, assign sentiment labels, 
and develop a classification model based on these labeled sentiments.

1. Load the data set.
2. Preprocess the data.
3. Text Visualization (Bar chart and WordCloud).

**Step 1: Initialize SentimentIntensityAnalyzer**
Use NLTK's SentimentIntensityAnalyzer.

**Step 2: Compute Polarity Scores**
Calculate polarity_scores() for the first 10 reviews.
Filter the first 10 reviews based on their compound scores.
Assign sentiment labels: "pos" (if compound score > 0) and "neg" (otherwise).
Apply sentiment labeling to all reviews and store the results in a new column.
Note: The labeled dataset serves as the dependent variable for the classification model.


**Train-Test Split**
Split the dataset into training and test sets.

Convert Text to Numerical Representation
Use TfidfVectorizer

Train a Logistic Regression model on the dataset.
Generate a classification report.








