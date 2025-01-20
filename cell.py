from point import Point
from tkinter import Canvas
from line import Line

class Cell:
    size = 10

    def __init__(self, win):
        self.left = True
        self.top = True
        self.right  = True
        self.bottom = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, point1, point2):
        fill_color = "black"
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        if self.left:
            self._win.draw_line(Line(point1, Point(point1.x, point2.y)))
        if self.top:
            self._win.draw_line(Line(point1, Point(point2.x, point1.y)))
        if self.right:
            self._win.draw_line(Line(point2, Point(point2.x, point1.y)))
        if self.bottom:
            self._win.draw_line(Line(point2, Point(point1.x, point2.y)))

    def middle_point(self):
        return Point( (self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, to_cell, undo=False):
        mid_point = self.middle_point()
        other_mid= to_cell.middle_point()
        line = Line(mid_point, other_mid)
        if undo:
            self._win.draw_line(line, "grey")
        else:
            self._win.draw_line(line, "red")