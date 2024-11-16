# Linear Regression on Ames Housing Dataset

## Overview
In this project, we use the Ames Housing dataset to build a Linear Regression model to predict house prices. The goal is to train an Elastic Net regression model using optimal parameters, which we determine through a Grid Search strategy, and evaluate its performance on a test set.

## Project Structure

1. **Data Loading and Preprocessing**
   - Loaded the Ames Housing dataset.
   - Cleaned the data by removing unnecessary columns (`Unnamed: 0.1` and `Unnamed: 0`).
   - Split the dataset into features (`X`) and labels (`y`), where `SalePrice` is the target label.

2. **Data Splitting**
   - Split the data into training and test sets using a 90/10 split, with a random state for reproducibility (`random_state=101`).

3. **Data Scaling**
   - Scaled the feature set (`X`) using `StandardScaler` to normalize features with different units and scales.
   - Fit the scaler on the training set and transformed both the training and test features.

4. **Model Selection**
   - Chose an Elastic Net model as the base regression model.
   - Defined a parameter grid for the Elastic Net model to determine the optimal values for the parameters `alpha`, `l1_ratio`, and `normalize`.

5. **Grid Search for Optimal Parameters**
   - Used `GridSearchCV` to perform a 5-fold cross-validation and find the optimal parameters based on negative mean squared error.

6. **Model Training and Evaluation**
   - Trained the Elastic Net model using the scaled training data and the best parameters obtained from Grid Search.
   - Evaluated the model on the unseen 10% test set using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Key Skills Demonstrated
- **Data Cleaning and Feature Selection**: Removed unnecessary columns, split features and labels, and scaled the data appropriately.
- **Data Splitting**: Used scikit-learn to create training and test datasets for model validation.
- **Feature Scaling**: Applied `StandardScaler` to ensure features were on the same scale, which is critical for optimal regression performance.
- **Model Training with Elastic Net**: Implemented an Elastic Net model, which combines Ridge and Lasso regression to handle multicollinearity and select features.
- **Hyperparameter Tuning**: Used `GridSearchCV` to optimize model parameters by finding the best combination of `alpha`, `l1_ratio`, and `normalize`.
- **Model Evaluation**: Evaluated model performance on the test set using metrics like MAE, MSE, and RMSE.

## Technologies Used
- **Python**: Programming language for data processing and modeling.
- **Pandas**: Data manipulation and exploration.
- **NumPy**: Numerical calculations and operations.
- **scikit-learn**: Machine learning library used for model training, evaluation, and hyperparameter tuning.
- **Matplotlib & Seaborn**: Data visualization (if used to explore data).

## How to Run the Project
1. **Requirements**: Ensure you have Python installed with the following libraries:
   - `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
2. **Data File**: Place the dataset file (`AMES_Final_DF.csv`) in the working directory.
3. **Run the Code**: Execute the script in your preferred IDE or environment (e.g., Jupyter Notebook, Google Colab).

## Project Highlights
- **Elastic Net Implementation**: Trained an Elastic Net model, combining Lasso and Ridge regression to balance feature selection and model regularization.
- **Hyperparameter Optimization**: Used Grid Search to determine the optimal parameters for improving model accuracy.
- **Performance Metrics**: Evaluated the model on a test set using key metrics to understand its predictive power on unseen data.

## Results
The best parameters found through Grid Search were as follows:
- `alpha`: Optimal regularization strength.
- `l1_ratio`: Balance between Lasso and Ridge penalty.
- `normalize`: Whether or not the data should be normalized.

The model evaluation on the test set yielded:
- **MAE**: Mean Absolute Error value.
- **MSE**: Mean Squared Error value.
- **RMSE**: Root Mean Squared Error value, which provides an indication of model accuracy.

## Future Improvements
- **Feature Engineering**: Explore additional feature engineering to improve model accuracy.
- **Model Comparison**: Compare with other regression models such as Ridge, Lasso, or even non-linear models to see if better performance can be achieved.
- **Residual Analysis**: Analyze residuals to better understand model limitations and potential improvements.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for any questions or collaboration opportunities.