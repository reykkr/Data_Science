# Cats and Dogs Image Classifier

## Overview
The **Cats and Dogs Image Classifier** is a deep learning project that uses a convolutional neural network (CNN) to distinguish between images of cats and dogs. This project is part of my machine learning journey through **freeCodeCamp** and leverages transfer learning to achieve classification accuracy.

The dataset used includes labeled images of cats and dogs, and the model is trained to predict whether a given image belongs to one of these two categories.

## Purpose
The purpose of this project is to:

- Develop a CNN-based image classifier capable of distinguishing between cats and dogs.
- Gain practical experience with convolutional neural networks for image classification tasks.
- Demonstrate skills in image augmentation, model building, training, and evaluation.

## Key Skills Demonstrated
1. **Data Preprocessing and Augmentation**
   - Performed data augmentation using **ImageDataGenerator** to improve the generalization ability of the model.
   - Rescaled images and used techniques like **rotation**, **width/height shift**, and **horizontal flip** to artificially expand the training dataset.

2. **Convolutional Neural Networks**
   - Built a CNN model using **TensorFlow** and **Keras**, which includes several layers such as **Convolution**, **MaxPooling**, **Flatten**, and **Dense** layers.

3. **Model Training and Evaluation**
   - Used early stopping to avoid overfitting during training.
   - Evaluated model performance on both training and validation datasets, analyzing metrics such as **accuracy** and **loss**.

## Tools Used
- **Python**: Image processing, model building, and evaluation.
- **TensorFlow & Keras**: Neural network implementation and training.
- **Pandas & NumPy**: Data handling and processing.
- **Matplotlib**: Visualizing training metrics and prediction outcomes.

## Project Components
1. **Dataset Preparation**
   - Downloaded the dataset, which included separate training, validation, and test sets for both cats and dogs.
   - Restructured the test set to contain all images in a single subdirectory for easier evaluation.

2. **Image Augmentation**
   - Utilized **ImageDataGenerator** to create augmented versions of the training images, applying transformations such as **rotations**, **zoom**, and **flips** to improve model generalization.

3. **Model Construction**
   - Built a sequential model using **Keras**, with three sets of **Conv2D** and **MaxPooling2D** layers followed by a fully connected layer with **Dense** nodes and a final **sigmoid** output layer.

4. **Model Training**
   - The model was trained for up to **30 epochs** with an early stopping callback that restored the best weights based on validation loss.
   - Evaluated the model's performance on the validation dataset to track **accuracy** and **loss**.

5. **Evaluation and Predictions**
   - Generated predictions for the test dataset and evaluated model performance.
   - Created visualizations to compare the **true labels** with the **predicted labels**, displaying both the predicted probability and the label (cat/dog).

## Example Output
```python
# Generate predictions for a test image
probabilities = model.predict(test_data_gen, steps=len(test_data_gen), verbose=1).flatten()
```
Returns:
```
- Probability: 95.2% (Dog)
- Actual Label: Dog
```
This classifier correctly identified over **63%** of the test images, meeting the challenge requirements.

## Notes
This project showcases the power of deep learning for binary classification tasks such as distinguishing between cats and dogs. By applying **data augmentation**, **transfer learning**, and effective training strategies, the model achieved satisfactory accuracy for this image classification challenge.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.

