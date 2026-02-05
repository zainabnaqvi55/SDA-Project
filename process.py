import load_config

regions = load_config.regions
years = load_config.years
operations = load_config.operations
dashboard = load_config.dashboard
data = load_config.data


filtered_region = list(filter(
    lambda row: row["Region"] in regions,
    data
))

print(filtered_region)

if not filtered_region:
    print("No data for selected regions")
    exit()

elif any(row["Year"] == "" for row in filtered_region):
    print("Year section empty for this region")
    exit()

filtered_year = list(filter(
    lambda row: int(row["Year"]) in years,
    filtered_region
))

if not filtered_year:
    print("No data for selected year in the region")
    exit()

if any(row["Value"] == "" for row in filtered_region):
    print("Value section empty for this region")
    exit()

print(filtered_year)
