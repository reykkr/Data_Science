# Generative Adversarial Network for MNIST

**Overview**

This project involves building a Generative Adversarial Network (GAN) to generate new handwritten digits based on the MNIST dataset. GANs consist of two competing neural networks: a generator and a discriminator. The generator attempts to create realistic images to fool the discriminator, while the discriminator aims to distinguish between real and generated images. The adversarial training process leads to the generator producing images that become increasingly indistinguishable from real ones.

GANs were first introduced in 2014 by Ian Goodfellow and his collaborators in Yoshua Bengio's lab. Since then, GANs have gained significant popularity for their ability to generate realistic data, including images, text, and more.

**Dataset Used**

The MNIST dataset, consisting of 28x28 grayscale images of handwritten digits (0-9), is used in this project. The dataset contains 60,000 training images and 10,000 testing images. The goal is to train the GAN to generate new handwritten digits that resemble the original dataset.

**Network Architecture**

**Discriminator**

The discriminator is a binary classifier designed to distinguish between real and fake images. It is composed of multiple fully connected layers with Leaky ReLU activations, which allow gradients to flow even for negative input values, thus improving training stability. The discriminator uses a final linear layer without an activation function, as the output is passed to a binary cross-entropy loss function.

- **Input Layer**: The input is a flattened 28x28 image, resulting in a vector of size 784.
- **Hidden Layers**: The discriminator has several fully connected layers with decreasing sizes, each followed by Leaky ReLU and dropout for regularization.
- **Output Layer**: A single output unit that predicts whether the input image is real or fake.

**Generator**

The generator network is responsible for creating new images that resemble the MNIST dataset. The generator takes a random vector (latent vector) as input and uses fully connected layers with increasing dimensions to generate an image. The final layer applies a `tanh` activation function, which scales the output to be between -1 and 1, matching the range of the normalized MNIST images.

- **Input Layer**: The input is a latent vector of size 100, sampled from a uniform distribution.
- **Hidden Layers**: The generator has several fully connected layers with increasing sizes, each followed by Leaky ReLU and dropout.
- **Output Layer**: A vector of size 784, reshaped to a 28x28 image, with a `tanh` activation.

**Loss Functions**

- **Discriminator Loss**: The discriminator's loss is a combination of two parts: the loss for real images (which should be classified as real) and the loss for generated images (which should be classified as fake). Binary cross-entropy loss is used for both components.
- **Generator Loss**: The generator's goal is to fool the discriminator into classifying the generated images as real. The generator loss is calculated by flipping the labels for the fake images.

**Optimizers**

Separate Adam optimizers are used for the discriminator and generator, with a learning rate of 0.002. The optimizers update the weights of the respective networks to minimize their loss functions.

**Training Process**

The training process involves alternating between training the discriminator and the generator:

1. **Training the Discriminator**

   - The discriminator is trained on a batch of real images and a batch of generated (fake) images.
   - The real and fake losses are computed, and the weights are updated to improve the discriminator's ability to distinguish real images from generated ones.

2. **Training the Generator**

   - The generator is trained by passing random latent vectors through it to produce fake images.
   - The discriminator's output for these fake images is used to compute the generator's loss.
   - The weights are updated to improve the generator's ability to create realistic images that can fool the discriminator.

**Results**

The GAN successfully generates new handwritten digits that resemble the original MNIST dataset. During training, the generated images start as random noise and gradually become clearer and more similar to handwritten digits as the training progresses.

- **Training Losses**: The discriminator and generator losses are monitored throughout the training process to ensure balanced learning.
- **Generated Samples**: Samples of generated digits are saved periodically during training to visualize the improvement in the quality of generated images.

**Visualization**

- **Training Loss Plot**: A plot of the discriminator and generator losses over epochs shows how the networks compete and improve over time.
- **Generated Images**: The generated images from different stages of training demonstrate the GAN's learning process, from producing noise to recognizable digits.

**Conclusion**

This project demonstrates the power of Generative Adversarial Networks in generating realistic images. By training the generator to compete with the discriminator, the GAN learns to create new handwritten digits that are indistinguishable from real ones. Future work could involve experimenting with different GAN architectures, such as DCGANs or Conditional GANs, or applying GANs to other datasets and types of data generation tasks.

**Author**

Mohamad Ali Ghaddar