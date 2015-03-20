import numpy as np
import matplotlib.pyplot as plt
import ColorPicker

def bar_chart_csv_by_row(csv_file, 
                         output, 
                         output_folder=None, 
                         separator=",",
                         named_first_row=False,
                         x_label="",
                         y_label="",
                         title="",
                         style="ggplot"):
    """
    Merges a bunch of CSV files
    It assumes that the name associated with the data are stored in the first 
    column in each row

    Params:
            @csv_file: str 
            The name of the input CSV file
            
            @output : str
            The name of the output chart

            @output_folder : str        (Default: None)
            Tells where the chart should be written
            If no path is given, the file is written in the same folder as 
            the program is called

            @separator : str            (Default: ",")
            The key used to separate the values within the file

    Output:
            @chart : file 
            A file containing the chart of the input CSV file
    """
    csv = open(csv_file, 'r')
    column_names = []
    data = {}

    for index, line in enumerate(csv.readlines()):
        if named_first_row and index == 0:
           column_names = line.split(separator) 
        
        name = line.split(separator)[0]
        data[name] = line.split(separator)[1:]

    index = np.arrange(len(data.keys()))
    bar_width=0.35
    opacity=0.4
    colors = ColorPicker(len(data.keys()))
    for index, name, values in enumerate(data.iteritems()):
        rects = plt.bar(index, values, bar_width,
                        aplha=opacity,
                        color=colors.get_color(index),
                        label=name)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(index + bar_width, data.keys())
    plt.legend

    if style is in plt.style.available:
        plt.style.use(style)

    plt.tight_layout()

    plt.show()
