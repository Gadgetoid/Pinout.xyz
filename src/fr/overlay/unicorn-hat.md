<!--
---
name: Unicorn HAT
manufacturer: Pimoroni
url: http://shop.pimoroni.com/products/unicorn-hat
buy: http://shop.pimoroni.com/products/unicorn-hat
description: une matrice 8x8 de LEDs RGB
github: https://github.com/pimoroni/unicornhat
install:
  'apt':
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'unicornhat'
  'python3':
    - 'unicornhat'
  'examples': 'python/examples/'
pincount: 40
pin:
  '12':
    name: données
    direction: output
    mode: pwm
    active: high
    description: WS2812 Data
-->
#Unicorn HAT

l'Unicorn présente une matrice composée de 64 LEDs tricolores RGB contrôlées par une bibliothèque programmée en C, mais addressable depuis Python.

Important: l'opération de l'Unicorn au travers de la broche PWM n'est pas compatible avec l'usage de la sortie analogique audio de la Raspberry Pi, et il n'est pas possible d'utiliser les deux simultanément.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
