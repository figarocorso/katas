class Minesweeper():

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.field = [['.' for column in range(columns)] for rows in range(rows)]
        self.calculated_field = [['.' for column in range(columns)] for rows in range(rows)]

    def plant_mine(self, column, row):
        self.field[column][row] = '*'

        return self

    def get_item_at(self, column, row):
        return self.field[column][row]

    def fill_adjacent_mine_number(self):
        self.calculated_field = [[self.calculate_adjacent_mine_number(column,row) for column in range(columns)] for rows in range(rows)]

        return self


    def calculate_adjacent_mine_number(self, column, row):

