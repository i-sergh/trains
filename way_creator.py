import cv2
import numpy as np
from random import randint, choice

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
               dtype=np.uint8() )
for_mouse = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
               dtype=np.uint8() )

def mouseCallbackDecoraor(event, x, y, flags, param, func):
    pass


class Dot:
    """
    Класс точки  интерфейса
    Должен магнититься к точке перекрестка
    """
    def __init__ (self, x, y):
        # центр точки
        self.x = x
        self.y = y
        # предположительно разница от точки до позиции мыши
        self.dx = 0
        self.dy = 0
        # отображение точки
        self.visible = False
    
    def visibility(self):
        self.visible = not self.visible
        
    def draw(self):
        cv2.circle(cnv, (self.x, self.y ), 5, (0, 255,255), -1  )
        self.visibility()
        
    def destroy(self):
        cv2.circle(cnv, (self.x, self.y ), 5, (0, 0, 0), -1  )
        self.visibility()
    
    def set_cross(self,event, x,y, flags, param):
        #"""
        #    Должно по позиции мыши отрисовывать
        #    но только одну точку
        #"""
        print(event, x,y, flags, param)
        
        if flags == 1 and abs(x - self.x) < 50 and abs(y - self.y):
            self.destroy()


cv2.namedWindow('TRAINS')
d = [] 
for x in range(60, WINDOW_WIDTH-30, 60 ):
    for y in range(60, WINDOW_HEIGHT-30, 60 ):
        d.append( Dot(x, y) )
        d[-1].draw()
        cv2.setMouseCallback( 'TRAINS', d[-1].set_cross )

#d = Dot(300, 300)

#cv2.setMouseCallback('TRAINS', set_cross)
#cv2.setMouseCallback('TRAINS', d.set_cross)
while True:
    cv2.imshow('TRAINS', cnv)
    key = cv2.waitKey(1)
    if key == 27: # ESC
        break
cv2.destroyAllWindows()



