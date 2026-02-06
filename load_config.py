import json
import csv

with open("config.json") as c:
    config = json.load(c)

regions = config["regions"]
years = config["years"]
operations = config["operations"]
dashboard = config["dashboard"]
Country = config.get("Country")

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    data = list(reader)
