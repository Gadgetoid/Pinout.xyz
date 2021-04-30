<!--
---
name: JamHat
class: board
type: multi
formfactor: HAT
manufacturer: ModMyPi
description: A Jam friendly board with 6 LEDs, 2 buttons and a buzzer.
url: https://www.modmypi.com/jam-hat
github: https://github.com/modmypi/Jam-HAT
buy: http://www.modmypi.com/jam-hat
image: 'modmypi-jamhat.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
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
  '29':
    name: LED1
    direction: output
    active: high
  '31':
    name: LED2
    direction: output
    active: high
  '32':
    name: LED3
    direction: output
    active: high
  '33':
    name: LED4
    direction: output
    active: high
  '36':
    name: LED5
    direction: output
    active: high
  '11':
    name: LED6
    direction: output
    active: high
  '12':
    name: Button 2/Right Button
    direction: input
    active: high
  '35':
    name: Button 1/Left Button
    direction: input
    active: high
  '38':
    name: Buzzer
    direction: output
    active: high
-->
#Jam Hat


Un LED, botón y timbre ideal para Raspberry Jams, Jam Makers y personas que aprenden los conceptos básicos de GPIO.

El HAT tiene 6 LED, 2 botones y un zumbador tonal que permite mucha experimentación de hardware utilizando la biblioteca GPIO Zero para facilitar su uso.
`` `
from gpiozero import JamHat
from time import sleep

jh = JamHat()

# Turn the hat on, wait and turn it off.
jh.on()
sleep(1)
jh.off()

# Play tones through the buzzer.
jh.buzzer.play('C4')
sleep(0.5)
jh.buzzer.play('D4')
sleep(0.5)
jh.buzzer.play('E4')
sleep(0.5)
jh.off()

# Use the buttons to turn on lights.
jh.button_1.when_pressed = jh.lights_1.on
jh.button_1.when_released = jh.lights_1.off
jh.button_2.when_pressed = jh.lights_2.on
jh.button_2.when_released = jh.lights_2.off
´´´

Las guías de inicio completas están disponibles en el [sitio web de ModMyPi] (https://www.modmypi.com/blog/getting-started-with-the-jamhat)
