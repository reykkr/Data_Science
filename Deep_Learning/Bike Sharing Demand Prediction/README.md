**Neural Network from Scratch: Bike Sharing Demand Prediction**

**Overview**

The "Neural Network from Scratch: Bike Sharing Demand Prediction" project is a Python-based implementation of a neural network aimed at predicting the demand for bike rentals in a bike-sharing system. This project involves building a neural network from scratch using NumPy, followed by an implementation using PyTorch to improve the model's performance. The goal is to predict the number of bikes required at different times to optimize availability, thereby reducing customer dissatisfaction due to bike shortages.

This project utilizes the Bike Sharing Dataset provided by the UCI Machine Learning Laboratory, covering hourly and daily rental counts along with corresponding weather and seasonal information.

**Purpose**

The purpose of this project is to:

- Develop a neural network from scratch to predict bike demand using both NumPy and PyTorch.
- Understand the impact of weather, time, and seasonal variables on bike rental demand.
- Showcase skills in data preprocessing, exploratory data analysis, and implementing neural network models.

**Key Features Demonstrated**

**Data Analysis and Visualization**

- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand distributions and relationships between features such as weather, time, and bike rental counts.
- **Visualization**: Created visual representations, including count plots and trends, to better understand the data and improve model performance.

**Data Preprocessing**

- **One-Hot Encoding**: Converted categorical variables, such as weather and time, into dummy variables for compatibility with the neural network.
- **Train-Test Split**: Split the data into training, validation, and testing sets to evaluate model performance effectively.
- **Normalization**: Normalized continuous variables to have a mean of 0 and standard deviation of 1 to simplify network training.

**Model Implementation and Evaluation**

- **Neural Network Design**: Implemented a neural network from scratch using NumPy with an input layer, a hidden layer, and an output layer.
- **Backpropagation and Feedforward**: Implemented the forward and backward propagation algorithms to train the model.
- **PyTorch Implementation**: Developed a neural network using PyTorch to enhance model accuracy and reduce validation loss.
- **Model Evaluation**: Evaluated the model using loss functions, comparing training and validation losses to identify overfitting and analyze model performance.

**Tools Used**

- **Python**: The programming language used for data preprocessing, model building, and evaluation.
- **NumPy and Pandas**: Utilized for data manipulation and numerical operations.
- **Matplotlib**: Employed to visualize the model's predictions and analyze training and validation losses.
- **PyTorch**: Used to create a more sophisticated neural network with improved accuracy.

**Project Components**

**Data Analysis and Visualization**

- Analyzed the bike-sharing dataset to understand rental demand in different conditions.
- Created plots to explore relationships between features such as weather and rental counts.

**Data Preprocessing**

- **One-Hot Encoding**: Created dummy variables for categorical features like season, weather, and time.
- **Normalization**: Normalized continuous variables for efficient network training.
- **Splitting Data**: Divided the data into training, validation, and testing sets.

**Model Implementation**

- **NumPy Neural Network**: Implemented a neural network from scratch with a single hidden layer using NumPy.
- **PyTorch Neural Network**: Created an improved neural network using PyTorch, with reduced validation loss compared to the NumPy model.

**Model Evaluation and Interpretation**

- **Training and Validation Losses**: Compared losses during training to identify overfitting.
- **Predictions**: Visualized model predictions against actual rental counts to assess accuracy.
- **PyTorch vs. NumPy**: Compared the performance of the PyTorch model against the NumPy implementation, noting improved accuracy and lower validation loss with PyTorch.

**Example Output**

- **Training and Validation Losses**: Plots showing the model's progress during training, highlighting overfitting and generalization capabilities.
- **Predicted vs. Actual Rentals**: Line plots comparing predicted and actual bike rental counts to assess prediction accuracy.

**Notes**

This project demonstrates the process of building a neural network from scratch, highlighting the importance of data preprocessing, loss function evaluation, and model training. It also shows how transitioning from a NumPy implementation to PyTorch can lead to performance improvements in terms of reduced loss and increased accuracy.

**Author**

Mohamad Ali Ghaddar

Feel free to reach out for collaboration or if you have any questions about this project.