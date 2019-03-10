#!/usr/bin/env python
# pre-req : install scheduler module

import schedule
import subprocess
import time

def job():
    subprocess.call(['mpg321 /home/pi/songofyourchoice.mp3'], shell=True)
    
schedule.every().day.at('5:50').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
