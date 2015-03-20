import numpy as np
import matplotlib.colors.cnames as color_names

class ColorPicker(object):

    def __init__(self, size):
        self.colors = []
        if size > len(color_names.keys())
        for index, name, hex_value in enumerate(color_names.iteritems()):
            if index > size:
                break
            else:
                self.colors.append(hex_value)

    def get_color(self, index)
        return self.colors[index]

