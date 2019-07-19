
import numpy as np

class Profile:
    def __init__(self, name, arr):
        self.name = name
        self.mean_descriptor = np.mean(arr)
        self.array = arr
        
        """
        name = string
        arr = numpy array (128 vector) corresponding to picture of face
        
        """
        
    def __call__(self, newarr):
        
        self.array = np.vstack(self.array, newarr)
        self.mean_descriptor = np.mean(self.array)
    
        """
        newarr = 128 vector numpy array of new picture of person
        
        returns:
            new_mean_descriptor = numpy array
        
        """

# database = {name(string), name(class)}

    