import time
import random

class GasRegulator:
    """
    Simulates O2/CO2 balancing in a closed-loop habitat.
    Adjusts photosynthesis rate (via LED intensity) based on astronaut respiration.
    """
    def __init__(self, target_co2=1000, target_o2=21.0):
        self.target_co2 = target_co2 # ppm
        self.target_o2 = target_o2   # %
        self.current_co2 = target_co2
        self.current_o2 = target_o2
        self.photosynthesis_efficiency = 0.8 # 0.0 to 1.0

    def step(self, astronaut_count=4):
        # Astronauts consume O2 and produce CO2
        o2_consumption = astronaut_count * 0.005 # % per step
        co2_production = astronaut_count * 15    # ppm per step
        
        self.current_o2 -= o2_consumption
        self.current_co2 += co2_production
        
        # Plant photosynthesis consumes CO2 and produces O2
        # Controlled by "LED INTENSITY" (modelled as photosynthesis_efficiency)
        co2_uptake = self.photosynthesis_efficiency * 25
        o2_release = self.photosynthesis_efficiency * 0.008
        
        self.current_co2 -= co2_uptake
        self.current_o2 += o2_release
        
        # Regulation Logic (O2/CO2 Balancing)
        if self.current_co2 > self.target_co2:
            self.photosynthesis_efficiency = min(1.0, self.photosynthesis_efficiency + 0.05)
        else:
            self.photosynthesis_efficiency = max(0.1, self.photosynthesis_efficiency - 0.05)
            
        return {
            "o2": round(self.current_o2, 3),
            "co2": round(self.current_co2, 1),
            "efficiency": round(self.photosynthesis_efficiency, 2)
        }

def run_gas_simulation():
    regulator = GasRegulator()
    print("--- Starting O2/CO2 Atmospheric Balancing ---")
    for i in range(15):
        stats = regulator.step()
        print(f"Interval {i+1:02d}: O2={stats['o2']}% | CO2={stats['co2']}ppm | Photo-Eff={stats['efficiency']}")
        time.sleep(0.1)

if __name__ == "__main__":
    run_gas_simulation()
