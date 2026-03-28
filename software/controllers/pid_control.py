import time
import random

class PIDController:
    def __init__(self, p, i, d, setpoint):
        self.Kp = p
        self.Ki = i
        self.Kd = d
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def compute(self, current_value, dt=1.0):
        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

def monitor_nutrient_system():
    print("Initializing Nutrient PID Controllers (pH/EC)...")
    ph_pid = PIDController(0.5, 0.1, 0.05, 6.0) # Target pH 6.0
    ec_pid = PIDController(1.2, 0.2, 0.1, 1.8)  # Target EC 1.8 mS/cm
    
    current_ph = 6.5
    current_ec = 1.2
    
    for i in range(10):
        ph_adj = ph_pid.compute(current_ph)
        ec_adj = ec_pid.compute(current_ec)
        
        # Simulate physical response
        current_ph += ph_adj * 0.1 + (random.random() - 0.5) * 0.05
        current_ec += ec_adj * 0.1 + (random.random() - 0.5) * 0.01
        
        print(f"Cycle {i+1}: pH={current_ph:.2f} (Adj: {ph_adj:+.3f}) | EC={current_ec:.2f} (Adj: {ec_adj:+.3f})")
        time.sleep(0.1)

if __name__ == "__main__":
    monitor_nutrient_system()
