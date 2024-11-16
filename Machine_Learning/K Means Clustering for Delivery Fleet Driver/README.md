# K Means Clustering for Delivery Fleet Driver Data

## Overview

The K Means Clustering for Delivery Fleet Driver Data project is a Python-based machine learning implementation designed to group delivery drivers based on their driving behavior, such as average distance driven per day and speeding tendencies. This project applies k-means clustering, an unsupervised learning technique, to explore patterns and categorize drivers without prior labels.

The goal of this project is to identify natural groupings among drivers, which can be useful for optimizing fleet management, improving safety, and analyzing driver performance.

## Purpose

The purpose of this project is to:

- Implement a k-means clustering model to group drivers based on their driving characteristics.
- Explore relationships between driving features such as distance driven and speeding behavior.
- Showcase skills in data preprocessing, exploratory data analysis, and unsupervised learning using Python and scikit-learn.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize relationships between driver attributes, such as distance driven and speeding behavior, to identify potential clusters.

### Data Preprocessing

- **Handling Missing Values**: Checked for and handled any missing data to ensure data quality.
- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.

### Model Implementation and Evaluation

- **K Means Clustering Model**: Developed a k-means clustering model to group drivers based on selected features.
- **Cluster Analysis**: Evaluated the clustering results by analyzing cluster centers and interpreting the grouping of drivers.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature transformation, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's scatterplot, heatmap, and boxplot.
- **Visualized** relationships between features such as average daily distance and speeding behavior to understand patterns in driver characteristics.
- **Scatterplot**: Plotted relationships between `Speeding_Feature` and `Distance_Feature` to identify potential clusters.
- **Heatmap**: Created a heatmap to visualize the correlation between features and understand their relationships.

### Data Preprocessing

- **Feature Selection**: Selected relevant features (`Speeding_Feature`, `Distance_Feature`) for clustering analysis to simplify visualization and interpretation of results.
- **Feature Scaling**: Standardized the selected features to remove bias due to differing feature ranges.

### Model Implementation

- **K Means Clustering**: Implemented a k-means clustering model with `n_clusters=2` initially and used the elbow method to determine the optimal number of clusters.
- **Elbow Method**: Used the elbow method to evaluate the within-cluster sum of squares (WCSS) and identify the optimal number of clusters.
- **Final Model**: Trained a k-means model with `n_clusters=4` based on the elbow method's results.

### Model Evaluation and Interpretation

- **Cluster Centers**: Evaluated the centroids of the clusters to understand the average characteristics of each group.
- **Cluster Assignments**: Assigned labels to each driver, indicating which cluster they belong to based on their driving characteristics.
- **Cluster Visualization**: Visualized the clustering results, using scatterplots to compare the predicted cluster labels and understand groupings.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Cluster Centers**: Identified the average values for each feature in the clusters formed by the k-means model.
- **Cluster Assignments**: Assigned labels to each driver, indicating which cluster they belong to based on their driving behavior.
- **Scatterplot**: Visualized the clustering results, comparing the different clusters and their characteristics to assess the model's performance.

## Notes

This project demonstrates the application of k-means clustering for exploring and categorizing driver behavior data. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful groupings and insights in an unsupervised learning context.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

