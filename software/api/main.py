from fastapi import FastAPI
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

@app.get("/")
async def root():
    return {
        "status": "online",
        "mission": "TUA Astrohackathon - AstroBotany Optimizer",
        "system_time": datetime.utcnow().isoformat()
    }

@app.get("/telemetry/current")
async def get_telemetry():
    return TelemetryData(
        timestamp=datetime.utcnow().isoformat(),
        sensor_id="AO-NODE-01",
        ph=round(random.uniform(5.8, 6.2), 2),
        ec=round(random.uniform(1.6, 2.0), 2),
        co2=random.randint(800, 1200),
        humidity=round(random.uniform(70, 85), 1),
        temperature=round(random.uniform(22, 26), 1)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
