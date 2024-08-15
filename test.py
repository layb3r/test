import numpy as np 
import torch 

device = "cuda" if torch.cuda.is_available() else "cpu"
a = np.array(45)
print("Hello World")