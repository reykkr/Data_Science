# Healthcare Cost Prediction

## Overview
The **Healthcare Cost Prediction** project is a machine learning application that utilizes regression techniques to predict healthcare costs based on various features of patients. This project is part of my journey through **freeCodeCamp**'s machine learning curriculum and aims to achieve accurate cost predictions using a deep learning model built with **TensorFlow** and **Keras**.

The dataset used contains information about patients, including attributes such as age, gender, smoking status, and region. The primary goal is to predict healthcare expenses based on these features.

## Purpose
The purpose of this project is to:

- Develop a deep learning model capable of predicting healthcare costs with a low mean absolute error.
- Apply data preprocessing techniques to prepare the dataset for modeling.
- Demonstrate skills in building, training, and evaluating a regression model using **TensorFlow** and **Keras**.

## Key Skills Demonstrated
1. **Data Preprocessing**
   - Converted categorical features such as **sex**, **smoker**, and **region** into numerical values to enable model training.
   - Standardized features using **StandardScaler** to improve model convergence.
   - Removed outliers based on **z-scores** to enhance model accuracy.

2. **Deep Learning Model Construction**
   - Built a deep regression model using **TensorFlow** and **Keras** with multiple hidden layers and **Batch Normalization** for stable training.
   - Applied **LeakyReLU** activation functions to address vanishing gradient issues.

3. **Model Training and Evaluation**
   - Used **EarlyStopping** and **ReduceLROnPlateau** callbacks to optimize training and prevent overfitting.
   - Evaluated the model on unseen data, achieving a mean absolute error (MAE) of less than **3500** to meet the project requirements.

## Tools Used
- **Python**: Data preprocessing, model building, and evaluation.
- **TensorFlow & Keras**: Implementation of the deep learning regression model.
- **Pandas & NumPy**: Data handling and analysis.
- **Matplotlib**: Visualizing model predictions.
- **scikit-learn**: Data splitting, scaling, and outlier removal.

## Project Components
1. **Data Preprocessing**
   - The dataset was preprocessed to convert categorical features into numerical values, including **sex**, **smoker**, and **region**.
   - Standardized features using **StandardScaler** to ensure consistent scaling, improving model training efficiency.
   - Removed outliers by filtering **z-scores** greater than 3 to avoid skewing the model's predictions.

2. **Model Construction**
   - Built a deep learning model with multiple layers using **Dense** and **Batch Normalization** layers.
   - Used **LeakyReLU** activation functions to improve gradient flow through the model.
   - Compiled the model using the **Adam** optimizer with a low learning rate to stabilize training.

3. **Model Training**
   - Trained the model with **1000 epochs** using **EarlyStopping** to stop training when validation loss stopped improving.
   - Reduced the learning rate during training if the validation loss plateaued using **ReduceLROnPlateau**.

4. **Evaluation and Predictions**
   - Evaluated the model on the test dataset to determine the **mean absolute error (MAE)**.
   - Generated predictions for the test set and visualized the relationship between true and predicted values using a scatter plot.

## Example Output
After training the model, an example output for evaluating the test dataset is:

```
Testing set Mean Abs Error: 3420.56 expenses
You passed the challenge. Great job!
```

The model was able to meet the requirement of achieving an MAE under **3500**, demonstrating effective cost prediction.

## Notes
This project demonstrates the application of deep learning for regression tasks such as predicting healthcare costs. By applying data preprocessing, effective model construction, and training strategies, the model successfully predicts healthcare expenses with a satisfactory level of accuracy.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.