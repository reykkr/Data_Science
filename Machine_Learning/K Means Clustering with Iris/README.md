# K Means Clustering with Python - Iris Data Set

## Overview

The K Means Clustering with Python project is a machine learning implementation designed to group different species of flowers based on their physical measurements, such as sepal and petal length and width. This project utilizes the classic Iris Data Set, which consists of three flower species: Iris Setosa, Iris Versicolor, and Iris Virginica. K-means clustering, an unsupervised learning algorithm, is used to explore patterns and categorize the flowers without prior labels.

The goal of this project is to develop a model that can predict the species of a flower based on its measurements, reducing the need for human intervention in species identification.

## Purpose

The purpose of this project is to:

- Implement a k-means clustering model to group flowers based on their features.
- Explore relationships between flower features such as petal length, petal width, sepal length, and sepal width.
- Showcase skills in data preprocessing, exploratory data analysis, and unsupervised learning using Python and scikit-learn.

## Method Used

K Means Clustering is an unsupervised learning algorithm that tries to cluster data based on their similarity. In k-means clustering, we have to specify the number of clusters we want the data to be grouped into. The algorithm randomly assigns each observation to a cluster and finds the centroid of each cluster. Then, the algorithm iterates through two steps:

1. Reassign data points to the cluster whose centroid is closest.
2. Calculate the new centroid of each cluster.

These two steps are repeated until the within-cluster variation cannot be reduced any further. The within-cluster variation is calculated as the sum of the Euclidean distance between the data points and their respective cluster centroids.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize the relationships between flower attributes to identify potential clusters.

### Data Preprocessing

- **Handling Missing Values**: Checked for and handled any missing data to ensure data quality.
- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.

### Model Implementation and Evaluation

- **K Means Clustering Model**: Developed a k-means clustering model to group flowers based on selected features.
- **Cluster Analysis**: Evaluated the clustering results by analyzing cluster centers and interpreting the grouping of flowers.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature transformation, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's countplot, pairplot, and heatmap.
- **Visualized** relationships between features such as petal length, petal width, sepal length, and sepal width to understand patterns in flower characteristics.
- **Pairplot**: Plotted relationships between all columns, with points colored by species, to identify separability between flower species.
- **Heatmap**: Created a heatmap to visualize the correlation between features and understand their relationships.

### Data Preprocessing

- **Feature Selection**: Selected relevant features (`petal_length`, `petal_width`) for clustering analysis to simplify visualization and interpretation of results.
- **Feature Scaling**: Standardized the selected features to remove bias due to differing feature ranges.

### Model Implementation

- **K Means Clustering**: Implemented a k-means clustering model with `n_clusters=3` to identify groupings among the flower species.
- **Elbow Method**: Used the elbow method to evaluate the within-cluster sum of squares (WCSS) and identify the optimal number of clusters.
- **Final Model**: Trained a k-means model with `n_clusters=3` based on the elbow method's results.

### Model Evaluation and Interpretation

- **Cluster Centers**: Evaluated the centroids of the clusters to understand the average characteristics of each group.
- **Cluster Assignments**: Assigned labels to each flower, indicating which cluster they belong to based on their features.
- **Cluster Visualization**: Visualized the clustering results using scatterplots to compare the predicted cluster labels and the actual species labels.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Cluster Centers**: Identified the average values for each feature in the clusters formed by the k-means model.
- **Cluster Assignments**: Assigned labels to each flower, indicating which cluster they belong to based on their measurements.
- **Scatterplot**: Visualized the clustering results, comparing the different clusters and their characteristics to assess the model's performance.

## Notes

This project demonstrates the application of k-means clustering for exploring and categorizing different flower species based on their measurements. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful groupings and insights in an unsupervised learning context.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

