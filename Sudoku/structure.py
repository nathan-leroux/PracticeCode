#sudoku file structure

'''
grid as dict
list of grid values as readoff
list reads back aswell
using string formula to make grid referances

zeros are blank spaces


'''
#defining the grid
import csv
import logging


class GridAbstract:
    def __init__(self, grid_platform, input, output):
        self.grid_platform = grid_platform
        self.input_csv = input
        self.output_csv = output

    def open(self):
        self.grid_platform.read_csv(self.input_csv)
        self.grid_platform.possibilities_check()

    def print(self):
        print(self.grid_platform)

    def solve(self):
        pass

    def solve_one_loop(self):
        self.grid_platform.solve_loop()

    def write(self):
        self.grid_platform.write_csv(self.output_csv)


class GridPlatform:
    def __init__(self, solve_platform):
        logging.debug(f'#####GridPlatform created')
        self.grid  = self._make_grid(0)
        self.possibility = self._make_grid([])
        self.solve_platform = solve_platform

    def __str__(self):
        string = ''
        count = 0
        block_count = 0
        vert_count = 0
        for x in self.grid.values():
            if block_count == 2 and count == 3:
                string += '\n'
                block_count = 0
                count = 0
                vert_count += 1
            if vert_count == 3:
                string += '- - - + - - - + - - -\n'
                vert_count = 0
            if count == 3:
                string += '| '
                count = 0
                block_count += 1
            string += f'{x} '
            count += 1
        string += '\n'
        return string

    def make_box(self, ref):
        grouplist = []
        box_centres = {'11':'22', '21':'52', '31':'82',
                       '12':'25', '22':'55', '32':'85',
                       '13':'28', '23':'58', '33':'88'}
        switch = {'1': '1',
                  '2': '1',
                  '3': '1',
                  '4': '2',
                  '5': '2',
                  '6': '2',
                  '7': '3',
                  '8': '3',
                  '9': '3'}
        adjusted_ref0 = switch.get(ref[0])
        adjusted_ref1 = switch.get(ref[1])
        box_centre = box_centres.get(adjusted_ref0 + adjusted_ref1)

        for y in range(-1,2):
            row = int(box_centre[1]) + y
            for x in range(-1,2):
                coloumn = int(box_centre[0]) + x
                grouplist.append(f'{coloumn}{row}')
        return grouplist

    def make_row(self, ref):
        grouplist = []
        row = int(ref[1])
        for coloumn in range(1,10):
            grouplist.append(f'{coloumn}{row}')
        return grouplist

    def make_coloumn(self, ref):
        grouplist = []
        coloumn = int(ref[0])
        for row in range(1,10):
            grouplist.append(f'{coloumn}{row}')
        return grouplist

    def _make_grid(self, default):
        logging.debug(f'***_make_grid called    input: {default} type: {type(default)}')
        grid = {}
        for x in range(1, 10):
            for y in range(1, 10):
                string = str(y) + str(x)
                grid.setdefault(string, default)
        logging.debug(f'output: {grid} type: {type(grid)}')
        return grid

    def possibilities_check(self):
        logging.debug('***possibilities_check called')
        for key in self.grid.keys():
            if self.grid[key] == 0:
                possible_values = [1,2,3,4,5,6,7,8,9]
                row = self.make_row(key)
                coloumn = self.make_coloumn(key)
                box = self.make_box(key)
                neighboor_cells = row + coloumn + box
                for cell in neighboor_cells:
                    if self.grid[cell] in possible_values:
                        possible_values.remove(self.grid[cell])
                self.possibility[key] = possible_values
            else:
                self.possibility[key] = []

    def read_csv(self, csv_file):
        logging.debug('***read_csv called')
        with open(csv_file) as file:
            file_reader = csv.reader(file)
            data = []
            for row in file_reader:
                data += row
        count = 0
        for key in self.grid.keys():
            self.grid[key] = int(data[count])
            count += 1

    def write_csv(self, output):
        logging.debug(f'***write_csv called    input: {output} type: {type(output)}')
        with open(output, 'w', newline='') as file:
            file_writer = csv.writer(file)
            data = []
            count = 0
            for value in self.grid.values():
                data.append(value)
                count += 1
                if count == 9:
                    file_writer.writerow(data)
                    data = []
                    count = 0

    def create_reference_set(self, reference_list):
        logging.debug(f'***create_referance_set called   input: {reference_list} type {type(reference_list)}')
        solved = []
        possibilities = []
        for ref in reference_list:
            solved.append(self.grid[ref])
            possibilities.append(self.possibility[ref])
        set = ReferenceSet(reference_list, solved, possibilities)
        logging.debug(f'output: refset type: {type(set)}')
        return set

    def solve_loop(self):
        logging.debug(f'***solve_loop called')
        sort_list = []
        for x in ['11', '22', '33', '44', '55', '66', '77', '88', '99']:
            sort_list.append(self.make_row(x))
            sort_list.append(self.make_coloumn(x))
        for y in ['22', '25', '28', '52', '55', '58', '82', '85', '88']:
            sort_list.append(self.make_box(y))
        for group in sort_list:
            reference_set = self.create_reference_set(group)
            result = self.solve_platform.solve(reference_set)
            if result is not None:
                self.grid[result[1]] = result[0]
                self.possibilities_check()


class SolvePlatform:
    def __init__(self):
        logging.debug(f'#####SolvePlatform created')
        self.reference_set = None
        self.number_count = None
        self.solve_test_number = 1

    def solve(self, reference_set):
        logging.debug(f'***solve called\n* * * ATTEMPT #{self.solve_test_number} * * *\ninput:\n{reference_set}')
        self.update_attempt_no()
        self.reference_set = reference_set
        self._tally_numbers()
        count = 0
        solved_value = None
        strat_list = [self.singles,
                      self.hidden_singles]
        while solved_value is None and count < len(strat_list):
            strat = strat_list[count]
            solved_value = strat()
            count += 1
        logging.debug(f'output: {solved_value} type: {type(solved_value)}')
        return solved_value

    def _tally_numbers(self):
        number_count = {}
        for cell in self.reference_set.possible_numbers:
            for number in cell:
                number_count.setdefault(number, 0)
                number_count[number] += 1
        self.number_count = number_count

    def update_attempt_no(self):
        self.solve_test_number += 1

    def singles(self):
        logging.debug('attempting singles')
        count = 0
        for cell in self.reference_set.possible_numbers:
            if len(cell) == 1:
                logging.debug('!!!!\tsingles method successful!')
                return (cell[0], self.reference_set.grid_ref[count])
            count += 1

    def hidden_singles(self):
        logging.debug('attempting hidden singles')
        count = 0
        for number in self.number_count.keys():
            if self.number_count[number] == 1:
                for cell in self.reference_set.possible_numbers:
                    if number in cell:
                        logging.debug('!!!\thidden singles method successful')
                        return (number, self.reference_set.grid_ref[count])
                    count += 1

class ReferenceSet():
    def __init__(self, reference_list, solved, possibilities):
        logging.debug(f'#####ReferanceSet created')
        self.grid_ref = reference_list
        self.solved_numbers = solved
        self.possible_numbers = possibilities

    def __str__(self):
        string = ''
        for count in range(0,9):
            string += f'ref:  {self.grid_ref[count]}\t'
            if self.solved_numbers[count] != 0:
                string += f'cell:  {self.solved_numbers[count]}\t\t\t{self.possible_numbers[count]}\n'
            else:
                string += f'cell:  {self.possible_numbers[count]}\n'
        return string

