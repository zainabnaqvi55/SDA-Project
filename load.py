import json
import pandas as pd

#load config
with open("config.json") as c:
    config = json.load(c)

#load CSV
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: data.csv file not found!")
    df = pd.DataFrame()  #empty dataframe to avoid crashes
