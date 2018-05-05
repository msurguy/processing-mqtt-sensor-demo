import time
import paho.mqtt.publish as publish

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Connect ADS1115 sensor to the PI as follows:

# SDA goes to SDA Pin (pin 3 on the Pi)
# SCL goes to SCL Pin (pin 5 on the Pi)
# GND goes to pin 6 on the Pi
# VDD goes to pin 1 on the Pi

# 10KOhm potentiometer is connected to the ADS1115 as follows:
#
#       [ ]
#    ---------
#   |    |    |
#   |    |    |
#  VDD   A0  GND
#


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
adc.start_adc(0, gain=GAIN)
# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, or stop_adc() to stop conversions.

try:
  while True:
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    # WARNING! If you try to read any other ADC channel during this continuous
    # conversion (like by calling read_adc again) it will disable the
    # continuous conversion!

    # Uncomment the following line to get text output in the Python script execution console
    #print('Channel 0: {0}'.format(value))

    # Publish the value of the potentiometer reading to channel called "a0" on "localhost" machine
    publish.single("a0", value, hostname="localhost")

    # How long to pause between sensor readings (in seconds) and between publishing to MQTT channel 
    time.sleep(0.016)

except KeyboardInterrupt:
    print("Keyboard interrupt received, stopping the script")
finally:
    # clean up
    # Stop continuous conversion.  After this point you can't get data from get_last_result!
    adc.stop_adc()