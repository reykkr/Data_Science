# Convolutional Autoencoder for MNIST Compression

**Overview**

This project involves building a convolutional autoencoder to compress and reconstruct images from the MNIST dataset. The encoder uses convolutional and pooling layers to create a compressed representation, while the decoder uses transposed convolutional layers to reconstruct the image from this representation. The project demonstrates how deep learning techniques can be applied to efficiently compress data, which can be useful in a wide range of applications including denoising and data storage optimization.

**Compressed Representation**

A compressed representation allows data to be stored more efficiently compared to raw formats, while still retaining key information. In this project, we demonstrate how autoencoders can create such representations for MNIST images, and how they can be used to reconstruct the original images.

**Dataset Used**

The MNIST dataset, consisting of 28x28 grayscale images of handwritten digits, is used in this project. The dataset contains 60,000 training examples and 10,000 testing examples. The training data is used to train the autoencoder, and the test data is used to evaluate the quality of the reconstructions.

**Network Architecture**

**Encoder**

The encoder consists of a series of convolutional layers, each followed by a max-pooling layer that reduces the spatial dimensions of the data:

- **Convolutional Layer 1**: 1 input channel to 16 output channels, 3x3 kernel, followed by ReLU activation and max pooling.
- **Convolutional Layer 2**: 16 input channels to 4 output channels, 3x3 kernel, followed by ReLU activation and max pooling.

The max-pooling layers progressively reduce the spatial dimensions of the data, creating a smaller and more compressed representation.

**Decoder**

The decoder reconstructs the original image using transposed convolutional layers:

- **Transposed Convolutional Layer 1**: 4 input channels to 16 output channels, 2x2 kernel, stride of 2, followed by ReLU activation.
- **Transposed Convolutional Layer 2**: 16 input channels to 1 output channel, 2x2 kernel, stride of 2, followed by Sigmoid activation.

These transposed convolutional layers effectively upsample the compressed representation back to the original image dimensions.

**Training Process**

- **Loss Function**: The mean squared error (MSE) loss function is used to compare the reconstructed images to the original images, as we are interested in pixel-wise accuracy.
- **Optimizer**: The Adam optimizer is used for efficient parameter updates during training.
- **Training Duration**: The network is trained for 30 epochs with a batch size of 20.

The training process involves minimizing the difference between the original and reconstructed images, thereby learning an efficient compressed representation.

**Results**

The autoencoder successfully compresses and reconstructs the MNIST images, although the reconstructions may show artifacts, such as checkerboard effects, due to the nature of the transposed convolutional layers. Despite these artifacts, the model is able to retain the overall structure of the handwritten digits, demonstrating the effectiveness of the autoencoder architecture for data compression.

**Visualization**

- **Original vs Reconstructed Images**: A side-by-side comparison of original images and their reconstructions is provided to evaluate the quality of the compression.
- **Training Loss**: The training loss decreases consistently over the epochs, indicating that the model is learning to accurately reconstruct the images.

**Future Work**

To improve the quality of the reconstructions and reduce artifacts, future work could involve experimenting with other upsampling techniques, such as nearest neighbor or bilinear interpolation, followed by convolutional layers instead of transposed convolutions. Additionally, tuning hyperparameters like the number of layers and filter sizes may further enhance the performance.

**Conclusion**

The convolutional autoencoder built in this project demonstrates how deep learning can be used for data compression. By learning a compressed representation of the MNIST images, the model is able to reconstruct images with reasonable accuracy. This technique has potential applications in denoising, feature extraction, and efficient data storage.

**Author**

Mohamad Ali Ghaddar

Adapted from Udacity Deep Learning V2