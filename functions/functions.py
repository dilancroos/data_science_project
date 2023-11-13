import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_Normalized_DataFrame(file):
    with open(file) as json_file:
        data = json.load(json_file)
        
        print(len(data))
        df = pd.json_normalize(data)
    return df