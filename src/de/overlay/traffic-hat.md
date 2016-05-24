<!--
---
name: Traffic HAT
manufacturer: Ryanteck LTD.
url: http://www.ryanteck.uk/store/traffichat
buy: http://www.ryanteck.uk/store/traffichat
description: Ein schneller und einfacher Weg um die grundlegenden Fähigkeiten der GPIO-Ports zu erkunden.
pincount: 40
pin:
  '15':
    name: LED1 / Grün
    direction: output
    active: high
  '16':
    name: LED2 / Orange
    direction: output
    active: high
  '18':
    name: LED3 / Rot
    direction: output
    active: high
  '22':
    name: Taster
    direction: input
    active: high
  '29':
    name: Buzzer
    direction: output
    active: high
-->
#Traffic HAT

###Ein schneller und einfacher Weg um die grundlegenden Fähigkeiten der GPIO-Ports zu erkunden.

```python
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

#Lights
IO.setup(22,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)

#Buzzer
IO.setup(5,IO.OUT)

#Button
IO.setup(25,IO.IN,pull_up_down=IO.PUD_UP)
```