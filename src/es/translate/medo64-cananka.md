<!--
---
name: Cananka
class: board
type: other
collected: Other
formfactor: HAT
manufacturer: Josip Medved
description: Cananka is Raspberry Pi HAT allowing for CAN bus communication.
url: https://medo64.com/cananka/
github: https://github.com/medo64/cananka/
image: 'medo64-cananka.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Interrupt
    mode: input
    active: low
  '23':
    mode: spi
  '24':
    mode: spi
-->
# Cananka

Cananka es un HAT para Raspberry Pi que permite la comunicación del bus CAN.

Las características incluyen hasta 1Mbit / s de velocidad de bus (125 kbit / s por defecto); completamente aislado
(1 kV); no requiere fuente de alimentación del bus CAN (convertidor de CC a CC integrado);
admite la alimentación de Raspberry Pi desde el bus CAN (hasta 24 V, 2 A); automático
detección a través de la especificación HAT; funciona en Raspberry Pi B + y superior (incluido
Pi Zero).
