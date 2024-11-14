# SMS Spam Classifier

## Overview
The **SMS Spam Classifier** project is a machine learning application that uses natural language processing (NLP) techniques to classify SMS messages as either 'ham' (not spam) or 'spam'. This project is part of my journey through **freeCodeCamp**'s machine learning curriculum, focusing on text classification using deep learning with **TensorFlow** and **Keras**.

The dataset used contains SMS messages labeled as 'ham' or 'spam'. The primary goal is to develop a model that can accurately distinguish between legitimate messages and spam.

## Purpose
The purpose of this project is to:

- Develop a deep learning model capable of classifying SMS messages as 'ham' or 'spam'.
- Apply text preprocessing techniques to prepare the SMS messages for modeling.
- Demonstrate skills in building, training, and evaluating a text classification model using **TensorFlow** and **Keras**.

## Key Skills Demonstrated
1. **Data Preprocessing**
   - Encoded categorical labels ('ham' and 'spam') into numerical values to facilitate model training.
   - Tokenized text messages using **TokenTextEncoder** to convert words into numerical representations.
   - Applied sequence padding to ensure all message sequences are of the same length.

2. **Deep Learning Model Construction**
   - Built a deep learning model using **TensorFlow** and **Keras** with an **Embedding** layer to handle the text input.
   - Added **GlobalAveragePooling1D** and **Dense** layers to construct a classification model with efficient text representation.

3. **Model Training and Evaluation**
   - Compiled the model with the **Adam** optimizer and **binary cross-entropy** loss function.
   - Trained the model with the training dataset and validated it on the test dataset, achieving good classification accuracy.

4. **Prediction Function**
   - Implemented a prediction function to classify new SMS messages, returning the predicted probability and corresponding label ('ham' or 'spam').

## Tools Used
- **Python**: Data preprocessing, model building, and evaluation.
- **TensorFlow & Keras**: Implementation of the deep learning classification model.
- **Pandas & NumPy**: Data handling and analysis.
- **TensorFlow Datasets**: Text tokenization and encoding.
- **Matplotlib**: Visualizing model training metrics.

## Project Components
1. **Data Preprocessing**
   - Loaded the training and validation datasets from TSV files.
   - Encoded the message labels ('ham' and 'spam') as **0** and **1** respectively.
   - Tokenized the messages and converted them into sequences using **TokenTextEncoder**.
   - Padded the sequences to ensure uniform input length for the model.

2. **Model Construction**
   - Built a sequential model with an **Embedding** layer to learn word representations.
   - Added a **GlobalAveragePooling1D** layer for dimensionality reduction, followed by **Dense** layers for classification.
   - Used a **sigmoid** activation function in the output layer to predict the probability of a message being 'spam'.

3. **Model Training**
   - Trained the model for **10 epochs** using the **binary cross-entropy** loss function.
   - Evaluated the model on the test dataset to assess its performance.

4. **Evaluation and Predictions**
   - Implemented the `predict_message()` function to classify new SMS messages based on the trained model.
   - Tested the model on a variety of sample messages to validate its effectiveness.

## Example Output
After training the model, an example output for classifying a sample SMS message is:

```python
pred_text = "how are you doing today?"
prediction = predict_message(pred_text)
print(prediction)
```
Returns:
```
[0.0083, 'ham']
```
This indicates a low probability of the message being spam, correctly classifying it as 'ham'.

## Notes
This project demonstrates the application of deep learning for text classification tasks such as identifying spam messages. By applying text preprocessing, embedding layers, and effective model construction, the model successfully classifies SMS messages with satisfactory accuracy.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.