import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to get the data from the json file


def get_DataFrame(file):

    with open(file) as json_file:
        data = json.load(json_file)

    return data

# Function to get the normalized data from the json file


def get_Normalized_DataFrame(file):
    data = get_DataFrame(file)

    df = pd.json_normalize(data)
    return df
