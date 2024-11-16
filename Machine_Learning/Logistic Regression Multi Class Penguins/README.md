# Multi-Class Logistic Regression Penguin Species Prediction

## Overview

The Multi-Class Logistic Regression Penguin Species Prediction project is a Python-based machine learning implementation designed to predict the species of a penguin based on various physical measurements. This project uses the Palmer Penguins dataset and applies logistic regression to build a multi-class classification model to distinguish between three penguin species: Adelie, Gentoo, and Chinstrap.

The goal of this project is to explore the relationships between body measurements such as bill length, bill depth, flipper length, and body mass, and to predict the species of a penguin efficiently and accurately.

## Purpose

The purpose of this project is to:

- Implement a logistic regression model to predict the species of a penguin.
- Explore the relationships between physical attributes and penguin species classification.
- Showcase skills in data preprocessing, exploratory data analysis, and model evaluation using Python and scikit-learn.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize target distributions, pairwise relationships, and feature correlations, aiding in better understanding of the data.

### Data Preprocessing

- **Handling Missing Values**: Dropped rows with missing values to ensure data quality.
- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.
- **Train-Test Split**: Separated the dataset into training and testing sets to evaluate model performance effectively.

### Model Implementation and Evaluation

- **Multi-Class Logistic Regression Model**: Developed a logistic regression model using scikit-learn to classify penguins into one of the three species.
- **Model Coefficients**: Calculated and interpreted the model's coefficients to understand the impact of each feature on the outcome.

### Evaluation Metrics

- **Confusion Matrix and Classification Report**: Evaluated model performance using confusion matrices and classification reports to assess precision, recall, and F1-score for each species.
- **ROC Curves**: Generated ROC curves for each class to evaluate model performance.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature scaling, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's pairplot and heatmap.
- **Visualized** class distributions to understand the balance between the three penguin species.
- **Scatter Plots**: Plotted relationships between features such as flipper length, body mass, bill depth, and bill length to understand feature separability.

### Model Implementation

- **Train-Test Split**: Divided the dataset into training (75%) and testing (25%) subsets to evaluate the model's generalizability.
- **Feature Scaling**: Standardized the feature data to remove bias due to differing feature ranges.
- **Multi-Class Logistic Regression Model**: Trained a logistic regression model to predict the species of a penguin.

### Model Evaluation and Interpretation

- **Confusion Matrix**: Evaluated the model's accuracy in distinguishing between the three penguin species.
- **Classification Report**: Provided detailed metrics including precision, recall, and F1-score for each species (Adelie, Chinstrap, Gentoo).
- **ROC Curves**: Generated ROC curves to better understand the model's performance for each class.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Confusion Matrix**: Shows the breakdown of true positives, false positives, true negatives, and false negatives for each species.
- **Classification Report**: Precision, recall, and F1-scores for each class.
- **Prediction Example**: The model predicted the species of a penguin with given physical measurements, along with the probability of that prediction.

## Notes

This project demonstrates the application of multi-class logistic regression for predicting penguin species. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful and actionable insights from ecological data.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.