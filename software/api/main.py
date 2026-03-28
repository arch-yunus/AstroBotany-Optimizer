from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(title="AstroBotany Telemetry API", version="1.0.0")

class TelemetryData(BaseModel):
    timestamp: str
    sensor_id: str
    ph: float
    ec: float
    co2: int
    humidity: float
    temperature: float

class SystemControl(BaseModel):
    led_intensity: float # 0.0 to 1.0
    misting_frequency: int # seconds
    nutrient_pump_state: bool

@app.get("/")
async def root():
    return {
        "status": "online",
        "mission": "TUA Astrohackathon - AstroBotany Optimizer",
        "system_time": datetime.utcnow().isoformat()
    }

@app.get("/telemetry/current")
async def get_telemetry():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "sensor_id": "AO-NODE-01",
        "ph": round(random.uniform(5.8, 6.2), 2),
        "ec": round(random.uniform(1.6, 2.0), 2),
        "co2": random.randint(800, 1200),
        "humidity": round(random.uniform(70, 85), 1),
        "temperature": round(random.uniform(22, 26), 1)
    }

@app.post("/control/override")
async def control_override(command: SystemControl):
    # Simulated hardware override
    if command.led_intensity < 0 or command.led_intensity > 1:
        raise HTTPException(status_code=400, detail="Invalid LED intensity")
    
    print(f"OVERRIDE: LED={command.led_intensity} | Misting={command.misting_frequency}s")
    return {
        "status": "success",
        "message": "Hardware parameters updated successfully",
        "applied_intensity": command.led_intensity
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
