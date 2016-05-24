<!--
---
name: Display-o-Tron HAT
manufacturer: Pimoroni
url: https://github.com/pimoroni/dot3k
description: Un LCD da 3 righe di caratteri, RGB retroilluminato a 6 zone con 6 bottoni touch
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '19':
    mode: spi
  '22':
    name: LCD Register Select
    mode: output
  '23':
    mode: spi
  '24':
    name: LCD Chip Select
    mode: chipselect
    active: high
  '32':
    name: LCD Reset
    mode: output
    active: low
-->
#Display-o-Tron HAT

Il Display-o-Tron HAT usa sia l'SPI che l'I2c per controllare il display LCD, la retroilluminazione e il touchscreen. 
Entrambi questi bus possono essere comunque condivisi con altre periferiche.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

&hellip;e seguire le istruzioni!
