<!--
---
name: Skywriter HAT
manufacturer: Pimoroni
url: https://github.com/pimoroni/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
description: un capteur de mouvements 3D
install:
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'skywriter'
  'examples': 'python/examples/'
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: reset
  '13':
    name: transfer
-->
#Skywriter HAT

Le Skywriter est capable de détecter la position de vos doigts dans l'espace défini en 3 dimensions au dessus de son capteur. Il transfère les coordonnées X, Y et Z à votre Raspi, qui sont dès lors disponibles pour effectuer l'opération désirée au sein de votre script.

En analysant ces données dans le temps il est aussi possible de reconnaître toutes sortes de gestes et de les traiter de manière appropriée.

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS get.pimoroni.com/skywriter | bash
```
