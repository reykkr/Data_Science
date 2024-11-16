# Decision Trees and Random Forests Loan Repayment Prediction

## Overview

The Decision Trees and Random Forests Loan Repayment Prediction project is a Python-based machine learning implementation designed to predict whether a borrower will fully repay a loan based on various financial and credit-related features. This project uses lending data from LendingClub.com, focusing on loans issued between 2007-2010, and applies decision trees and random forests to build a classification model to predict loan repayment.

The goal of this project is to assist investors in identifying borrowers who are more likely to repay loans, thereby minimizing risks and optimizing investments.

## Purpose

The purpose of this project is to:

- Implement decision tree and random forest models to predict loan repayment.
- Explore relationships between financial attributes and loan repayment behavior.
- Showcase skills in data preprocessing, exploratory data analysis, and model evaluation using Python and scikit-learn.

## Key Features Demonstrated

### Data Analysis and Visualization

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions, relationships between features, and the presence of any missing values.
- **Visualization**: Created plots to visualize target distributions, relationships between loan purpose and repayment, and trends between FICO scores and interest rates.

### Data Preprocessing

- **Handling Categorical Features**: Converted categorical features like loan purpose into dummy variables using `pd.get_dummies()` to make the data compatible with machine learning models.
- **Train-Test Split**: Separated the dataset into training and testing sets to evaluate model performance effectively.

### Model Implementation and Evaluation

- **Decision Tree Model**: Developed a decision tree classifier to predict whether a borrower will fully repay a loan.
- **Random Forest Model**: Implemented a random forest classifier to improve prediction performance by leveraging multiple decision trees.
- **Model Evaluation**: Evaluated model performance using metrics such as confusion matrices, classification reports, precision, and recall.

## Tools Used

- **Python**: The programming language used for data handling, visualization, and model implementation.
- **Pandas and NumPy**: Used for data manipulation and numerical operations.
- **Seaborn and Matplotlib**: Employed to create visualizations for better understanding of data relationships.
- **scikit-learn**: Utilized for feature transformation, model building, and evaluation.

## Project Components

### Data Analysis and Visualization

- **Explored** the dataset's distributions and relationships using tools like Seaborn's countplot and jointplot.
- **Visualized** loan repayment distribution to understand the balance between fully paid and non-fully paid loans.
- **Countplot**: Plotted the relationship between loan purpose and repayment status to identify patterns.
- **Jointplot**: Examined the trend between FICO scores and interest rates to understand borrower risk levels.

### Data Preprocessing

- **Dummy Variables**: Created dummy variables for the categorical feature `purpose` to convert it into numerical form.
- **Train-Test Split**: Divided the dataset into training (70%) and testing (30%) subsets to evaluate the model's generalizability.

### Model Implementation

- **Decision Tree Classifier**: Trained a decision tree model to predict loan repayment outcomes.
- **Random Forest Classifier**: Trained a random forest model to improve prediction accuracy by combining multiple decision trees.

### Model Evaluation and Interpretation

- **Confusion Matrix**: Evaluated the model's accuracy in distinguishing between fully paid and non-fully paid loans.
- **Classification Report**: Provided detailed metrics including precision, recall, and F1-score for each class (fully paid, not fully paid).
- **Precision and Recall Scores**: Calculated precision and recall scores to assess model performance in identifying borrowers likely to default or repay.

## Example Output

After training and evaluating the models, the following outputs were generated:

- **Confusion Matrix**: Shows the breakdown of true positives, false positives, true negatives, and false negatives for loan repayment status.
- **Classification Report**: Precision, recall, and F1-scores for each class (fully paid, not fully paid).
- **Model Comparison**: Compared the performance of the decision tree and random forest models to determine which performed better in predicting loan repayment.

## Notes

This project demonstrates the application of decision trees and random forests for predicting loan repayment outcomes. It highlights how data preprocessing, model building, and evaluation can be used to create meaningful and actionable insights for investors looking to minimize risk.

## Author

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.

