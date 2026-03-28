import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_performance_report(csv_path="data/synthetic_growth.csv"):
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return
    
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("AstroBotany-Optimizer: 60-Day Mission Performance Report", fontsize=16)
    
    # Biomass Growth
    axes[0, 0].plot(df['timestamp'], df['biomass_g'], color='green')
    axes[0, 0].set_title("Biomass Accumulation (grams)")
    axes[0, 0].set_ylabel("Biomass (g)")
    
    # Atmospheric Stabilty (Temp & Humidity)
    axes[0, 1].plot(df['timestamp'], df['temp_c'], label="Temp C", color='red', alpha=0.6)
    axes[0, 1].plot(df['timestamp'], df['humidity_pct'], label="Humidity %", color='blue', alpha=0.6)
    axes[0, 1].set_title("Atmospheric Stability")
    axes[0, 1].legend()
    
    # Nutrient Profile (pH & EC)
    axes[1, 0].plot(df['timestamp'], df['ph'], label="pH", color='purple')
    axes[1, 0].set_title("Nutrient Solution pH Profile")
    axes[1, 0].set_ylim(5, 7)
    
    # Resource Consumption
    axes[1, 1].fill_between(df['timestamp'], df['power_consumption_w'], color='orange', alpha=0.3, label="Power (W)")
    axes[1, 1].set_title("Energy Consumption Profile")
    axes[1, 1].legend()
    
    os.makedirs("assets", exist_ok=True)
    report_path = "assets/performance_report.png"
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(report_path)
    print(f"Performance report saved to {report_path}")

if __name__ == "__main__":
    generate_performance_report()
