import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
def dda(xi,yi,xf,yf):
   dx=xf-xi
   dy=yf-yi
   if(abs(dx)>abs(dy)):
       steps=abs(dx)
   else:
       steps=abs(dy)
   xinc=dx/float(steps)
   yinc=dy/float(steps)
   x=xi
   y=yi
   i=0
   while i<=steps:
       setpixel(x,y)
       x=x+xinc
       y=y+yinc
       i=i+1
 
def setpixel(x,y):
   glBegin(GL_POINTS)
   glVertex2f(x,y)
   glEnd()
 
def iterate():
   glClearColor(0.0,0.0,0.0,0.0)
   glMatrixMode(GL_PROJECTION)
   gluOrtho2D(0.0,200.0,0.0,150.0)
 
def displayscreen():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0.0,0.0,1.0)
   dda(15,95,80,60)
   glFlush()
 
 
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(50,100)
glutInitWindowSize(400,300)
glutCreateWindow("DDA Algo - 1811071")
iterate()
glutDisplayFunc(displayscreen)
glutMainLoop()
