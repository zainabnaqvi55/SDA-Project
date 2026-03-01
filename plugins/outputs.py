# plugins/outputs.py
import json
from typing import List, Dict, Any
from core.contracts import DataSink
import matplotlib.pyplot as plt


class ConsoleWriter(DataSink):
    """Prints results and generates visualizations"""
    def write(self, records: List[Dict[str, Any]]) -> None:
        for record in records:
            filtered_data: List[Dict[str, Any]] = record.get("filtered_data", [])
            stats: Dict[str, Any] = record.get("stats", {})
            config: Dict[str, Any] = record.get("config", {})

            print("=" * 50)
            print("STATISTICAL RESULTS:")
            for k, v in stats.items():
                if isinstance(v, (int, float)):
                    print(f"{k}: {v:.2f}")
            print("\nTop 5 Rows:")
            for row in filtered_data[:5]:
                print(row)
            print("=" * 50)

            dashboard = config.get("dashboard", ["bar", "line"])
            self.generate_charts(filtered_data, stats, dashboard)

    def generate_charts(
        self,
        filtered_data: List[Dict[str, Any]],
        stats: Dict[str, Any],
        dashboard: List[str],
    ) -> None:
        if not filtered_data:
            return

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Top 10 countries chart
        top_countries = stats.get("top_10_countries", [])
        if top_countries:
            countries = [r["Country"] for r in top_countries]
            values = [r["Value"] for r in top_countries]

            chart_type = dashboard[0].lower() if dashboard else "bar"

            if chart_type == "bar":
                ax1.bar(countries, values, color="skyblue")
                ax1.set_title("Top 10 Countries by GDP")
                ax1.set_xlabel("Country")
                ax1.set_ylabel("GDP (in billions)")
                ax1.tick_params(axis="x", rotation=45)
            elif chart_type == "pie":
                sorted_pairs = sorted(zip(countries, values), key=lambda x: x[1], reverse=True)
                sorted_countries, sorted_values = zip(*sorted_pairs)
                ax1.pie(sorted_values, labels=sorted_countries, autopct="%1.1f%%", startangle=90)
                ax1.set_title("GDP Distribution of Top 10 Countries")

        # Global GDP trend chart
        global_trend = stats.get("global_gdp_by_year", {})
        if global_trend:
            years = sorted(global_trend.keys())
            values = [global_trend[y] for y in years]

            chart_type = dashboard[1].lower() if len(dashboard) > 1 else "line"

            if chart_type == "line":
                ax2.plot(years, values, marker="o", linewidth=2, color="green")
            elif chart_type == "scatter":
                ax2.scatter(years, values, s=100, alpha=0.7, color="red")

            ax2.set_title("Global GDP Trend by Year")
            ax2.set_xlabel("Year")
            ax2.set_ylabel("Total GDP")
            ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()


class FileWriter(DataSink):
    """Writes results to a JSON file"""
    def __init__(self, file_path: str = "output.json"):
        self.file_path = file_path

    def write(self, records: List[Dict[str, Any]]) -> None:
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(records, f, indent=2)
            print(f"Results written to {self.file_path}")
        except IOError as e:
            print(f"ERROR: Failed to write to file {self.file_path}: {e}")