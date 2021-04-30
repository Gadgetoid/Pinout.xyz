<!--
---
name: Coral Environmental Sensor Board
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Google
description: An Environmental Sensor and Grove Breakout Board
url: https://coral.withgoogle.com/products/environmental
github: https://coral.googlesource.com/coral-cloud/
buy: https://coral.withgoogle.com/products/environmental
image: 'coral-enviro-board.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    mode: uart
  '10':
    mode: uart
  '12':
    mode: pwm
  '13':
    name: OPT3002_INT
    mode: input
    active: low
  '16':
    name: Push Button
    mode: input
    active: low
  '18':
    name: OLED DC
    mode: output
    active: high
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: OLED RESET
    mode: output
    active: low
  '23':
    mode: spi
  '24':
    mode: spi
  '29':
    name: A71CH_RST_N
    mode: output
    active: low
  '33':
    mode: pwm
  '35':
    name: HDC2010_DRDY
    mode: input
    active: high
  '40':
    name: LED
    mode: output
    active: high
i2c:
  '0x30':
    name: Cyptographic Secure Element
    device: ECC608
  '0x40':
    name: Humidity/Temperature Sensor
    device: HDC2010
  '0x45':
    name: Wide Spectrum Ambient Light Sensor
    device: OPT3002
  '0x49':
    name: Single-Channel ADC
    device: TLA2021
  '0x76':
    name: Barometric Pressure Sensor
    device: BMP280

-->
#Coral Environmental Sensor Board

Coral Environmental Sensor Board añade múltiples sensores ambientales y conectores Grove para dispositivos externos. Funciona con todas las variantes de Rasperry Pi de 40 pines, así como con la placa Coral Dev.

Características:

* Pantalla OLED de 128x32 (interfaz SPI basada en SSD1306)
* Sensor de luz ambiental (OPT3002, 0x45 en bus i2c)
* Sensor de presión barométrica (BMP280, 0x76 en el bus i2c)
* Sensor de humedad / temperatura (HDC2010, 0x40 en bus i2c)
* Criptoprocesador con claves de Google (ECC608, 0x30 en el bus i2c)
* Cuatro conectores Grove:
    1x UART
    1x I2C
    1x PWM
    1x analógico de 3.3 / 5V (usando TLA2022 ADC, 0x49 en el bus i2c)
* Botón de uso general
* LED de uso general
