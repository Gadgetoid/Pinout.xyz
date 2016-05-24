<!--
---
name: Display-o-Tron 3000
manufacturer: Pimoroni
url: https://github.com/pimoroni/dot3k
description: 3 satır destekleyen, RGB renkli arka plana sahip bir LCD ve joystick
  butonları
pincount: 26
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Joystick Button
    mode: input
    active: low
  '11':
    name: Joystick Left
    mode: input
    active: low
  '13':
    name: Joystick Up
    mode: input
    active: low
  '15':
    name: Joystick Right
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick Down
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
-->
#Display-o-Tron 3000

Aşağıdaki tek satır kodla Display-o-Tron 3000'u kurup kullanmaya başlayabilirsiniz. Yapmanız gereken tek şey terminalde şu komutu çalıştırmak,

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

ve de karşınıza gelen yönergeleri takip etmek.