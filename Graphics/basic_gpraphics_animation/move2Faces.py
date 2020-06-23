'''
Test animation of a group of objects making a face.
Combine the face elements in a function, and use it twice.
Have an extra level of repetition in the animation.
This version may be wobbly and slow on some machines

Created on Jun 23, 2020
@author: olegg
'''

from graphics import *
import time

def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''    
    for shape in shapeList: 
        shape.move(dx, dy)
            
def moveAllOnLine(shapeList1, shapeList2, dx, dy, repetitions, delay):
    '''Animate the shapes in shapeList along a line.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    '''
    for i in range(repetitions):
        moveAll(shapeList1, dx, dy)
        moveAll(shapeList2, -dx, dy)
        time.sleep(delay)

def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face.
    '''
    
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone()
    eye1Center.move(-10, 5)
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    nosePt1 = center.clone()
    nosePt1.move(0, 5)
    nosePt2 = center.clone()
    nosePt2.move(-5, -5)
    nosePt3 = center.clone()
    nosePt3.move(5, -5)
    nose = Polygon(nosePt1, nosePt2, nosePt3)
    nose.setOutline('red')
    nose.setFill('green')
    nose.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, nose, mouth]

def main():
    win = GraphWin('2 Faces Back and Forth', 300, 300)
    win.yUp()

    faceList1 = makeFace(Point(30, 100), win)
    faceList2 = makeFace(Point(270,200), win)

    stepsAcross = 46
    dx = 5
    wait = .05
    
    for i in range(2):
        moveAllOnLine(faceList1, faceList2, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList1, faceList2, -dx, 0, stepsAcross, wait)

    win.promptClose(win.getWidth()/2, 20)

main()
