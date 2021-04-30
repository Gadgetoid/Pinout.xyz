<!--
---
name: Christmas Tree Star
class: board
type: LED
formfactor: Custom
manufacturer: ModMyPi
description: A star shaped LED add-on board for the Raspberry Pi which can be used as a Christmas Tree topper.
url: https://www.modmypi.com/raspberry-pi-christmas-tree-star
github: https://github.com/modmypi/Programmable-Christmas-Star
buy: https://www.modmypi.com/raspberry-pi-christmas-tree-star
image: 'modmypi-star.png'
pincount: 40
eeprom: no
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
    name: Inner
    mode: output
    active: high
  '5':
    name: S
    mode: output
    active: high
  '7':
    name: R
    mode: output
    active: high
  '8':
    name: T
    mode: output
    active: high
  '10':
    name: W
    mode: output
    active: high
  '11':
    name: Q
    mode: output
    active: high
  '12':
    name: V
    mode: output
    active: high
  '13':
    name: P
    mode: output
    active: high
  '15':
    name: O
    mode: output
    active: high
  '16':
    name: U
    mode: output
    active: high
  '18':
    name: X
    mode: output
    active: high
  '19':
    name: N
    mode: output
    active: high
  '21':
    name: M
    mode: output
    active: high
  '22':
    name: Y
    mode: output
    active: high
  '23':
    name: L
    mode: output
    active: high
  '24':
    name: B
    mode: output
    active: high
  '26':
    name: A
    mode: output
    active: high
  '29':
    name: K
    mode: output
    active: high
  '31':
    name: J
    mode: output
    active: high
  '32':
    name: C
    mode: output
    active: high
  '33':
    name: I
    mode: output
    active: high
  '35':
    name: H
    mode: output
    active: high
  '36':
    name: F
    mode: output
    active: high
  '37':
    name: G
    mode: output
    active: high
  '38':
    name: E
    mode: output
    active: high
  '40':
    name: D
    mode: output
    active: high
-->
# Christmas Tree Star

El ModMy Pi Christmas Tree Star es una placa adicional LED para Raspberry Pi diseñado para ir encima de su árbol de Navidad. Hay 30 LED blancos controlables a través de una biblioteca Python que extiende GPIO Zero y está disponible en GitHub.

## Caracteristicas
- 30 LED blancos
- Biblioteca GPIO Zero compatible.
- Puntos de montaje para Raspberry Pi Zero.
- [Guía de compilación del árbol de Navidad] (https://www.modmypi.com/blog/christmas-tree-star-guide)

## Sample Code
```
from star import Star
from time import sleep

# Initialise the star
star = Star()

# Turn the star on and off.
star.on()
sleep(1)
star.off()

# Turn the inner and outer LEDs off.
star.outer.on()
sleep(1)
star.off()
star.inner.on()
sleep(1)
star.off()

# Turn on individual LEDs on the outer rim.
star.outer.A.on()
star.outer.F.on()
star.outer.P.on()
star.outer.X.on()
sleep(1)
star.off()
```
