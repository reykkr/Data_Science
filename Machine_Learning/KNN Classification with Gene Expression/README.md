# K Nearest Neighbors (KNN) Classification with Gene Expression Data

## Overview

The K Nearest Neighbors (KNN) Classification project is a machine learning implementation designed to classify data points representing gene expression levels to predict whether a patient has cancer. Gene expression levels are calculated by the ratio between the expression of a target gene and reference genes, often used to determine the presence of diseases such as cancer. This project utilizes a synthetic gene expression dataset designed to illustrate the strengths and limitations of KNN for classification.

The goal of this project is to develop a model that can accurately predict the presence of cancer based on gene expression levels, demonstrating the use of KNN in biological and medical contexts.

## Purpose

The purpose of this project is to:

- Implement a KNN classification model to predict the presence of cancer based on gene expression features.
- Explore relationships between gene expression levels and understand how different features contribute to classification.
- Showcase skills in data preprocessing, exploratory data analysis, and supervised learning using Python and scikit-learn.

## Method Used

K Nearest Neighbors is a supervised learning algorithm that classifies a data point based on its proximity to other labeled points. It calculates the distance between points and assigns a class based on the majority class of the nearest neighbors.

The steps involved are:

1. **Standardization**: Standardize the features to remove the impact of varying scales.
2. **Distance Calculation**: Use distance metrics (such as Euclidean distance) to identify the nearest neighbors.
3. **Class Assignment**: Assign a class to the new data point based on the majority class of its neighbors.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created scatterplots, countplots, and heatmaps to visualize the relationships between features and the target class.

### Data Preprocessing

- **Handling Missing Values**: Checked for and handled any missing data to ensure data quality.
- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.

### Model Implementation and Evaluation

- **KNN Classification Model**: Developed a KNN model to predict cancer presence based on the nearest neighbors.
- **Elbow Method**: Used the elbow method to identify the optimal value for `k` by plotting the error rate for different `k` values.
- **Model Evaluation**: Evaluated model performance using confusion matrices, classification reports, and accuracy metrics.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature transformation, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's scatterplot, countplot, and heatmap.
- **Visualized** relationships between gene expression levels to understand patterns and separability between target classes.
- **Scatterplot**: Plotted relationships between gene expression features (`Gene One` and `Gene Two`), with points colored by cancer presence to identify separability between classes.
- **Heatmap**: Created a heatmap to visualize the correlation between features and understand their relationships.

### Data Preprocessing

- **Feature Scaling**: Standardized the features to ensure that variables on different scales contribute equally to the model's distance calculations.

### Model Implementation

- **Train-Test Split**: Split the dataset into training and testing subsets to evaluate the model's generalizability.
- **KNN Model Creation**: Implemented a KNN model using `n_neighbors=1` initially, and then used different values of `k` to determine the optimal parameter.
- **Elbow Method**: Evaluated different values of `k` by calculating the error rate and plotting it to identify the optimal number of neighbors.

### Model Evaluation and Interpretation

- **Confusion Matrix**: Evaluated the model's accuracy by generating a confusion matrix for the test set predictions.
- **Classification Report**: Provided detailed metrics including precision, recall, and F1-score for each class.
- **Optimal `k` Selection**: Used the elbow method to determine the best value for `k`, retrained the model, and reevaluated its performance.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Confusion Matrix**: Shows the breakdown of true positives, false positives, true negatives, and false negatives for each target class.
- **Classification Report**: Precision, recall, and F1-scores for each class.
- **Error Rate Plot**: Plotted the error rate vs. `k` value to identify the optimal number of neighbors.
- **Final Model with Optimal `k`**: Retrained the model with the optimal `k` value and evaluated its performance to achieve improved accuracy.

## Notes

This project demonstrates the application of K Nearest Neighbors for classifying gene expression data to predict cancer presence. It highlights how data preprocessing, model building, and evaluation can be used to create a robust classification model in a supervised learning context, particularly in biological and medical data analysis.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

