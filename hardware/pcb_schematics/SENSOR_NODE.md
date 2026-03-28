# Sensor Node & Control PCB (v1.0)

## Circuit Topology
The AstroBotany control system utilizes a distributed sensor architecture centered around an ESP32-S3 / STM32 cross-platform core.

## Pinout & Subsystems
- **I2C Bus 1:** Ambient Environmental Sensors (SCD41 CO2, SHT45 Temp/Humid).
- **Analog Input:** pH Probe (Isolated), EC Probe (1kHz AC Excitation).
- **PWM Control:** Nutirent Pump (MOSFET), LED Spectrometer (4-Channel Dimming).
- **Communication:** CAN-Bus for habitat integration, Wi-Fi for telemetry.

## Schematic Files
- `ASTRO_BOTANY_CORE_V1.pdf`: Main control board schematic.
- `BOM.csv`: Bill of materials for space-rated component alternatives.
