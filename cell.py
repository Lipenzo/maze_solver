from point import Point
from tkinter import Canvas
from line import Line

class Cell:
    size = 10

    def __init__(self, canvas, point, left=True, top=True, right=True, bottom=True):
        self.left = True
        self.top = True
        self.right  = True
        self.bottom = True
        self._x1 = point.x
        self._y1 = point.y
        self._x2 = self._x1 + self.size
        self._y2 = self._y1 + self.size
        self._win = canvas

    def draw(self, point1, point2):
        fill_color = "black"
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        if self.left:
            Line(point1, Point(point1.x, point2.y)).draw(self._win, fill_color)
        if self.top:
            Line(point1, Point(point2.x, point1.y)).draw(self._win, fill_color)
        if self.right:
            Line(point2, Point(point2.x, point1.y)).draw(self._win, fill_color)
        if self.bottom:
            Line(point2, Point(point1.x, point2.y)).draw(self._win, fill_color)

    def middle_point(self):
        return Point( (self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, to_cell, undo=False):
        mid_point = self.middle_point()
        other_mid= to_cell.middle_point()
        line = Line(mid_point, other_mid)
        if undo:
            line.draw(self._win, "grey")
        else:
            line.draw(self._win, "red")