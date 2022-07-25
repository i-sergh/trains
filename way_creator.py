import cv2
import numpy as np
from random import randint, choice
from time import time
from rails import Cross
#def doPass(*args):
#    pass

#def mouseCallbackDecorator(event=0, x=0, y=0, flags=0, param=0, func=doPass):
    
#    def wrapper(event, x, y, flags, param):
#        print('hi')
#        func(event, x, y, flags, param)

#    return wrapper

def dotsDestroy(event, x, y, flags, param):
    global d
    
    for i in range(len(d)):
        d[i].set_cross(event, x, y, flags, param)


class Dot:
    """
    Класс точки  интерфейса
    Должен магнититься к точке перекрестка
    """
    def __init__ (self, cnv, x, y):
        # центр точки
        self.x = x
        self.y = y
        # предположительно разница от точки до позиции мыши
        self.dx = 0
        self.dy = 0
        # отображение точки
        self.visible = True

        # счетчик времени
        self.ttime = time()

        # холст
        self.cnv = cnv

        # должен появляться свой перекресток

        self.cross = Cross(self.cnv, self.x, self.y,
              randint(0,1), randint(0,1), randint(0,1), randint(0,1),
              randint(0,1), randint(0,1), randint(0,1), randint(0,1), 
              randint(0,1), randint(0,1), randint(0,1), randint(0,1)
                        )
        
    
    def visibility(self):
        self.visible = not self.visible
        
        print( time() - self.ttime  )
        
        if self.visible and time() - self.ttime > 0.1 :
            self.draw()
            self.ttime = time()
        elif not self.visible and time() - self.ttime > 0.1 :
            self.destroy()
            self.ttime = time()
        
    def draw(self):
        cv2.circle(self.cnv, (self.x, self.y ), 5, (0, 255,255), -1  )
        ###
        self.cross.draw()
        ###
    def destroy(self):
        cv2.circle(self.cnv, (self.x, self.y ), 5, (0, 0, 0), -1  )
        ###
        self.cross.destroy()
        ###
        
        #cv2.circle(self.cnv, (self.x, self.y ), 5, (0, 255, 255), 1  )
    
    def set_cross(self,event, x,y, flags, param):
        #"""
        #    Должно по позиции мыши отрисовывать
        #    но только одну точку
        #"""
        #print(event, x,y, flags, param)
        
        if flags == 1 and abs(x - self.x) < 20 and abs(y - self.y) < 20:
            self.visibility()


if __name__ == '__main__':
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )
    for_mouse = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )



    cv2.namedWindow('TRAINS')
    cv2.setMouseCallback( 'TRAINS',  dotsDestroy )
    global d
    d = [] 
    for x in range(60, WINDOW_WIDTH-30, 60 ):
        for y in range(60, WINDOW_HEIGHT-30, 60 ):
            d.append( Dot(cnv, x, y) )
            d[-1].draw()
            
            
    
    #d = Dot(300, 300)

    #cv2.setMouseCallback('TRAINS', set_cross)
    #cv2.setMouseCallback('TRAINS', d.set_cross)
    while True:
        cv2.imshow('TRAINS', cnv)
        key = cv2.waitKey(1)
        if key == 27: # ESC
            break
    cv2.destroyAllWindows()



