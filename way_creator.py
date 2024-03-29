import cv2
import numpy as np
from random import randint, choice
from time import time
from rails import Cross
from train import Train



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
    idx = 0
    def __init__ (self, cnv, x, y):
        
        # центр точки
        self.x = x
        self.y = y
        # предположительно разница от точки до позиции мыши
        self.dx = 0
        self.dy = 0
        # отображение точки
        self.visible = False

        # счетчик времени
        self.ttime = time()

        # холст
        self.cnv = cnv

        # информация о соседях
        self.neighbor_up = None
        self.neighbor_down = None
        self.neighbor_left = None
        self.neighbor_right = None
        
        # должен появляться свой перекресток

        self.cross = Cross(self.cnv, self.x, self.y,
              #randint(0,1), randint(0,1), randint(0,1), randint(0,1),
              #randint(0,1), randint(0,1), randint(0,1), randint(0,1), 
              #randint(0,1), randint(0,1), randint(0,1), randint(0,1)
                           0,0,0,0,
                           0,0,0,0,
                           0,0,0,0
                        )
        
    
    def visibility(self):
        self.visible = not self.visible
        
        #self.cross.rail_interface("left", True)
        #self.cross.rail_interface("right", True)
        #self.cross.rail_interface("top", True)
        #self.cross.rail_interface("bottom", True)

        #self.cross.rail_interface("right_bottom", True)
        #self.cross.rail_interface("top_right", True)
        #self.cross.rail_interface("bottom_left", True)
        #self.cross.rail_interface("bottom_left", True)

        #self.cross.rail_interface("top_left", True)
        #self.cross.rail_interface("left_bottom", True)
        #self.cross.rail_interface("bottom_right", True)
        #self.cross.rail_interface("right_top", True)
        #self.cross.draw()
        # возможно время мы уберём >>> and time() - self.ttime > 0.1 
        if self.visible :
            
            if self.neighbor_left != None and self.neighbor_right != None and \
               self.neighbor_left.visible and self.neighbor_right.visible:
                
                self.cross.rail_interface("left", True)
                self.cross.rail_interface("right", True)

                self.neighbor_left.cross.rail_interface('right', True)
                              #                           #
                self.neighbor_right.cross.rail_interface('left', True)

                self.neighbor_left.cross.destroy()
                self.neighbor_right.cross.destroy()
                
                self.neighbor_left.cross.draw()
                self.neighbor_right.cross.draw()
              
            if self.neighbor_up != None and self.neighbor_down != None and \
               self.neighbor_up.visible and self.neighbor_down.visible:
                
                self.cross.rail_interface("top", True)
                self.cross.rail_interface("bottom", True)

                self.neighbor_up.cross.rail_interface('bottom', True)
                              #                           #
                self.neighbor_down.cross.rail_interface('top', True)

                self.neighbor_up.cross.destroy()
                self.neighbor_down.cross.destroy()
                
                self.neighbor_up.cross.draw()
                self.neighbor_down.cross.draw()
                
            if self.neighbor_up != None and self.neighbor_left != None and \
               self.neighbor_up.visible and self.neighbor_left.visible:
                
                self.cross.rail_interface("top_left", True)
                self.cross.rail_interface("left_top", True)

                self.neighbor_up.cross.rail_interface('bottom', True)
                              #                           #
                self.neighbor_left.cross.rail_interface('right', True)

                self.neighbor_up.cross.destroy()
                self.neighbor_left.cross.destroy()
                
                self.neighbor_up.cross.draw()
                self.neighbor_left.cross.draw()
                
            if self.neighbor_up != None and self.neighbor_right != None and \
               self.neighbor_up.visible and self.neighbor_right.visible:
                
                self.cross.rail_interface("top_right", True)
                self.cross.rail_interface("right_top", True)

                self.neighbor_up.cross.rail_interface('bottom', True)
                              #                           #
                self.neighbor_right.cross.rail_interface('left', True)

                self.neighbor_up.cross.destroy()
                self.neighbor_right.cross.destroy()
                
                self.neighbor_up.cross.draw()
                self.neighbor_right.cross.draw()

            if self.neighbor_down != None and self.neighbor_right != None and \
               self.neighbor_down.visible and self.neighbor_right.visible:
                
                self.cross.rail_interface("bottom_right", True)
                self.cross.rail_interface("right_bottom", True)

                self.neighbor_down.cross.rail_interface('top', True)
                              #                           #
                self.neighbor_right.cross.rail_interface('left', True)

                self.neighbor_down.cross.destroy()
                self.neighbor_right.cross.destroy()
                
                self.neighbor_down.cross.draw()
                self.neighbor_right.cross.draw()
            if self.neighbor_down != None and self.neighbor_left != None and \
               self.neighbor_down.visible and self.neighbor_left.visible:
                
                self.cross.rail_interface("bottom_left", True)
                self.cross.rail_interface("left_bottom", True)

                self.neighbor_down.cross.rail_interface('top', True)
                              #                           #
                self.neighbor_left.cross.rail_interface('right', True)

                self.neighbor_down.cross.destroy()
                self.neighbor_left.cross.destroy()
                
                self.neighbor_down.cross.draw()
                self.neighbor_left.cross.draw()                 
            self.draw()
            self.ttime = time()
            
        elif not self.visible  :

            self.destroy()
            self.neighbor_up.cross.destroy()
            self.neighbor_left.cross.destroy()
            self.neighbor_right.cross.destroy()
            self.neighbor_down.cross.destroy()
            self.cross.rail_interface("left", False)
            self.cross.rail_interface("right", False)
            self.cross.rail_interface("top", False)
            self.cross.rail_interface("bottom", False)

            self.cross.rail_interface("right_bottom", False)
            self.cross.rail_interface("top_right", False)
            self.cross.rail_interface("bottom_left", False)
            self.cross.rail_interface("bottom_left", False)

            self.cross.rail_interface("top_left", False)
            self.cross.rail_interface("left_bottom", False)
            self.cross.rail_interface("bottom_right", False)
            self.cross.rail_interface("right_top", False)

            self.neighbor_down.cross.rail_interface('top', False)
            self.neighbor_left.cross.rail_interface('right', False)
            self.neighbor_right.cross.rail_interface('left', False)
            self.neighbor_up.cross.rail_interface('bottom', False)

            
                
            self.neighbor_up.cross.draw()
            self.neighbor_left.cross.draw()
            self.neighbor_right.cross.draw()
            self.neighbor_down.cross.draw()

            
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
        """
        
            по позиции мыши отрисовывает
            но только одну точку

            Должна опросить соседей
            и по полученным данным видимости отрисовать свои пути
            и попросить это сделать соседей

            ето ихний
        """
        #print(event, x,y, flags, param)
        
        if flags == 1 and abs(x - self.x) < 20 and abs(y - self.y) < 20:
            self.visibility()
            
            
                

    def init_link(self, direction):
        # Привет, ето я. Ты для меня слева
        return self, direction

    def get_invite(self, seq):
        '''
            получение информации о соседе и отправка иформации о себе
        '''
        
        other_self, direction = seq[0], seq[1]
        
        # Если он видит меня слева, значит он справа
        if direction == 'left':
            self.neighbor_right = other_self
            
        # Если я для соседа сверху, то он сосед снизу
        elif direction == 'up':
            self.neighbor_down = other_self
        
        other_self.callback_invite( self, direction )
        
    def callback_invite(self, other_self, direction):
        '''
            получение информации о соседе только
        '''
        
        # Если сосед слева ответил, то он есть
        if direction == 'left':
            self.neighbor_left = other_self
            
        # Если сосед сверху ответил, то он есть
        elif direction == 'up':
            self.neighbor_up = other_self
    

if __name__ == '__main__':
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )
    for_train = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )

    idx = 0

    cv2.namedWindow('TRAINS')
    cv2.setMouseCallback( 'TRAINS',  dotsDestroy )
    global d
    d = [] 
    for x in range(60, WINDOW_WIDTH-30, 60 ):
        for y in range(60, WINDOW_HEIGHT-30, 60 ):
            d.append( Dot(cnv, x, y) )

            # для отладки
            d[-1].idx = idx
            idx += 1
            
            if len(d )> 1:
            #try:
                d[-2].get_invite( d[-1].init_link( 'up' ) )
                #print('im trying')
            #except:
             #   pass
            #d[-1].visibility()
            if len(d )> 9:
                d[-10].get_invite( d[-1].init_link( 'left' ) )
    

    trains_dot = randint(0,81) 

    d[trains_dot].visibility()

    tr = Train( d[trains_dot].y,
                 d[trains_dot].x,
                 d[trains_dot] )

    
    
    while True:
        for_train *= 0
        for_train = np.where(for_train!= 0 , for_train, cnv)

        tr.destroy(for_train)        
        
        tr.grad+=1

        tr.draw(for_train)

        cv2.imshow('TRAINS', for_train)

        
        key = cv2.waitKey(1)
        if key == 27: # ESC
            break

        if key == ord('w'): #вперед
            tr.move(for_train, -2, 0)
            
        if key == ord('s'): # назазд
            tr.move(for_train, 2, 0)
        if key == ord('a'): # влево
            tr.move(for_train, 0, -2)
        if key == ord('d'): # вправо
            tr.move(for_train, 0, 2)
    cv2.destroyAllWindows()



