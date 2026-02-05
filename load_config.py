
import json
import csv

#load config
with open("SDA-Project/config.json") as c:
    config = json.load(c)


regions = config["regions"]
years=config["years"]
operations=config["operations"]
dashboard=config["dashboard"]

with open("SDA-Project/data.csv", newline="") as f:
    reader = csv.DictReader(f)
    data = list(reader)

if not data:
    print("csv file is empty")
    exit()

