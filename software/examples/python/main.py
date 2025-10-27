"""
UNIT Buzzer Module - Basic Test
MicroPython - GPIO 6

Simple buzzer test for passive buzzer module.
Frequency range: 500 Hz to 5 kHz

Connections:
- Signal -> GPIO 6
- VCC -> 3.3V
- GND -> GND
"""

from machine import Pin, PWM
import time

# Initialize buzzer on GPIO 6
buzzer_pin = Pin(6, Pin.OUT)
buzzer = PWM(buzzer_pin)

def beep(frequency, duration):
    """Make a simple beep"""
    buzzer.freq(frequency)
    buzzer.duty(512)  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty(0)    # Stop sound

def stop():
    """Stop buzzer"""
    buzzer.duty(0)

# Basic test
print("Testing UNIT Buzzer Module...")

# Test 1: Single beep
print("1. Single beep (1000 Hz)")
beep(1000, 0.5)
time.sleep(0.5)

# Test 2: Three quick beeps
print("2. Three quick beeps")
for i in range(3):
    beep(1500, 0.2)
    time.sleep(0.2)

time.sleep(1)

# Test 3: Different frequencies
print("3. Testing frequencies (500-3000 Hz)")
frequencies = [500, 1000, 1500, 2000, 3000]
for freq in frequencies:
    print(f"   {freq} Hz")
    beep(freq, 0.3)
    time.sleep(0.2)

print("Test completed!")