SCL (I2C1 Clock) is one of the i2c pins on the Pi, [learn more about i2c](/pinout/i2c).

SCL includes a fixed, 1.8 kΩ pull-up to 3.3v, which means this pin is not suitable for use as a general purpose IO where no pull-up resistor is desired.

This pin can be used to power up the Pi by pulling it low (but only after a clean shutdown, which puts the Pi in a deep sleep mode with the bootloader monitoring this pin). This makes this pin very suitable for a power button. See [this blogpost](https://www.stderr.nl/Blog/Hardware/RaspberryPi/PowerButton.html) for more info.
