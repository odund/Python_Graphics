'''
Create a scene with graphics methods

Created on Jun 23, 2020
@author: olegg
'''

from graphics import *

def main():
    win = GraphWin('Scene with graphic methods', 400, 400)
    win.yUp()
    win.setBackground('yellow')

    base = Point(30, 200)

    for nxtPt in [Point(50, 300), Point(70, 100), Point(90, 250), Point(110, 155), Point(130, 225), Point(150, 200), Point(170, 200), Point(350, 200)]:
        line = Line(base, nxtPt)
        base = nxtPt
        line.setOutline('red')
        line.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to change scene')
    message.setTextColor('green')
    message.draw(win)
    win.getMouse()
    win.setBackground('pink')
    #message = Text(Point(win.getWidth()/2, 30), 'Click on five points')
    message.setText('Click on five points')
    message.setTextColor('blue')
    #message.draw(win)
    # Get and draw five vertices
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)
    vertices = [p1, p2, p3, p4, p5]
    # Use Polygon object to draw pentagon
    pentagon = Polygon(vertices)
    pentagon.setFill('cyan')
    pentagon.setOutline('gray')
    pentagon.setWidth(3)
    pentagon.draw(win)

    #message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit')
    message.setText('Click anywhere to quit')
    message.setTextColor('green')
    #message.draw(win)
    win.getMouse()
    win.close()

main()
