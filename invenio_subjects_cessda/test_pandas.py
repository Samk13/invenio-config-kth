#%%
from os import getcwd
import json
import pandas as pd


path = f'{getcwd()}/vocabularies/result.json'
res = pd.read_json(path)

with open(path,'r', encoding="utf-8") as f:
    data = json.loads(f.read())

# Flattening JSON data
df = pd.json_normalize(data, record_path=['data'], meta=['name'])[['id', 'name', 'title', 'uri']]

df

# ff.head


