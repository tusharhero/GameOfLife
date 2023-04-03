"""
The GPLv3 License (GPLv3)

Copyright (c) 2023 Tushar Maharana

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import gol_engine as gol
import time

alive: str = "⬜"
dead: str = "⬛"

try:
    size: tuple = tuple(eval(input("Enter the size: ")))
except:
    size: tuple = (10, 10)

canvas: list = gol.CreateCanvas(size)

for x_index in range(len(canvas)):
    print(f" {x_index} ", end="")
for y_index in range(len(canvas[0])):
    print(f"\n{y_index}{canvas[y_index]}", end="")

print("\nEnter the coordinates you want to spell life into:")

while True:
    try:
        coordinates: tuple = tuple(eval(input()))
    except:
        break

    canvas[coordinates[0]][coordinates[1]] = 1

for g in range(1000):
    print(chr(27) + "[2J")  # escape codes to clear the terminal
    print(f"generation:{g}")
    for row in canvas:
        for cell in row:
            if cell == 1:
                print(alive, end="")
            else:
                print(dead, end="")
        print()
    canvas = gol.GetNextGen(canvas)
