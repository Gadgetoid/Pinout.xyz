<!--
---
name: MotoZero
class: board
type: motor
formfactor: pHAT
manufacturer: PiHut
description: Control 4 motors from your Raspberry Pi
url: https://thepihut.com/products/motozero
buy: https://thepihut.com/products/motozero
image: 'motozero.png'
pincount: 40
eeprom: no
power:
  '2':
  '4':
ground:
  '20':
  '39':
pin:
  '11':
    name: "Motor 2 EN"
  '12':
    name: "Motor 4 -"
  '13':
    name: "Motor 1 -"
  '15':
    name: "Motor 2 -"
  '16':
    name: "Motor 3 +"
  '18':
    name: "Motor 1 +"
  '22':
    name: "Motor 4 EN"
  '29':
    name: "Motor 1 EN"
  '31':
    name: "Motor 2 +"
  '32':
    name: "Motor 3 EN"
  '33':
    name: "Motor 4 +"
  '36':
    name: "Motor 3 -"
-->
# MotoZero


MotoZero es una placa adicional de controlador de motor Raspberry Pi simple que le permite controlar hasta 4 motores de forma independiente.
Con un simple control GPIO y su propia entrada a la biblioteca GPIO Zero, es una de las formas más fáciles de controlar muchos motores en su Raspberry Pi.

caracteristicas:

* Controle 4 motores de forma independiente tanto en avance como en retroceso
* Control con el código básico de encendido / apagado de GPIO, o usando la biblioteca GPIO Zero
* Los terminales rompen las salidas del motor al borde de la placa
* Diodos de protección de voltaje de retorno integrados
* Adecuado para todos los modelos de 40 pines Raspberry Pi
