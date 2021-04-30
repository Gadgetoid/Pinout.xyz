<!--
---
name: Monarco HAT
class: board
type: adc, dac, io, led, com, rtc, power, motor
formfactor: HAT
manufacturer: Monarco
collected: Other
description: Industrial I/O for the Raspberry Pi
url: https://monarco.io
github: https://github.com/monarco
schematic: http://www.monarco.io/docs/Monarco-HAT-Hardware-Reference-Manual.pdf
buy: https://www.monarco.io/#buy-monarco-hat
image: 'monarco-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    name: RS-485, can be disabled
    mode: uart
  '10':
    name: RS-485, can be disabled
    mode: uart
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '37':
    name: ID EEPROM write enable
    mode: output
    active: low
  '38':
    name: MCU bootloader enable
    mode: output
    active: high
  '40':
    name: MCU RESETn
    mode: output
    active: low
i2c:
  '0x18':
    name: Real Time Clock Module
    device: MCP79410
  '0x6f':
    name: 1-Wire Interface Controller
    device: DS2482-100
-->
#Monarco HAT

Fabricado por Monarco Solutions Group / REX Controls s.r.o., Monarco HAT es una solución todo en uno para usar Raspberry Pi en la automatización industrial. Proporciona entradas y salidas analógicas y digitales, así como interfaces de comunicación RS-485 y 1-Wire. De hecho, convierte la Raspberry Pi en un PLC o una mini PC industrial (IPC) lista para usar en su proyecto de automatización.

Todas las entradas y salidas están diseñadas para interactuar directamente con sensores y dispositivos industriales estándar, eliminando la necesidad de hardware adicional.

##Características

- ** Fuente de alimentación: 10-30 VDC **, alimenta también la Raspberry Pi
- ** 4x entrada digital, 3.5-30 VDC **, aislamiento óptico, GND común
    - 2x contador (pulso / DIR) o 2x codificador (A / B), hasta 200 kHz
    - Retención de valores de contador durante el apagado
- ** 4x SALIDA digital **, drenaje abierto, máx. 40 V CC, 1 A por canal continuo
    - Todo con hasta 100 kHz PWM
    - Protección contra cortocircuitos (continua)
- ** 2 entradas analógicas **, 0-10 V / 0-20 mA, 12 bits
    - Conmutación electrónica del modo de detección de voltaje / corriente
    - Protegido contra sobretensión y polaridad inversa
    - Ancho de banda de 500 Hz, filtro configurable
- ** 2x OUT analógico **, 0-10 V, tiempo de establecimiento de 0,5 ms, 12 bits
- ** 1x bus RS-485 ** con protección ESD
- ** 1x bus de 1 cable ** con protección ESD
- ** Indicador LED 9x **, asignado de forma predeterminada como indicadores para entradas y salidas digitales y estado del sistema, controlable por el usuario
- ** Terminales push-in de alta calidad **, conector desmontable
- ** Chip RTC respaldado por batería ** para mantener la noción del tiempo
- ** Watchdog de hardware ** para apagar y encender el Raspberry Pi en caso de falla
- Compatible con la ** pantalla táctil oficial ** Raspberry Pi 7 "(conector integrado para alimentar la pantalla)
- ** EMC probado, marcado CE **
