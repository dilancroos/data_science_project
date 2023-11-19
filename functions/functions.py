import json
import pandas as pd


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


def get_file_name(givenFile):
    fileN = givenFile.split('.')[0].split('_')

    if len(fileN) == 2:
        fileName = f"{fileN[0]} in {fileN[1]}"
    else:
        fileName = f"{fileN[0]} in {fileN[1]} {fileN[2]}"

    return fileName
