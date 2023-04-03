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


def CreateCanvas(size: tuple = (100, 100)) -> list:
    row: list = []
    for _ in range(size[0]):
        row.append(0)
    canvas: list = []
    for _ in range(size[1]):
        canvas.append(row.copy())
    return canvas


def GetAlivecells(Canvas: list) -> list:
    alivecells: list = []
    for row in range(len(Canvas)):
        for column in range(len(Canvas[0])):
            if Canvas[row][column] == 1:
                alivecells.append((row, column))
    return alivecells


def Getneighbours(canvas: list, coordinates: tuple = (0, 0)) -> list:
    x: int = coordinates[0]
    y: int = coordinates[1]
    neighbours: list = []
    for row in range(x - 1, x + 1 + 1):
        for column in range(y - 1, y + 1 + 1):
            if (
                not (row == x and column == y)
                and (row >= 0 and column >= 0)
                and (row < len(canvas[0]) and column < len(canvas[0]))
            ):
                neighbours.append((row, column))
    return neighbours


def GetneighbourPopulation(Canvas: list, neighbours: list) -> int:
    population: int = 0
    for cell in neighbours:
        if GetCell(Canvas, cell) == 1:
            population += 1
    return population


def GetCell(canvas: list, coordinates: tuple = (0, 0)) -> int:
    return canvas[coordinates[0]][coordinates[1]]


def GetNextGen(canvas: list) -> list:
    alivecells: list = GetAlivecells(canvas)
    NextGenCanvas: list = CreateCanvas((len(canvas[0]), len(canvas)))
    for alivecell in alivecells:
        neighbours: list = Getneighbours(canvas, alivecell)
        for coordinates in neighbours + [alivecell]:
            x, y = coordinates[0], coordinates[1]
            cell = GetCell(canvas, coordinates)
            cellneighbours: list = Getneighbours(canvas, coordinates)
            neighbourPopulation: int = GetneighbourPopulation(canvas, cellneighbours)
            if cell == 1:
                if neighbourPopulation in [2, 3]:
                    NextGenCanvas[x][y] = 1
                else:
                    NextGenCanvas[x][y] = 0
            else:
                if neighbourPopulation == 3:
                    NextGenCanvas[x][y] = 1
                else:
                    NextGenCanvas[x][y] = 0
    return NextGenCanvas
