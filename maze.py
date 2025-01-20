from cell import Cell
from point import Point
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_colls, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_colls = num_colls
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for x in range(0, self.num_colls):
            collum = []
            self._cells.append(collum)
            for y in range(0, self.num_rows):
                cell = Cell(self.win)
                collum.append(cell)
                point1 = Point(x*self.cell_size_x, y*self.cell_size_y)
                point2 = Point(point1.x + self.cell_size_x, point1.y + self.cell_size_y)
                self._draw_cell(x, y)
    
    def _draw_cell(self, x_mul, y_mul):
        x = self.x1 + x_mul * self.cell_size_x
        y = self.y1 + y_mul * self.cell_size_y
        x2 = x + self.cell_size_x
        y2 = y + self.cell_size_y
        self._cells[x_mul][y_mul].draw(Point(x, y), Point(x2, y2))
        self._animate()
    
    def _animate(self):
        if  self.win:
            self.win.redraw()
            sleep(0.05)