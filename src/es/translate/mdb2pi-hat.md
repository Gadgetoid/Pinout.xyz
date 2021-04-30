<!--
---
name: MDB2Pi HAT
class: board
type: IO,Power
formfactor: HAT
manufacturer: Abrantix
collected: Other
description: Multi-Drop-Bus MDB Converter Board for the Raspberry Pi
url: http://blog.abrantix.com/webshop/mdb-converter/
buy: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi
image: 'mdb2pi-hat.png'
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
    mode: UART
  '10':
    mode: UART
  '27':
    mode: i2c
  '28':
    mode: i2c
i2c:
  '0x50':
    name: HAT EEPROM on I2C0
    device: 24C32
  '0x51':
    name: RTC on I2C1
    device: PCF8563
-->
# MDB2Pi HAT

El MDB2Pi es un HAT de Raspberry Pi que puede servir como un maestro MDB (VMC), como un periférico sin efectivo MDB o como un rastreador para máquinas expendedoras MDB. Se ocupa del formato específico de MDB de 9 bits, las restricciones eléctricas y de temporización. Reenvía la carga útil de MDB a la Raspberry Pi UART utilizando un protocolo en serie simple. El MDB2Pi se alimenta a través del bus MDB (suministro regulado o no regulado de 10 ... 42 V) y retroalimenta Raspberry Pi con hasta 2.5 A a 5 V. Por lo tanto, no se requiere una fuente de alimentación separada. Además, el MDB2Pi contiene un reloj de tiempo real (RTC), protegido por un supercondensador.

Una carcasa para el MDB2Pi (y el propio MDB2Pi) está disponible en la tienda web de Abrantix: http://blog.abrantix.com/webshop/product/mdb-to-raspberrypi/. Alternativamente, puede descargar un modelo 3D gratuito aquí: http://www.thingiverse.com/thing:2209661

Para la configuración y más información, consulte http://blog.abrantix.com/webshop/mdb-to-raspberry-pi-configuration/
