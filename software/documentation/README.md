---
title: "UNIT Buzzer Module"
version: "1.0"
modified: "2025-05-08"
output: "buzzer_module"
subtitle: "A passive buzzer module is a sound-generating device that produces tones when controlled by a PWM signal from a microcontroller."
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->
 <!-- logo -->

# UNIT Buzzer Module

![product](./images/product.png)

## Introduction

This passive buzzer module requires a PWM (Pulse Width Modulation) signal or frequency generator to function.

When a PWM signal is applied to the passive buzzer, the frequency of this signal determines the pitch of the sound. This feature enables developers to produce musical tones, alarms of varying urgency, or simple feedback clicks—all from the same device.

## Functional Description

- The module contains a piezoelectric transducer without internal oscillation circuitry.
- Sound is produced only when driven by an external frequency source, such as a microcontroller PWM output.
- Operates efficiently in the audible frequency range between 500 Hz and 5 kHz.
- The module consists of three pins: VCC, GND, and SIGNAL, suitable for direct breadboard or header connection.

## Electrical Characteristics & Signal Overview

- Operating voltage: 3.0 V – 5.5 V (recommended 5 V)
- Current consumption: 5 mA – 30 mA depending on frequency
- Frequency range: 500 Hz – 5 kHz (nominal response)
- Logic level compatibility: 3.3 V / 5 V digital signals
- Drive type: External PWM (no internal tone generator)

## Applications

- Audio indication for buttons or events
- Timers and countdown alerts
- Warning and alarm systems
- Feedback for embedded user interfaces
- Educational or DIY electronics kits

## Features

- Requires external PWM signal (passive buzzer type)
- Compact module with 3-pin interface
- Wide voltage range (3.0 V to 5.5 V)
- Clear tone generation based on input frequency
- Breadboard-friendly layout
- Low power consumption

## Pin & Connector Layout

| PIN     | Description              |
|---------|--------------------------|
| VCC     | MCU logic voltage (5V)   |
| Signal  | Digital or PWM input     |
| GND     | Ground                   |

## Settings

### Interface Overview

| Interface  | Signals / Pins      | Typical Use                          |
|------------|---------------------|--------------------------------------|
| Digital    | Signal               | Accepts PWM from MCU                 |
| Power      | VCC, GND             | Connects to 5 V supply and ground    |

### Supports

| Symbol | I/O   | Description                         |
|--------|-------|-------------------------------------|
| VCC    | Input | Power supply (3.0 V to 5.5 V)       |
| GND    | Input | Electrical ground                   |
| SIG    | Input | Digital/PWM signal input            |

## Block Diagram

![Function Diagram](images/function-diagram.jpg)

## Dimensions

![Dimensions](images/dimensions.png)

## Usage

Works with:

- Arduino AVR
- Raspberry Pi RP2040
- STM32
- NRF
- PY32
- MAX II

## Downloads

- [Schematic PDF](../hardware/Schematics_UE0088_Buzzer_SMD-v1.0.pdf)

## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
