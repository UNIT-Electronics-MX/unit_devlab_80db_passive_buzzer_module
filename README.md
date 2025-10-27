# DevLab: 80dB Passive Buzzer Module

<div align="center">
    <a href="#"><img src="https://img.shields.io/badge/version-1.0-blue.svg" alt="Version"></a>
    <a href="#"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
    <br>
</div>

<div align="center">
    <a href="#">
        <img src="hardware/resources/unit_top_ue0088_modulo_buzzer_v_1_1_0.png" width="500px" alt="UNIT Buzzer Module"><br/>
        UNIT Buzzer Module
    </a>
</div>
<br/>

This module is a compact, easy-to-use **passive** buzzer component designed for embedded systems and prototyping. It features a standardized 3-pin interface: **VCC (5V)**, **Signal**, and **GND**, allowing seamless integration with a variety of microcontrollers, such as `Arduino`, `ESP32`, `CH552`, and `STM32` boards.

> **_NOTE:_** The buzzer onboard can generate audible signals for use in **alarms**, **notifications**, **timers**, and **user feedback systems**. Its design includes a pre-mounted drive circuit, enabling direct digital control from microcontroller GPIO pins.

## Additional Resources

<div align="center">

| Resource              | Link                                                                                                                        |
|:---------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| Wiki-UNIT Electronics | [Wiki - UNIT Electronics](https://unit-electronics-mx.github.io/wiki_uelectronics/es/docs/Modules/buzzer_module)                   |
| Github Repository     | [Github Repository](https://github.com/UNIT-Electronics-MX/unit_buzzer_module)                              |
| Product Brief         | [Product brief](docs/unit_product_brief.pdf)                                                   |
| Schematic             | [Schematic](hardware/unit_sch_v_1_1_0_ue0088_modulo_buzzer.pdf)                                                           |

</div>


## Features

- 🧩 3-pin standard interface: `+5V`, `Signal`, `GND`
- 🔊 Built-in buzzer (active or passive)
- 📏 Compact footprint with mounting hole


## Applications

- Fire or Gas Detection Alarm System
- Elderly Health Monitoring System
- Secure Access Control with Intrusion Alerts using RFID
- Automotive Diagnostic Panel
- Smart Irrigation System with Fault Alerts
- Autonomous Drone or Robot Alert System

## 🔄 Alert Priority System (Optional) 
- 🔴 Continuous tone → Critical failure
- 🟡 Intermittent tone → Warning or moderate event
- 🔵 Short beep → Event confirmation or feedback


> 🔧 Note: use **PWM signals** to generate tones.
<div align="center">
    <img src="hardware/resources/img/sonido.gif" alt="Sound Icon" width="100"/>
</div>


## Documentation and Setup

### Overview
This repository contains firmware and documentation for integrating the Relay Module into your projects.

### Installation
1. Clone the repository:
   ```
    git@github.com:UNIT-Electronics-MX/unit_buzzer_module.git
   ```
2. Navigate to the project directory:
   ```
   cd ./unit_buzzer_module.git
   ```
3. Follow the platform-specific setup instructions detailed in the project documentation.

### Usage
Include the module initialization and configuration routines in your main project file. Sample code snippets and detailed explanations can be found in the documentation folder of the repository.


## Support
For any issues or further assistance, please open an issue on the GitHub repository or contact our support team.


## LICENSE 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


