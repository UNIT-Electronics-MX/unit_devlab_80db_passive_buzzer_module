# UNIT Buzzer Module - MicroPython Basic Example

This example demonstrates how to control the UNIT Electronics passive buzzer module using MicroPython with PWM signals in a simple and straightforward way.

## Hardware Connections

```
Buzzer Module    Microcontroller
─────────────    ───────────────
Signal Pin   →   GPIO 6
VCC          →   3.3V or 5V
GND          →   GND
```

## Code Features

### Simple Functions

The code provides basic functions for buzzer control:

- **`beep(frequency, duration)`**: Generate a simple beep at specified frequency
- **`stop()`**: Stop the buzzer immediately

### Recommended Ranges

- **Frequency**: 500 Hz to 5000 Hz (optimal range for the buzzer)
- **Duty Cycle**: 512 (50% - fixed for best sound quality)
- **Duration**: Any positive value in seconds

## Basic Usage

```python
# Simple beep
beep(1000, 0.5)  # 1000 Hz for 0.5 seconds

# Stop buzzer
stop()
```

## Test Examples

The file includes automatic tests that run when executed:

1. **Single beep**: Test at 1000 Hz
2. **Three quick beeps**: Rapid beeps at 1500 Hz
3. **Frequency test**: Tests multiple frequencies (500Hz, 1000Hz, 1500Hz, 2000Hz, 3000Hz)

## How to Run

1. Copy the `main.py` file to your MicroPython microcontroller
2. Connect the buzzer to GPIO 6
3. Run the code:

```python
# The test runs automatically when the file is executed
# Or use functions directly:
beep(1000, 0.5)  # Make a beep
stop()           # Stop sound
```

## Technical Parameters

- **GPIO Pin**: 6 (hardcoded in simple version)
- **PWM Frequency**: 500-5000 Hz recommended
- **Duty Cycle**: 512 (50%) fixed for optimal sound quality
- **Voltage**: 3.3V or 5V compatible

## Important Notes

- The buzzer is **passive**, requires PWM signal to generate sound
- Frequencies outside 500-5000 Hz range may have lower volume
- The duty cycle is set to 50% for optimal volume and clarity
- Use `stop()` to completely silence the buzzer

## Troubleshooting

- **No sound**: Check connections and ensure the buzzer is passive type
- **Weak sound**: Verify power supply voltage (3.3V/5V)
- **Wrong frequency**: Make sure to use the 500-5000 Hz range