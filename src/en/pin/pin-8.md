This pin doubles up as the UART transmit pin, TX. It's also commonly known as "Serial" and, by default, will output a Console from your Pi that, with a [suitable Serial cable](https://elinux.org/RPi_Serial_Connection), you can use to control your Pi via the command line.

The UART pins can be useful for setting up a "headless" Pi (a Pi without a screen) and getting it connected to a network.

UART can be used to talk to Serial GPS modules or sensors such as the PM5003, but you must make sure you disable the Serial Console in raspi-config first.

By default on the Pi 3, Pi 4 and Pi Zero W the full, hardware UART is used for Bluetooth and the Pi's UART pins are connected to the less stable miniUART. To achieve a stable UART connection to other devices, you may need to add "dtoverlay=miniuart-bt" to "/boot/config.txt". This has the effect of switching Bluetooth over to miniUART, freeing the full UART for use to connect to other devices.

Note that all UARTs are 3.3V only and damage will occur if they are connected to 5V systems.

[Learn more about UART](/pinout/uart)

[Raspberry Pi UART documentation](https://www.raspberrypi.org/documentation/configuration/uart.md)
