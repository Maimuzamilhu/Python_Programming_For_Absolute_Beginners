class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [['' for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.table[row][col] = value
        else:
            print("Invalid row or column index")

    def display(self):
        for row in self.table:
            print('| ' + ' | '.join(row) + ' |')

# Usage
table = Table(3, 3)
table.insert(0, 0, 'User')
table.insert(0, 1, 'Input')
table.insert(0, 2, 'Class')
table.display()
