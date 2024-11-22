# Dog Breed Classification using Transfer Learning

**Overview**

This project involves building a convolutional neural network (CNN) to classify dog breeds using transfer learning. We leverage a pre-trained ResNet50 model from ImageNet to first detect dogs in images and then classify the breeds. The project demonstrates the application of transfer learning, data preprocessing, and model training using deep learning techniques.

**Step 1: Import Dataset**

The dataset used for this project is a collection of dog images, organized into separate folders for each breed. The dataset should be placed in the directory `/dogs`, which contains training, validation, and testing sets. The dataset is loaded using the `glob` and `torchvision` libraries, allowing us to manage and preprocess images efficiently.

- **Dataset Link**: The dataset can be accessed and downloaded from [this Google Drive link](https://drive.google.com/drive/folders/1Epe3QZW7b0DuY87QCQqRdKBNcndUGuaK?usp=drive_link).

**Step 2: Detect Dogs using ResNet50**

The first step is to detect whether an image contains a dog. We use a pre-trained ResNet50 model, which is trained on ImageNet with 1000 categories. The model is downloaded, and we use it to predict the class index of the input image. The model is moved to GPU for faster processing if CUDA is available.

- **Dog Detector Function**: The `dog_detector` function is designed to return `True` if a dog is detected in an image. The function checks if the predicted class index is within the range corresponding to dog breeds (151-268).

**Step 3: CNN for Dog Breed Classification using Transfer Learning**

**Data Loaders**

Three separate data loaders are defined for the training, validation, and test datasets. Image augmentation techniques like resizing, cropping, horizontal flipping, and random rotation are applied to enhance the model's generalization capability.

**Model Architecture**

Transfer learning is used to create a CNN for dog breed classification. We use the ResNet50 model and replace its fully connected layer to output 133 classes, representing different dog breeds. All other layers are frozen to retain the learned features from ImageNet.

- **Model Initialization**: The model is initialized with pre-trained weights, and only the final fully connected layer is trainable to adapt the model to our dataset of dog breeds.

**Training Process**

- **Loss Function**: Cross-entropy loss is used as the criterion for classification.
- **Optimizer**: Stochastic gradient descent (SGD) is used to optimize the model parameters with a learning rate of 0.01.
- **Training and Validation**: The model is trained for 10 epochs, during which training and validation losses are monitored. The model parameters are saved whenever the validation loss improves.

**Testing the Model**

The trained model is evaluated on the test set to calculate the test loss and accuracy. This provides an indication of the model's generalization capability on unseen data.

**Dog Breed Prediction Function**

A function is defined to predict the breed of a dog from an input image. The image is preprocessed using the same transformations as the training data and then passed through the trained model to obtain the predicted breed.

**Dog Detection using YOLOv5**

In addition to the ResNet50 model, we use YOLOv5 to detect dogs in images. YOLOv5 is a state-of-the-art object detection model that can detect multiple objects in an image and draw bounding boxes around them. The detected dogs are then classified using our trained model to determine their breed.

- **YOLOv5 Integration**: The YOLOv5 model is used to detect dogs in the input image, and the detected dogs are then cropped and passed to the breed classification model.
- **Visualization**: The detected dogs are annotated with bounding boxes, and their predicted breeds are displayed to provide a complete solution for both detection and classification.

**Results**

The project successfully demonstrates the use of transfer learning for dog breed classification. By leveraging a pre-trained ResNet50 model and a YOLOv5 detector, the system is capable of detecting and classifying dog breeds accurately. The integration of YOLOv5 adds robustness by allowing the model to work on images with multiple dogs.

**Conclusion**

This project showcases the power of transfer learning in building a robust image classification system. The combination of a pre-trained ResNet50 model for classification and YOLOv5 for detection ensures high accuracy in detecting and classifying dog breeds. Future work could involve fine-tuning the entire ResNet50 model, experimenting with different pre-trained models, or expanding the model's capability to classify other animals.

**Author**

Mohamad Ali Ghaddar
