import numpy as np
import matplotlib.pyplot as plt


def read_image(w, h, input):
    n_layers = len(input) // (w * h)
    image = np.zeros((w, h, n_layers))
    index = 0
    for layer in range(n_layers):
        for height in range(h):
            for width in range(w):
                image[width, height, layer] = int(input[index])
                index += 1
    return image


def find_color(layers):
    return layers[np.argmax(layers != 2)]


def decode_image(image):
    return np.apply_along_axis(find_color, 2, image)


if __name__ == "__main__":
    W = 25
    H = 6
    with open("../data/day_08.txt") as f:
        image = read_image(W, H, f.readline().strip())

    less_zeros_level = np.argmin([np.sum(image[:, :, i] == 0) for i in range(image.shape[2])])
    print(np.sum(image[:, :, less_zeros_level] == 1) * np.sum(image[:, :, less_zeros_level] == 2))
    plt.imshow(decode_image(image).T)
    plt.show()
