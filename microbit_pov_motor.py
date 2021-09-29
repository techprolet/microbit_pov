"""
microbit_pov_motor.py
https://www.instructables.com/Microbit-Persistence-of-Vision-Daisy

Part of "micro:bit Persistence-of-Vision daisy"
    Copyright 2021 Pavlos Iliopoulos, techprolet.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/ .
"""

from microbit import *


startPeriod = 10000
targetPeriod = 1000
pwm_value = 511
speedChangeWaitTime = 1

# accelerate motor till we reach the desired speed
def MotorTurn():
    global startPeriod
    global targetPeriod
    global speedChangeWaitTime
    global pwm_value

    thisPeriod = startPeriod

    pin1.write_analog(pwm_value)
    for i in range(targetPeriod, startPeriod):
        pin1.set_analog_period_microseconds(thisPeriod)
        sleep(speedChangeWaitTime)
        thisPeriod -= 1

# decelerate motor before stopping completely
def MotorStop():
    global startPeriod
    global targetPeriod
    global speedChangeWaitTime

    thisPeriod = targetPeriod
    for i in range(targetPeriod, startPeriod):
        pin1.set_analog_period_microseconds(thisPeriod)
        sleep(speedChangeWaitTime)
        thisPeriod += 1

    pin1.write_digital(0)

# button B starts motor, button A stops it
while True:
    if button_b.is_pressed():
        MotorTurn()
    if button_a.is_pressed():
        MotorStop()
    sleep(1)
