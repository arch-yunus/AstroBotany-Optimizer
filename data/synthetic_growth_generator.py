import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_growth_data(days=60):
    print(f"Generating synthetic growth data for {days} days...")
    
    data = []
    base_time = datetime(2026, 1, 1, 0, 0, 0)
    
    for i in range(days * 24): # Hourly data
        current_time = base_time + timedelta(hours=i)
        
        # Environmental factors
        temp = 24 + 2 * np.sin(i * np.pi / 12) + 0.5 * np.random.randn()
        humidity = 75 + 5 * np.sin(i * np.pi / 12) + np.random.randn()
        co2 = 1000 + 200 * np.sin(i * np.pi / 12) + 20 * np.random.randn()
        
        # Nutrient factors
        ph = 6.0 + 0.1 * np.random.randn()
        ec = 1.8 + 0.05 * np.random.randn()
        
        # Growth metric (cumulative biomass)
        biomass = 0.5 * np.exp(0.002 * i) + 0.1 * np.random.randn()
        
        # Efficiency (Resource consumption)
        water_cons = 0.1 * (temp / 24) * (humidity / 75)
        power_cons = 50 + 10 * np.sin(i * np.pi / 12)
        
        data.append({
            "timestamp": current_time.isoformat(),
            "temp_c": round(temp, 2),
            "humidity_pct": round(humidity, 1),
            "co2_ppm": int(co2),
            "ph": round(ph, 2),
            "ec_ms_cm": round(ec, 2),
            "biomass_g": round(biomass, 4),
            "water_consumption_l": round(water_cons, 4),
            "power_consumption_w": round(power_cons, 2)
        })
        
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    file_path = "data/synthetic_growth.csv"
    df.to_csv(file_path, index=False)
    print(f"Dataset saved to {file_path} ({len(df)} records)")

if __name__ == "__main__":
    generate_growth_data()
