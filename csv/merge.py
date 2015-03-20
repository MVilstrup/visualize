import numpy as np
import os
from os.path import splitext, basename

def merge_rows(files, output, output_folder=None):
    """
    Merges a bunch of CSV files
    It assumes that the name associated with the data are stored in the first 
    column in each row

    Params:
            @files : array, shape=[file_paths]
            An array of the paths to all the files that should be merged.
            
            @output : str
            The name of the merged file

            @output_folder : str       (Default: None)
            Tells where the merged file should be written
            If no path is given, the file is written in the same folder as 
            the program is called

    Output:
            @merged : file 
            A file containing the merged content of the given CSV files 
    """
    csv_files = {}
    file_names = [] 
    for path in files:
        name, extension = splitext(basename(path))
        if extension != ".csv":
            raise ArgumentError("All files must be CSV")
        csv_files[name] = path
        file_names.append[name]

    if output_folder is not None:
        output = os.path.join(output_folder, output)
    

def merge_columns(files):
    pass

