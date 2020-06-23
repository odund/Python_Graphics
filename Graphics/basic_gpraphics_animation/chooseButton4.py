'''
Make a choice of colors via mouse clicks in Rectangles --
Demonstate loops using lists of tuples of data.

Created on Jun 23, 2020
@author: olegg
'''

from graphics import *

def isBetween(x, end1, end2):
    '''Return True if x is between the ends or equal to either.
    The ends do not need to be in increasing order.'''
    
    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):
    '''Return True if the point is inside the Rectangle rect.'''
    
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

def makeColoredRect(corner, width, height, color, win):
    ''' Return a Rectangle drawn in win with the upper left corner
    and color specified.'''

    corner2 = corner.clone()  
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def getChoice(choicePairs, default, win):     #NEW
    '''Given a list choicePairs of tuples with each tuple in the form
    (rectangle, choice), return the choice that goes with the rectangle
    in win where the mouse gets clicked, or return default if the click
    is in none of the rectangles.'''

    point = win.getMouse()
    for (rectangle, choice) in choicePairs:
        if isInside(point, rectangle):
            return choice
    return default

def makeButtonSetup(colors):
    initButtons = list()
    x = 310
    y = 390

    for col in colors:
        y -= 40
        initButtons.append((x, y, col))
    return initButtons
        
def main():
    win = GraphWin('pick Colors', 400, 400)
    win.yUp() 

    #NEW
    choicePairs = list()
    colors = ['red', 'yellow', 'blue', 'brown', 'orange', 'cyan', 'green']
    buttonSetup = makeButtonSetup(colors)
    
    for (x, y, color) in buttonSetup:
       button = makeColoredRect(Point(x, y), 80, 30, color, win)
       choicePairs.append((button, color))

    house = makeColoredRect(Point(60, 200), 180, 150, 'gray', win)
    door = makeColoredRect(Point(90, 150), 40, 100, 'white', win)
    window = makeColoredRect(Point(160, 150), 60, 60, 'white', win)
    roof = Polygon(Point(50, 200), Point(250, 200), Point(150, 300))
    roof.setFill('black')
    roof.draw(win)
    chemney = Polygon(Point(180, 270), Point(180, 300), Point(200, 300),
                      Point(200, 250))
    chemney.setFill('black')
    chemney.draw(win)
    
    #NEW
    shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof'),
                  (window, 'window'), (chemney, 'chemney')] 
    msg = Text(Point(win.getWidth()/2, 375),'')
    msg.draw(win)
    for (shape, description) in shapePairs:
        prompt = 'Click to choose a ' + description + ' color.'
        msg.setText(prompt)
        color = getChoice(choicePairs, 'white', win)
        shape.setFill(color)

    outlinePairs = [(house, 'houseOutline'), (door, 'doorOutline'),
                    (roof, 'roofOutline'), (window, 'windowOutline'),
                    (chemney, 'chemneyOutline')]
    for (outline, description) in outlinePairs:
        prompt = 'Click to choose a ' + description + ' color.'
        msg.setText(prompt)
        color = getChoice(choicePairs, 'white', win)
        outline.setWidth(3)
        outline.setOutline(color)

    win.promptClose(msg)

main()
