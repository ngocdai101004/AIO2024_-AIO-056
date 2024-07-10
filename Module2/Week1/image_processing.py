import numpy as np
import matplotlib . image as mpimg
import matplotlib.pyplot as plt


img = mpimg.imread('dog.jpeg')


def convert_to_gray_img_by_lightness(img):
    res = (np.max(img, axis=2) + np.min(img, axis=2))/2
    return res


def convert_to_gray_img_by_average(img):
    res = np.average(img, axis=2)
    return res


def convert_to_gray_img_by_luminosity(img):
    coefficients = [0.21, 0.72, 0.07]
    res = np.sum(np.multiply(img, coefficients), axis=2)
    return res


if __name__ == "__main__":
    img = mpimg.imread('dog.jpeg')
    img_by_lightness = convert_to_gray_img_by_lightness(img)
    img_by_average = convert_to_gray_img_by_average(img)
    img_by_luminosity = convert_to_gray_img_by_luminosity(img)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    axes[0, 0].imshow(img)
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')

    axes[0, 1].imshow(img_by_lightness, cmap='gray')
    axes[0, 1].set_title('By Lightness')
    axes[0, 1].axis('off')

    axes[1, 0].imshow(img_by_average, cmap='gray')
    axes[1, 0].set_title('By Average')
    axes[1, 0].axis('off')

    axes[1, 1].imshow(img_by_luminosity, cmap='gray')
    axes[1, 1].set_title('By Luminosity')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
