import sys
import os

# Ensure all scripts are runnable
scripts = [
    "software/ai_core/simulate_growth.py",
    "software/ai_core/vision_analysis.py",
    "software/controllers/pid_control.py",
    "software/controllers/gas_regulator.py",
    "software/api/dashboard.py",
    "data/synthetic_growth_generator.py"
]

def run_integration_test():
    print("--- AstroBotany Integration Test Hub ---")
    all_passed = True
    
    for script in scripts:
        print(f"\n[TESTING] {script}...")
        res = os.system(f"python {script}")
        if res == 0:
            print(f"[PASSED] {script}")
        else:
            print(f"[FAILED] {script}")
            all_passed = False
            
    if all_passed:
        print("\nMISSION READY: All systems operational.")
    else:
        print("\nMISSION ABORT: Component failure detected.")
    return all_passed

if __name__ == "__main__":
    run_integration_test()
