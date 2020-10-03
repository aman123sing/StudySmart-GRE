import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def EightWaySymmetricalPoints(xc,yc,x,y):
    setpixel(x+xc,y+yc)
    setpixel(x+xc,-y+yc)
    setpixel(-x+xc,-y+yc)
    setpixel(-x+xc,y+yc)
    setpixel(y+xc,x+yc)
    setpixel(y+xc,-x+yc)
    setpixel(-y+xc,-x+yc)
    setpixel(-y+xc,x+yc)
    
def bresenhamCircle(xi,yi,r):
    x=0
    y=r
    d=3-(2*r)
    EightWaySymmetricalPoints(xi,yi,x,y)
    while x<=y:
        if d<=0:
            d=d+(4*x)+6
            x=x+1
        else:
            d=d+4*(x-y)+10
            x=x+1
            y=y-1
        EightWaySymmetricalPoints(xi,yi,x,y)




def setpixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def iterate():
    glClearColor(0.0,0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,200.0,0.0,150.0)

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    bresenhamCircle(80,80,40)
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50,100)
glutInitWindowSize(400,300)
glutCreateWindow("Bresenham's Circle Algorithm - 1811071")
iterate()
glutDisplayFunc(showscreen)
glutMainLoop()