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
def CreateCanvas(size = (100,100)):
    row = []
    for _ in range(size[0]):
        row.append(0)
    canvas = []
    for _ in range(size[1]):
        canvas.append(row)
    return canvas

def Get8neightbours(cell = [0,0]):
    x = cell[0]
    y = cell[1]
    return [
            (x+1,y),
            (x-1,y),
            (x,y+1),
            (x,y-1),
            (x+1,y+1),
            (x+1,y-1),
            (x-1,y+1),
            (x-1,y-1),
            ]
