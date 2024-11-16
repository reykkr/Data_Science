# Logistic Regression Heart Disease Prediction

## Overview

The Logistic Regression Heart Disease Prediction project is a Python-based machine learning implementation designed to predict whether a patient is likely to have heart disease based on various physical attributes. This project uses the Heart Disease dataset from the UCI Machine Learning Repository and applies logistic regression to build a binary classification model.

The goal of this project is to explore the relationships between physical health features such as age, cholesterol, and exercise-induced factors, and to predict heart disease presence efficiently and accurately.

## Purpose

The purpose of this project is to:

- Implement a logistic regression model to predict heart disease.
- Explore the relationships between physical health metrics and heart disease.
- Showcase skills in data preprocessing, exploratory data analysis, and model evaluation using Python and scikit-learn.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize target distributions, pairwise relationships, and feature correlations, aiding in better understanding of the data.

### Data Preprocessing

- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.
- **Train-Test Split**: Separated the dataset into training and testing sets to evaluate model performance effectively.

### Model Implementation and Evaluation

- **Logistic Regression Model**: Developed a logistic regression model using scikit-learn to classify patients as having heart disease or not.
- **Model Coefficients**: Calculated and interpreted the model's coefficients to understand the impact of each feature on the outcome.

### Evaluation Metrics

- **Confusion Matrix and Classification Report**: Evaluated model performance using confusion matrices and classification reports to assess precision, recall, and F1-score.
- **Precision and Recall Curves**: Generated precision-recall and ROC curves to evaluate model performance at different threshold settings.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature scaling, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's pairplot and heatmap.
- **Visualized** class distributions to understand the balance of positive and negative heart disease cases.

### Model Implementation

- **Train-Test Split**: Divided the dataset into training (90%) and testing (10%) subsets to evaluate the model's generalizability.
- **Feature Scaling**: Standardized the feature data to remove bias due to differing feature ranges.
- **Logistic Regression Model**: Trained a logistic regression model to predict whether a patient is likely to have heart disease.

### Model Evaluation and Interpretation

- **Confusion Matrix**: Evaluated the model's accuracy in distinguishing between positive and negative cases.
- **Classification Report**: Provided detailed metrics including precision, recall, and F1-score for both classes (heart disease positive and negative).
- **Performance Curves**: Generated precision-recall and ROC curves to better understand the model's performance.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Confusion Matrix**: Shows the breakdown of true positives, false positives, true negatives, and false negatives.
- **Classification Report**: Precision, recall, and F1-scores for each class.
- **Prediction Example**: The model predicted whether a patient with given physical health metrics is likely to have heart disease, along with the probability of that prediction.

## Notes

This project demonstrates the application of logistic regression for predicting heart disease outcomes. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful and actionable insights from health data.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

