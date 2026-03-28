import numpy as np
import argparse
import time

class AstroBotanyOptimizer:
    def __init__(self, crop_type="Microgreens", target_days=30):
        self.crop_type = crop_type
        self.target_days = target_days
        self.water_usage = []
        self.energy_usage = []
        self.biomass = []
        
    def objective_function(self, water, energy, time_step):
        # Math from README: Z = sum((K * B(t)) / (S(t) + E(t)))
        calorie_density = 0.5  # kcal/g for typical microgreens
        growth_rate = 0.1 * (1 + 0.5 * np.sin(time_step / self.target_days * np.pi))
        current_biomass = growth_rate * time_step * (1 - (water+energy)*0.01)
        
        cost = water + energy + 0.001 # prevent div by zero
        efficiency = (calorie_density * current_biomass) / cost
        return efficiency, current_biomass

    def run_simulation(self):
        print(f"--- AstroBotany Simulation: {self.crop_type} ---")
        print(f"Target: {self.target_days} days of closed-loop growth.")
        
        for day in range(1, self.target_days + 1):
            # Simulated RL decision for water and energy optimization
            optimal_water = 5.0 * np.exp(-day/10) # Efficiency increases over time
            optimal_energy = 10.0 + 2.0 * np.random.randn()
            
            score, bio = self.objective_function(optimal_water, optimal_energy, day)
            self.water_usage.append(optimal_water)
            self.energy_usage.append(optimal_energy)
            self.biomass.append(bio)
            
            if day % 5 == 0:
                print(f"Day {day:02d}: Biomass={bio:.2f}g | Efficiency Score={score:.4f}")
            time.sleep(0.05)
            
        print("\n--- Simulation Complete ---")
        print(f"Total Biomass Produced: {sum(self.biomass):.2f} grams")
        print(f"Total Water Consumed (Net): {sum(self.water_usage):.2f} liters")
        print(f"Average System Efficiency: {np.mean(score):.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AstroBotany Growth Simulation")
    parser.add_argument("--crop", type=str, default="Microgreens", help="Type of crop to simulate")
    parser.add_argument("--days", type=int, default=30, help="Simulation duration")
    args = parser.parse_args()
    
    optimizer = AstroBotanyOptimizer(args.crop, args.days)
    optimizer.run_simulation()
