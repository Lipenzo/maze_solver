from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    maze = Maze(10, 10, 10, 15, 20, 20, win)
    
    """ 
    p1 = Point(10, 10)
    p2 = Point(110, 110)
    p3 = Point(110, 10)
    p4 = Point(210, 110)
    line = Line(p1, p2)
    win.draw_line(line)
    cell = Cell(win)
    cell2 = Cell(win)
    cell.draw(p1, p2)
    cell2.draw(p3, p4)
    cell.draw_move(cell2)
    """
    win.wait_for_close()

main()