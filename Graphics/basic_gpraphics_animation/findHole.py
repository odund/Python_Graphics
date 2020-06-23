'''
A grphical program game - Find The Hole. This program uses a random
number generator to determine a circular hole, selecting a point and a
radius around that point. These determine the target and are not revealed
to the player initially. The user is then prompted to click around on
the screen to find the hidden hole. It shows the points the user has
tried. Once the user selects a point that is within the chosen radius of
the mystery point, the mystery circle should appear. There is a message
announcing how many steps it took, and the game should end.

Created on Jun 23, 2020
@author: olegg
'''

from graphics import *
import random

def getShift(point1, point2):
    '''Returns a tuple (dx, dy) which is the shift from point1 to point2.'''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return (dx, dy)

def getRandomPoint(xLow, xHigh, yLow, yHigh):
    '''Return a random Point with coordinates in the range specified.'''
    x = random.randrange(xLow, xHigh+1)
    y = random.randrange(yLow, yHigh+1)
    return Point(x, y)

def makeHole(center, radius, win):
    '''return a black disk that is drawn in win with given center and radius.'''
    disk = Circle(center, radius)
    disk.setOutline("black")
    disk.setFill("black")
    disk.draw(win)
    return disk

def getDistance(point, userPt, win):
    (dx, dy) = getShift(point, userPt)
    distance = (dx*dx + dy*dy) ** 0.5
    print(distance)
    return distance

def main():
    win = GraphWin('Find the Hole', 300, 300)
    win.yUp()

    lineHeight = win.getHeight() - 40
    textHeight = win.getHeight() - 20
    Line(Point(0, lineHeight), Point(win.getWidth(), lineHeight)).draw(win)
    
    radius = random.randrange(10, 20)
    xLow = radius
    xHigh = win.getWidth() - radius
    yLow = radius
    yHigh = lineHeight - radius
    center = getRandomPoint(xLow, xHigh, yLow, yHigh)
    print("Center: ", center, " Radius: ", radius)
  
    message = Text(Point(win.getWidth()/2, textHeight), 'Click in any point')
    message.setTextColor('green')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)

    #Run game here
    countSteps = 0
    userPt = win.getMouse()
    userPt.draw(win)
    countSteps = countSteps + 1
    distance = getDistance(center, userPt, win)
    while (distance > radius):
        userPt = win.getMouse()
        userPt.draw(win)
        countSteps = countSteps + 1
        distance = getDistance(center, userPt, win)
    hole = makeHole(center, radius, win)
    print("Found the hole! It took", countSteps, "steps")
    
    message.setText('Found! It took ' + str(countSteps) +
                    ' steps.\nClick anywhere to quit')
    win.getMouse()
    win.close()    

main()
