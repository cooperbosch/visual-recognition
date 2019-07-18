
    

class Profile:
    def __init__(self, name, arr):
        self.name = name
        self.mean_descriptor = arr
        self.num_of_samples = 1
        
        """
        name = string
        arr = numpy array (128 vector) corresponding to picture of face
        
        """
        
    def __call__(self, newarr):
        total = self.mean_descriptor * self.num_of_samples + newarr
        self.num_of_samples += 1
        new_mean_descriptor = total / self.num_of_samples
        return new_mean_descriptor
    
        """
        newarr = 128 vector numpy array of new picture of person
        
        returns:
            new_mean_descriptor = numpy array
        
        """
        
database = {}

# database = {name(string), name(class)}