'''
This program asks the user to click the mouse, and then
it draws a face at the point where the user clicked. This
action repeated six times: After each of 6 mouse clicks, a
face immediately appears at the location of the latest click.

Created on Jun 23, 2020
@author: olegg
'''

from graphics import *

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
    win = GraphWin('Face', 300, 300)
    win.yUp()

    message = Text(Point(win.getWidth()/2, 30), 'Click in any point')
    message.setTextColor('green')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)

    for i in range(6):
        p = win.getMouse()
        faceList = makeFace(p, win)

    message.setText('Click anywhere to quit')
    win.getMouse()
    win.close()

main()
