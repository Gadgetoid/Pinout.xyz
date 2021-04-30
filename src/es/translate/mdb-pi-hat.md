<!--
---
name: MDB HAT
class: board
type: io
formfactor: HAT
manufacturer: Qibixx
description: MDB (Machine Data Bus) Bus Interface
url: https://qibixx.com
buy: https://qiba.pt/
image: 'mdb-pi-hat.png'
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
  '8':
    name: TxD
    mode: UART
    description: Serial TX > MDB Controller
  '10':
    name: RxD
    mode: UART
    description: Serial RX < MDB Controller
  '19':
    name: SPI_MOSI
    mode: spi
    description: MDB Controller - MOSI
  '21':
    name: SPI_MISO
    mode: spi
    description: MDB Controller – MISO
  '23':
    name: SPI_SCLK
    mode: spi
    description: MDB Controller - SCLK
  '24':
    name: SPI_CE0
    mode: spi
    description: MDB Controller – CS
  '27':
    name: ID_SD
    mode: I2C
    description: ID EEPROM DTA
  '28':
    name: ID_SC
    mode: I2C
    description: ID EEPROM CLK
  '29':
    name: IO2RPI
    mode: output
    description: IO MDB>RPi
  '31':
    name: MDB_RES
    mode: input
    description: MDB Contoller Reset
  '33':
    name: IOfromRPi
    mode: input
    description: IO RPi>MDB
-->
# MDB HAT

El MDBHAT de [Qibixx] (https://qibixx.com) es un Raspberry Pi HAT que conecta Raspberry Pi con el MDB (Machine Data Bus), que se encuentra en máquinas expendedoras y periféricos, como los receptores de monedas y billetes. Con su arquitectura avanzada, MDB Hat puede admitir aplicaciones MDB Master, MDB Peripheral y MDB Sniffing sin ninguna configuración de puente.

El firmware de MDBHAT se puede actualizar desde Pi.

Para conectividad universal, el HAT MDB se conecta con Raspberry Pi con una interfaz serial o SPI.
El MDB HAT es alimentado por el Pi, sin embargo, también puede proporcionar hasta 15W (5V, 3A) y retroalimentar el Pi si hay energía MDB disponible. En la mayoría de las aplicaciones, el MDB HAT plus Pi e incluso otros periféricos se pueden usar sin una fuente de alimentación adicional.

La documentación completa del dispositivo y la información del protocolo están disponibles [aquí] (https://docs.qibixx.com).

Se puede encontrar información general sobre MDB y una descripción general de la familia de dispositivos [aquí] (https://mdb.technology).
