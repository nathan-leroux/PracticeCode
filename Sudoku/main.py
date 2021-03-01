#! python3
#main.py
#oh yeah, its all coming together
'''
initialise grid and pgrid
read in sudoku from csv to grid
fill out pgrid with shortlist
solver function
print finished sudoku
fin
'''
import logging
import csv

from structure import GridAbstract, GridPlatform, SolvePlatform

logging.basicConfig(level=logging.DEBUG,
                    format='%(filename)s : %(funcName)s\t: %(msg)s')

solve_platform = SolvePlatform()
grid_platform = GridPlatform(solve_platform)
grid_abstract = GridAbstract(grid_platform, 'P1.csv', 'P1edit.csv')

grid_abstract.open()
grid_abstract.solve_one_loop()
grid_abstract.write()
