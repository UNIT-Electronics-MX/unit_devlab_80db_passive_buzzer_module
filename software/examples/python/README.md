# UNIT Buzzer Module - MicroPython Example

Este ejemplo demuestra cómo controlar el módulo buzzer pasivo de UNIT Electronics usando MicroPython con señales PWM.

## Conexiones de Hardware

```
Buzzer Module    Microcontrolador
-----------      ----------------
Signal Pin   ->  GPIO 6
VCC          ->  3.3V o 5V
GND          ->  GND
```

## Características del Código

### Clase BuzzerController

La clase principal que maneja el control del buzzer con las siguientes funciones:

- **`play_tone(frequency, duration, duty_cycle)`**: Reproduce un tono a una frecuencia específica
- **`beep(frequency, duration, duty_cycle)`**: Función simple para hacer beeps
- **`play_scale(base_freq, steps, step_duration)`**: Reproduce una escala musical
- **`play_alarm(low_freq, high_freq, cycles, cycle_duration)`**: Patrón de alarma alternando frecuencias
- **`frequency_sweep(start_freq, end_freq, duration, steps)`**: Barrido de frecuencias
- **`test_duty_cycles(frequency, duration)`**: Prueba diferentes ciclos de trabajo

### Rangos Recomendados

- **Frecuencia**: 500 Hz a 5000 Hz (rango óptimo para el buzzer)
- **Duty Cycle**: 0 a 1023 (0% a 100%)
- **Duración**: Cualquier valor positivo en segundos

## Uso Básico

```python
from main import BuzzerController

# Inicializar el controlador
buzzer = BuzzerController(pin=6)

# Beep simple
buzzer.beep(1000, 0.5)  # 1000 Hz por 0.5 segundos

# Tono continuo
buzzer.play_tone(800, 2.0)  # 800 Hz por 2 segundos

# Detener sonido
buzzer.stop()
```

## Ejemplos de Prueba

El archivo incluye una función `main()` que ejecuta varios tests:

1. **Beeps básicos**: Prueba diferentes frecuencias
2. **Escala musical**: Reproduce una escala cromática
3. **Patrón de alarma**: Alterna entre dos frecuencias
4. **Barrido de frecuencias**: Transición suave entre frecuencias
5. **Prueba de duty cycles**: Diferentes intensidades de sonido

## Cómo Ejecutar

1. Copia el archivo `main.py` a tu microcontrolador con MicroPython
2. Conecta el buzzer al GPIO 6
3. Ejecuta el código:

```python
# Para la suite completa de tests
exec(open('main.py').read())

# O importa y usa funciones específicas
from main import BuzzerController
buzzer = BuzzerController(pin=6)
buzzer.beep(1000, 0.5)
```

## Parámetros Técnicos

- **GPIO Pin**: 6 (configurable)
- **Frecuencia PWM**: 500-5000 Hz recomendado
- **Duty Cycle**: 512 (50%) por defecto para mejor calidad de sonido
- **Voltaje**: 3.3V o 5V compatible

## Notas Importantes

- El buzzer es **pasivo**, requiere señal PWM para generar sonido
- Frecuencias fuera del rango 500-5000 Hz pueden tener menor volumen
- El duty cycle afecta el volumen percibido y la claridad del sonido
- Usa `buzzer.stop()` para detener el sonido completamente

## Troubleshooting

- **No hay sonido**: Verifica las conexiones y que el buzzer sea pasivo
- **Sonido débil**: Ajusta el duty cycle o verifica el voltaje de alimentación
- **Frecuencia incorrecta**: Asegúrate de usar el rango 500-5000 Hz