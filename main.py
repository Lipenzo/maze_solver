from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 800)
    p1 = Point(10, 10)
    p2 = Point(20, 20)
    line = Line(p1, p2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()