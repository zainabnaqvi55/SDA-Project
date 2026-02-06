from load_config import data, regions, operations, Country

cleaned_data = list(filter(
    lambda r: r["Region"] != "" and r["Year"] != "" and r["Value"] != "",
    data
))

for row in cleaned_data:
    row["Year"] = int(row["Year"])
    row["Value"] = float(row["Value"])

region_filtered = list(filter(lambda r: r["Region"] in regions, cleaned_data))
country_filtered = list(filter(lambda r: r["Country"] == Country, cleaned_data)) if Country else []

region_sum = sum(map(lambda r: r["Value"], region_filtered))
region_avg = region_sum / len(region_filtered) if region_filtered else 0

country_sum = sum(map(lambda r: r["Value"], country_filtered))
country_avg = country_sum / len(country_filtered) if country_filtered else 0

print("Sum of GDP of Regions:", region_sum)
print("Average GDP of Regions:", region_avg)
print("Average GDP of a Country:", country_avg)
