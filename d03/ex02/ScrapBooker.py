import numpy as np


class ScrapBooker:
    def crop(self, array, dimensions, position=(0, 0)):
        if arr.shape[0] < dimensions[0] or arr.shape[1] < dimensions[1]:
            raise ValueError("Dimensions can not be larger than the original image")
        elif position[0] + dimensions[0] > arr.shape[0] or position[1] + dimensions[1] > arr.shape[1]:
            raise ValueError("Crop dimensions out of bounds")
        return arr[position[0]:dimensions[1], position[1]:dimensions[1]]

    def thin(self, array, n, axis):
        return arr[0::n, :] if axis else arr[:, 0::n]

    def juxtapose(self, array, n, axis):
        return np.concatenate((array,)*n, axis=axis)

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)
