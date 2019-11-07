import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    def load(self, path):
        img = mpimg.imread(path)
        wsi = img.shape[0]
        lsi = img.shape[1]
        print(f"Loading image of dimensions {wsi} x {lsi}")
        return img

    def display(self, array, interpolation="nearest"):
        return plt.imshow(array, interpolation=interpolation)
