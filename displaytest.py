#!/usr/bin/env python
# four row lcd screen

import i2c_driver
import time

mydisplay = i2c_driver.lcd()

while True:
    mydisplay.lcd_display_string("Kids Alarm Clock", 1)
    mydisplay.lcd_display_string(time.strftime('%I:%M:%S %p'), 2)
    mydisplay.lcd_display_string(time.strftime('%a %b %d, 20%y'), 3)
    mydisplay.lcd_display_string("Alarm Time", 4)
