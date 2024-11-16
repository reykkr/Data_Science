# K Means Clustering for University Data

## Overview

The K Means Clustering for University Data project is a Python-based machine learning implementation designed to group universities based on various attributes, such as student enrollment, tuition costs, and faculty characteristics. This project applies k-means clustering, an unsupervised learning technique, to explore patterns and categorize universities without prior labels.

The goal of this project is to identify natural groupings among universities, which can be useful for understanding similarities in educational offerings and costs.

## Purpose

The purpose of this project is to:

- Implement a k-means clustering model to group universities based on their characteristics.
- Explore relationships between university features such as tuition costs, graduation rates, and student demographics.
- Showcase skills in data preprocessing, exploratory data analysis, and unsupervised learning using Python and scikit-learn.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize relationships between university attributes, such as student enrollment and out-of-state tuition, and faculty characteristics.

### Data Preprocessing

- **Handling Categorical Features**: Converted categorical features like `Private` into numerical form to make the data compatible with machine learning models.
- **Feature Scaling**: Standardized the data using `StandardScaler` to ensure that all features contribute equally to the model.

### Model Implementation and Evaluation

- **K Means Clustering Model**: Developed a k-means clustering model to group universities based on selected features.
- **Cluster Analysis**: Evaluated the clustering results by comparing cluster labels with known attributes like public vs. private universities.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature transformation, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's scatterplot and histogram.
- **Visualized** relationships between features such as full-time undergraduate enrollment, out-of-state tuition, and graduation rates to understand patterns in university characteristics.
- **Scatterplot**: Plotted relationships between features such as `F.Undergrad` and `Outstate` to understand differences between public and private universities.
- **Histograms**: Created histograms of features like `PhD` and `Grad.Rate` to examine their distributions across different types of universities.

### Data Preprocessing

- **Categorical Encoding**: Converted the `Private` column into numerical values (0 for `No`, 1 for `Yes`) to make it compatible with the k-means algorithm.
- **Feature Selection**: Selected relevant features (`F.Undergrad`, `Enroll`) for clustering analysis to simplify visualization and interpretation of results.

### Model Implementation

- **K Means Clustering**: Implemented a k-means clustering model with `n_clusters=2` to identify groupings among universities.
- **Elbow Method**: Used the elbow method to determine the optimal number of clusters by evaluating the within-cluster sum of squares (WCSS).

### Model Evaluation and Interpretation

- **Cluster Centers**: Evaluated the centroids of the clusters to understand the average characteristics of each group.
- **Cluster Assignments**: Analyzed the assigned cluster labels and compared them with the original `Private` column to assess how well the clustering model captured known groupings.

## Example Output

After training and evaluating the model, the following outputs were generated:

- **Cluster Centers**: Identified the average values for each feature in the two clusters formed by the k-means model.
- **Cluster Assignments**: Assigned labels to each university, indicating which cluster they belong to based on their characteristics.
- **Scatterplot**: Visualized the clustering results, comparing the predicted cluster labels with the original `Private` labels to assess the model's performance.

## Notes

This project demonstrates the application of k-means clustering for exploring and categorizing university data. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful groupings and insights in an unsupervised learning context.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

