from process import region_filtered, filtered_year, region_sum, region_avg
from load_config import dashboard, operations, regions, years  
import matplotlib.pyplot as plt

print("=" * 50)
print("GDP ANALYSIS DASHBOARD")
print("=" * 50)

# Display configuration
print("\nCONFIGURATION:")
print(f"Regions: {', '.join(regions)}")
print(f"Years: {years}")
print(f"Operations: {operations}")
print(f"Dashboard Types: {dashboard}")

print("\n" + "=" * 50)

# ---------------- OPERATIONS ----------------
print("\nSTATISTICAL RESULTS:")
for op in operations if isinstance(operations, list) else [operations]:
    op_lower = op.lower()
    if op_lower == "sum":
        print(f"Sum of GDP: ${region_sum:,.2f} billion")
    elif op_lower == "average":
        print(f"Average GDP: ${region_avg:,.2f} billion")

print("\n" + "=" * 50)

# ---------------- REGION-WISE DATA ----------------
region_countries = [row["Country"] for row in region_filtered]
region_values = [row["Value"] for row in region_filtered]  # REMOVE float()
# ---------------- YEAR-WISE DATA ----------------
# Group data by year for the selected region(s)
years_data = {}
for row in region_filtered:
    year = row["Year"]
    if year not in years_data:
        years_data[year] = []
    years_data[year].append(row["Value"])

# Calculate total/average GDP per year
year_totals = []
for year in sorted(years_data.keys()):
    values = years_data[year]
    year_totals.append((year, sum(values)))

years_list = [year for year, _ in year_totals]
year_values = [value for _, value in year_totals]

# ---------------- VISUALIZATIONS ----------------
print("\nGENERATING VISUALIZATIONS...")

# Determine chart types
if isinstance(dashboard, list):
    region_chart_type = dashboard[0].lower() if len(dashboard) > 0 else "bar"
    year_chart_type = dashboard[1].lower() if len(dashboard) > 1 else "line"
else:
    region_chart_type = year_chart_type = dashboard.lower()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- REGION PLOT ---
if region_chart_type == "bar":
    bars = ax1.bar(region_countries, region_values, color='skyblue')
    ax1.set_title(f"GDP by Country ({', '.join(regions)})")
    ax1.set_xlabel("Country")
    ax1.set_ylabel("GDP (in billions)")
    ax1.tick_params(axis='x', rotation=45)
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom')
    
elif region_chart_type == "pie":
    ax1.pie(region_values, labels=region_countries, autopct="%1.1f%%", startangle=90)
    ax1.set_title(f"GDP Distribution by Country ({', '.join(regions)})")

# --- YEAR PLOT ---
if year_chart_type == "line":
    ax2.plot(years_list, year_values, marker="o", linewidth=2, markersize=8, color='green')
    ax2.set_title(f"GDP Trend by Year ({', '.join(regions)})")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Total GDP (in billions)")
    ax2.grid(True, alpha=0.3)
    
elif year_chart_type == "scatter":
    ax2.scatter(years_list, year_values, s=100, alpha=0.6, color='red')
    ax2.set_title(f"GDP by Year ({', '.join(regions)})")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Total GDP (in billions)")
    ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("Visualization complete!")
print("=" * 50)