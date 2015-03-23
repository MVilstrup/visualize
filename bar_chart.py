import numpy as np
import matplotlib.pyplot as plt

class BarChart(object):

    def __init__(self, 
                 style="ggplot",
                 width=0.4, 
                 bar_groups=None, 
                 data=None):
        # Initialize the empty varaibles
        self.bar_groups = []
        self.data = {}
        self.index = []
        self.width = width
        self.figure = plt.figure()

        # If data is provided in the initializer update the variables accordingly 
        if data is not None:
            self.data = data
        if bar_groups is not None:
            self.bar_groups = bar_groups
            self.index = np.arange(len(self.bar_groups))
        
        if style not in plt.style.available:
            raise ValueError("Style should be one of the following :%s" % plt.style.available)            
        self.style = style 

    def add_bar_group(self, group):
        self.bar_groups.append(group)
        self.index = np.arange(len(self.data))

    def add_data(self, data, label):
        self.data[label] = data

    def set_width(self, width):
        self.width = width

    def save(self, name, folder):
        pass

    def _create_bars(self):
        for label, values in self.data.iteritems():
            print "Label = %s" % label
            values = np.array(map(float, values))
            print "Values = %s" % values
            plt.bar(self.index + self.width,
                    values,
                    self.width,
                    color="b",
                    label=label)

    def show(self):
        plt.style.use(self.style)
        
        self._create_bars()
        plt.xticks(self.index + self.width,
                   self.bar_groups)
        plt.legend()
        plt.tight_layout()
        plt.show()
