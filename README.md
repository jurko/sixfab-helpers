# Sixfab IoTHat Helper


## Usage

    ./bg96.py command [commands]
    commands one of:
      - on
      - unlock (-p <pin>)
      - off
      - info
      - connect


## Installation

 * Follow https://docs.sixfab.com/docs/getting-started-with-cellular-hat-sixfab-connect-sim
    * Do NOT install the Sixfab library, but used this package instead
    * However follow their dependency installation (either in our main python or in a virtual env)
    * Dependencies
      * `Adafruit-GPIO>=0.9.3`, `pyserial`, `adafruit-ads1x15`, and `RPi`
      * `RPi` package, on my system is provided by `python3-rpi.gpio`
