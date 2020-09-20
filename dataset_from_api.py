import pandas as pd
import requests
import json

url = "apiname"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent=4, sort_keys=True)
print(content)

# list of channels we want to access
channels = [""]

channels_list = []
# for each channel, access its information through its API
for channel in channels:
    JSONContent = requests.get("apiname" + channel).json()
    if 'error' not in JSONContent:
        channels_list.append([JSONContent['id']])

dataset = pd.DataFrame(channels_list)
# display randomly selected rows of the dataframe
dataset.sample(5)

# giving name to the headings
dataset.columns = ['Id']
# remove the rows with missing values
dataset.dropna(axis=0, how='any', inplace=True)
dataset.index = pd.RangeIndex(len(dataset.index))

dataset.to_csv("new_dataset.csv")
print(dataset)