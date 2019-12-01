import matplotlib.pyplot as plt
import numpy as np


def normalize_images(x):
    return x / 255

def plot_images(image, blocks=3, indices=None):
    if indices is not None:
        assert len(indices) == blocks
    blocks = min(blocks, 5)
    fig, ax = plt.subplots(1, blocks)
    indices = np.random.randint(0, image.shape[0], blocks) if indices is None else indices
    ex_img = image[indices, ...]
    for b in range(blocks):
        ax[b].imshow(ex_img[b, ...], cmap='Greys')
        ax[b].axis('off')
    plt.show()