# Denoising Autoencoder for MNIST

**Overview**

This project focuses on building a denoising autoencoder using the MNIST dataset. The aim is to add noise to the input data and train the autoencoder to reconstruct the original, noise-free images. By leveraging deep learning techniques, the denoising autoencoder can effectively remove noise from images, demonstrating the capability of autoencoders in enhancing data quality.

**Denoising with Autoencoders**

Denoising autoencoders are designed to learn a robust compressed representation of noisy inputs, allowing the network to reconstruct clean outputs. The process involves adding Gaussian noise to the original MNIST images and then training the autoencoder to recover the noise-free images. The architecture of this autoencoder consists of deeper convolutional layers to handle the complexity introduced by the added noise.

**Dataset Used**

The MNIST dataset, consisting of 28x28 grayscale images of handwritten digits, is used in this project. The dataset contains 60,000 training examples and 10,000 testing examples. Noise is added to these images to create noisy versions, which are then used as input to the autoencoder, while the original clean images are used as the target output.

**Network Architecture**

**Encoder**

The encoder compresses the input images into a lower-dimensional representation using a series of convolutional and pooling layers:

- **Convolutional Layer 1**: 1 input channel to 32 output channels, 3x3 kernel, followed by ReLU activation and max pooling.
- **Convolutional Layer 2**: 32 input channels to 64 output channels, 3x3 kernel, followed by ReLU activation and max pooling.

The encoder layers progressively reduce the spatial dimensions of the data, resulting in a compressed representation.

**Decoder**

The decoder reconstructs the original image using transposed convolutional layers:

- **Transposed Convolutional Layer 1**: 64 input channels to 32 output channels, 2x2 kernel, stride of 2, followed by ReLU activation.
- **Transposed Convolutional Layer 2**: 32 input channels to 1 output channel, 2x2 kernel, stride of 2, followed by Sigmoid activation.

These transposed convolutional layers effectively upsample the compressed representation back to the original image dimensions.

**Training Process**

- **Adding Noise**: Gaussian noise is added to the training images to generate noisy inputs. The noisy images are used as input to the model, while the original clean images serve as the target output.
- **Loss Function**: The mean squared error (MSE) loss function is used to compare the reconstructed images to the original images, as we are interested in pixel-wise accuracy.
- **Optimizer**: The Adam optimizer is used for efficient parameter updates during training.
- **Training Duration**: The network is trained for 20 epochs with a batch size of 20.

The training process involves minimizing the difference between the original and reconstructed images, thereby teaching the model to effectively remove noise from the inputs.

**Results**

The denoising autoencoder successfully reconstructs the original MNIST images from their noisy versions. The reconstructed images demonstrate that the autoencoder is capable of effectively removing noise while preserving the essential features of the handwritten digits.

**Visualization**

- **Noisy vs Reconstructed Images**: A side-by-side comparison of noisy input images and their reconstructed versions is provided to evaluate the effectiveness of the denoising process.
- **Training Loss**: The training loss decreases consistently over the epochs, indicating that the model is learning to accurately reconstruct the images from noisy inputs.

**Future Work**

Future work could involve experimenting with different noise levels and types, such as salt-and-pepper noise, to test the robustness of the denoising autoencoder. Additionally, increasing the depth of the network or using advanced architectures like residual networks could further improve the performance of the model.

**Conclusion**

The denoising autoencoder built in this project demonstrates how deep learning can be used to remove noise from images. By learning a robust compressed representation of the noisy MNIST images, the model is able to reconstruct clean images with reasonable accuracy. This technique has potential applications in image restoration, noise reduction, and improving the quality of data for further analysis.

**Author**

Mohamad Ali Ghaddar

Adapted from Udacity Deep Learning V2