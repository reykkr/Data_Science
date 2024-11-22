**Face Emotion Recognition: CNN vs MobileNetV2**

**Overview**

The "Face Emotion Recognition: CNN vs MobileNetV2" project is a deep learning-based implementation aimed at predicting emotions from facial images. The goal is to compare the performance of two models—a Convolutional Neural Network (CNN) and MobileNetV2—in recognizing different facial expressions.

Emotion detection from facial expressions has numerous applications, including human-computer interaction, market research, and mental health monitoring.

**Objective**

The objective of this project is to implement a program capable of predicting emotions based on facial images using deep learning models. We first implement a CNN and then MobileNetV2 on the same dataset, comparing the results of both models to evaluate their performance.

**Dataset Used**

We utilized the [FER 2013](https://www.kaggle.com/datasets/msambare/fer2013) dataset available on Kaggle. The dataset consists of 48x48 pixel grayscale images of faces, with each face categorized into one of seven emotion classes:

- 0 = Angry
- 1 = Disgust
- 2 = Fear
- 3 = Happy
- 4 = Sad
- 5 = Surprise
- 6 = Neutral

The training set consists of 28,709 examples, and the public test set consists of 3,589 examples.

**Data Exploration**

We began by importing the necessary libraries and exploring the dataset to visualize images representing each of the seven emotions. Data visualization helped us understand the distribution of data and assess the quality of the images.

**Data Preprocessing**

- **Data Augmentation**: We applied data augmentation to artificially expand the training set and introduce variability to improve model generalization.
- **Rescaling**: The images were rescaled by dividing by 255 to ensure all pixel values fell between 0 and 1.
- **Training and Validation Sets**: The data was split into training and validation sets for model evaluation.

**Model Implementations**

**CNN Model**

The CNN model was built with the following key features:

- **Sequential Architecture**: A series of convolutional layers with ReLU activation, followed by max pooling layers to downsample the data.
- **Batch Normalization and Dropout**: Used to stabilize training and prevent overfitting.
- **Fully Connected Layers**: Added at the end to classify the images into one of the seven emotion classes.
- **Optimizer**: The Adam optimizer was used for efficient gradient descent.

**MobileNetV2 Model**

The MobileNetV2 model was implemented to leverage its pre-trained convolutional layers for feature extraction. Since MobileNetV2 expects 3-channel input, we added a custom layer to repeat grayscale images into three channels. The model features:

- **Feature Extraction**: Used MobileNetV2's pre-trained layers with the addition of fully connected layers for classification.
- **Frozen Layers**: The base layers of MobileNetV2 were frozen to use the pre-trained weights effectively.

**Model Training and Evaluation**

Both models were trained for 100 epochs using the same training and validation sets. The following metrics were used for evaluation:

- **Training and Validation Accuracy**: Tracked to identify overfitting and underfitting issues.
- **Confusion Matrix**: Evaluated the model's performance across different emotion classes.

**Results and Comparison**

- **CNN Model**: Achieved 96% training accuracy and 64% validation accuracy. The model performed relatively well in predicting most emotions but struggled with classes like "angry" and "fear" due to limited data.
- **MobileNetV2 Model**: Achieved 92% training accuracy and 42% validation accuracy. It had difficulty predicting emotions consistently, especially in the "angry" and "fear" classes.
- **Confusion Matrices**: Visualized the accuracy across different classes for both models, showing that the CNN outperformed MobileNetV2 in predicting most emotions.

**Testing**

Both models were tested using sample images, with the CNN model achieving better accuracy compared to MobileNetV2. The CNN correctly predicted 62.5% of the test images, while MobileNetV2 only predicted 12.5% correctly.

**Conclusions**

- **CNN Performance**: The CNN model was able to achieve better validation accuracy and generalization compared to MobileNetV2. The model also performed well in predicting emotions from individual images.
- **MobileNetV2 Performance**: Despite leveraging transfer learning, MobileNetV2 struggled due to the small dataset size and the challenge of adapting from color to grayscale images.
- **Future Work**: Improving the dataset quality and size and tuning hyperparameters could help enhance the performance of both models, particularly MobileNetV2.

**Authors**

- Mohamad Ali Ghaddar
- Juste Bankumukunwi
- Ali Abdallah

Feel free to reach out for collaboration or if you have any questions about this project.