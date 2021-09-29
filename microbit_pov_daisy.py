"""
microbit_pov_daisy.py
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
import utime


# total rotation time is 200000us
wait_time = 200000
rotations_step = 2  # allow two rotations TODO: Find better naming

daisyImg = [
    Image(
        5,
        5,
        bytearray(
            [0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0]
        ),
    ),
    Image(
        5,
        5,
        bytearray(
            [0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
    ),
    Image(
        5,
        5,
        bytearray(
            [0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
    ),
    Image(
        5,
        5,
        bytearray(
            [0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
    ),
    Image(
        5,
        5,
        bytearray(
            [0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ),
    ),
]


display.on()
imgSize = len(daisyImg)
i = 0
rotations = 0
while True:
    rotations += 1
    rotations %= rotations_step
    if rotations == 0:
        display.show(daisyImg[i])
        i += 1
        i %= imgSize

    utime.sleep_us(wait_time)
