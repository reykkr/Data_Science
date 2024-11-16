# SMS Spam Detection System using NLP and Naive Bayes

## Overview

This project involves building an SMS spam detection system using natural language processing (NLP) and machine learning. The dataset consists of SMS messages that are labeled as either "spam" or "ham" (not spam). The primary objective is to preprocess the text data, analyze it, and train a Naive Bayes classifier to classify new messages as spam or not.

The goal of this project is to develop a reliable spam detection model that can help filter out unwanted messages effectively.

## Purpose

The purpose of this project is to:

- Perform text preprocessing to clean and prepare SMS messages for machine learning.
- Develop a classification model to distinguish between spam and legitimate messages.
- Demonstrate skills in natural language processing (NLP), data analysis, and machine learning using Python.

## Key Features Demonstrated

### Data Analysis and Preprocessing

- **Data Loading and Exploration**: Loaded the SMS dataset and performed an initial exploration of the data.
- **Handling Missing Values**: Checked for missing data and ensured data quality.
- **Text Preprocessing**:
  - Removed special characters and numbers.
  - Tokenized words, removed stopwords, and lemmatized tokens.
  - Converted cleaned text back to a single string format.

### Data Analysis and Visualization

- **Message Length Analysis**: Explored message length differences between spam and non-spam messages.
- **Token Frequency Analysis**: Analyzed the most common tokens in spam and non-spam messages using frequency distribution plots.

### Machine Learning Model

- **Vectorization**:
  - **Bag of Words (BOW)**: Used scikit-learn's `CountVectorizer` to convert SMS messages into a bag-of-words representation.
  - **TF-IDF**: Applied Term Frequency-Inverse Document Frequency (TF-IDF) to transform text data into numerical format, accounting for term importance.
- **Model Training**:
  - Trained a Naive Bayes classifier on the processed data to predict if a message is spam or ham.
- **Model Evaluation**:
  - Evaluated the model's performance using confusion matrices and classification reports.
  - Analyzed precision, recall, F1-score, and overall accuracy.

## Tools Used

- **Python**: Used for data handling, text preprocessing, and building the machine learning model.
- **Pandas and NumPy**: Employed for data manipulation and numerical operations.
- **NLTK**: Used for natural language processing, including tokenization, stopword removal, and lemmatization.
- **Matplotlib**: Utilized for visualizing token frequency distributions.
- **scikit-learn**: Used for text vectorization, model training, and evaluation.

## Project Components

### Data Loading and Preprocessing

- **Data Loading**: Loaded the SMS dataset from a local file.
- **Text Cleaning**: Removed special characters, numbers, and stopwords, and performed lemmatization to prepare text for analysis.
- **Data Transformation**: Converted text data into numerical format using BOW and TF-IDF techniques.

### Machine Learning Implementation

- **Train-Test Split**: Split the dataset into training and testing sets to evaluate the model's performance.
- **Model Training**: Used a Naive Bayes classifier, which is well-suited for text classification problems.
- **Model Evaluation**: Evaluated the model's performance with metrics like accuracy, precision, recall, and F1-score.

### Example Output

- **Confusion Matrix**: Displayed the number of true positives, false positives, true negatives, and false negatives to assess model performance.
- **Classification Report**: Provided detailed metrics for evaluating the model's performance on spam and non-spam messages.
- **Spam Detection Example**: Demonstrated how the model classifies a new SMS message as spam or ham.

## Notes

This project demonstrates the use of natural language processing and machine learning for classifying SMS messages as spam or ham. It highlights the importance of text preprocessing and the effectiveness of vectorization techniques like TF-IDF in building a robust classification model. The use of a Naive Bayes classifier ensures fast and accurate spam detection, making it ideal for real-time applications.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

