# Linear Regression Analysis of Foot Size Prediction

## Overview
This project aims to predict foot size ("pointure") based on height ("taille") using linear regression analysis. The dataset includes observations about individuals' height, foot size, and other relevant attributes. The project explores various statistical analyses, including univariate and bivariate analysis, and ultimately fits a linear regression model to predict foot size from height.

## Project Structure

1. **Univariate Analysis**
   - Explored key summary statistics for the "pointure" variable such as mean, median, and mode.
   - Investigated data dispersion using variance, standard deviation, and boxplots to detect outliers and aberrant values.
   - Cleaned and corrected identified outliers in the dataset.

2. **Bivariate Analysis**
   - Investigated the relationship between height and foot size using scatter plots and correlation coefficients.
   - Calculated covariance and the Pearson correlation coefficient to understand the relationship's strength and direction.

3. **Linear Regression Modeling**
   - Developed a linear regression model to predict foot size from height using scikit-learn's LinearRegression module.
   - Calculated model coefficients (β₀ and β₁) for foot size estimation.
   - Evaluated the model using metrics such as Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).

## Key Skills Demonstrated

- **Data Cleaning**: Handling missing values, removing outliers, and converting data types to ensure consistency.
- **Exploratory Data Analysis (EDA)**: Descriptive statistics to understand the distributions and identify patterns.
- **Bivariate Analysis**: Calculation and interpretation of covariance and correlation to understand the relationship between variables.
- **Linear Regression Modeling**: Building, training, and evaluating a simple regression model using Python.

## Technologies Used

- **Python**: Programming language for data analysis.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations and statistical calculations.
- **Matplotlib**: Data visualization for plotting boxplots and scatter plots.
- **Scikit-Learn**: Implementing the linear regression model and evaluating its performance.

## How to Run the Project

1. **Requirements**: Ensure Python is installed with the following libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
2. **Data File**: Place the dataset file (`Etudiants_TP.csv.txt`) in the working directory.
3. **Run the Code**: Execute the script using your preferred IDE or environment (e.g., Jupyter Notebook, Google Colab).

## Project Highlights

- **Outlier Detection and Handling**: Detected and replaced outliers to ensure the model's robustness.
- **Scatter Plot Analysis**: Visualized the relationship between height and foot size to confirm the linear trend.
- **Linear Model Evaluation**: Evaluated model accuracy using MSE and RMSE to determine how well height predicts foot size.

## Future Improvements

- **Feature Engineering**: Add more features such as "weight" or "age" for better predictions.
- **Advanced Modeling**: Explore non-linear regression models or machine learning techniques for enhanced accuracy.
- **Data Enrichment**: Collect more data to better generalize the findings.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for any questions or collaboration opportunities.