from process import region_filtered, filtered_year, region_sum, region_avg
from load_config import dashboard, operations, regions, years  
import matplotlib.pyplot as plt

print("=" * 50)
print("GDP ANALYSIS DASHBOARD")
print("=" * 50)

# Display 
print("\nCONFIGURATION:")
print(f"Regions: {', '.join(regions)}")
print(f"Years: {years}")
print(f"Operations: {operations}")
print(f"Dashboard Types: {dashboard}")

print("\n" + "=" * 50)

# operations
print("\nSTATISTICAL RESULTS:")
for op in operations if isinstance(operations, list) else [operations]:
    op_lower = op.lower()
    if op_lower == "sum":
        print(f"Sum of GDP: ${region_sum:,.2f} billion")
    elif op_lower == "average":
        print(f"Average GDP: ${region_avg:,.2f} billion")

print("\n" + "=" * 50)

# region wise data
region_countries = [row["Country"] for row in filtered_year]
region_values = [row["Value"] for row in filtered_year]

# year wise data
# Group data by year for selected region
years_data = {}
for row in region_filtered:
    year = row["Year"]
    if year not in years_data:
        years_data[year] = []
    years_data[year].append(row["Value"])

# Calculate sum/average GDP per year
year_totals = []
for year in sorted(years_data.keys()):
    values = years_data[year]
    year_totals.append((year, sum(values)))

years_list = [year for year, _ in year_totals]
year_values = [value for _, value in year_totals]

