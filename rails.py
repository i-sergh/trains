import cv2
import numpy as np
from random import randint, choice
'''
class Dot:
    """
    Класс точки  интерфейса
    Должен магнититься к точке перекрестка
    """
    def __init__ (self,cnv, x, y):
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
        pass
    def destroy(self):
        pass
    
    def set_cross(self,event, x,y, flags, param):
        #"""
        #    Должно по позиции мыши отрисовывать
        #    но только одну точку
        #"""
        print(event, x,y, flags, param)
'''


class Cross:
    def __init__(self, cnv, x, y, top, bottom, left, right,
                 top_right, right_bottom, bottom_left,  left_top,
                 top_left,  left_bottom,  bottom_right, right_top):
        '''
            x & y - center of the cross
        '''
        self.x = x
        self.y = y
        
        self.step = 30
        # холст
        self.cnv = cnv

        # список направлений
        self.nlist = [
                      top, bottom, left, right,
                      top_right, right_bottom, bottom_left,  left_top,
                      top_left,  left_bottom,  bottom_right, right_top
                      ]
        # хранение индексов направлений
        self.ndict = {'top':0, 'bottom':1, 'left':2, 'right':3,
                      'top_right':4, 'right_bottom':5, 'bottom_left':6,  'left_top':7,
                      'top_left':8,  'left_bottom':9,  'bottom_right':10, 'right_top':11}

        # информация для точек отрисовки
        self.drawDots = [# точка старта |  точка финиша
                            [  (x, y),   (x, y - self.step)], # top
                            [  (x, y),   (x, y + self.step)], # bottom
                            [  (x, y),   (x - self.step, y)], # left
                            [  (x, y),   (x + self.step, y)], # right
                         # центр  | угол старта | угол финиша 
                            [(x + self.step, y - self.step), 180, 135 ], # top right
                            [(x + self.step, y + self.step), 225, 270 ], # right bottom
                            [(x - self.step, y + self.step), 315, 360], # bottom left
                            [(x - self.step, y - self.step), 45, 90], # left_top

                            [(x - self.step, y - self.step), 0, 45], # top left
                            [(x - self.step, y + self.step), 270, 315], # left bottom
                            [(x + self.step, y + self.step), 180, 225], # bottom right
                            [(x + self.step, y - self.step), 90,  135]  # right top
                          ]
        # параметры пути
        
        self.paramWay  = [ # поворот или прямая| видимо не видимо
                           [True, True],  # top
                           [True, True],  # bottom 
                           [True, True],  # left 
                           [True, True],  # right
                           
                           [False, True], # top right
                           [False, True], # right bottom
                           [False, True], # bottom left
                           [False, True], # left_top

                           [False, True], # top left
                           [False, True], # left bottom
                           [False, True], # bottom right
                           [False, True]  # right top
                        ]
        self.paramWay[0][1] &= top + bottom
        self.paramWay[1][1] &= top + bottom
        self.paramWay[2][1] &= left + right
        self.paramWay[3][1] &= left + right

        self.paramWay[4][1] &= top_right + right_top
        self.paramWay[5][1] &= right_bottom + bottom_right
        self.paramWay[6][1] &= bottom_left + left_bottom
        self.paramWay[7][1] &= left_top + top_left

        self.paramWay[8][1] &= left_top + top_left
        self.paramWay[9][1] &= bottom_left + left_bottom
        self.paramWay[10][1] &= right_bottom + bottom_right
        self.paramWay[11][1] &= top_right + right_top
                                                                                                
    def draw(self):
        for i, zn in enumerate(self.nlist):
            if self.paramWay[i][1]:
                if self.paramWay[i][0]:
                    if zn:
                    
                        cv2.line(self.cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (250, 200,30), 4 )
                    else:
                        cv2.line(self.cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (0, 0,255), 4 )
                else:
                    if zn:
                    
                        cv2.ellipse(self.cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (250, 200,30), 4 )
                    else:
                        cv2.ellipse(self.cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (0, 0,255), 4 )
    
    def destroy(self):
        for i, zn in enumerate(self.nlist):
            if self.paramWay[i][1]:
                # для прямых
                if self.paramWay[i][0]:
                    if zn:
                    
                        cv2.line(self.cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (0, 0,0), 4 )
                    else:
                        cv2.line(self.cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (0, 0,0), 4 )
                # для дуг
                else:
                    if zn:
                    
                        cv2.ellipse(self.cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (0, 0,0), 4 )
                    else:
                        cv2.ellipse(self.cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (0, 0,0), 4 )

    def rail_interface (self, rail_side, val ):
        self.nlist [
                self.ndict[rail_side]
            ] = val

        self.update_params()
    def rail_q_interface(self, rail_side ):
        return self.nlist [
                self.ndict[rail_side]
            ]
    def update_params(self):
        self.paramWay[0][1] = self.rail_q_interface('top') + self.rail_q_interface('bottom')
        self.paramWay[1][1] = self.rail_q_interface('top') + self.rail_q_interface('bottom')
        self.paramWay[2][1] = self.rail_q_interface('left') + self.rail_q_interface('right')
        self.paramWay[3][1] = self.rail_q_interface('left') + self.rail_q_interface('right')

        self.paramWay[4][1] = self.rail_q_interface('top_right') + self.rail_q_interface('right_top')
        self.paramWay[5][1] = self.rail_q_interface('right_bottom') + self.rail_q_interface('bottom_right')
        self.paramWay[6][1] = self.rail_q_interface('bottom_left') + self.rail_q_interface('left_bottom')
        self.paramWay[7][1] = self.rail_q_interface('left_top') + self.rail_q_interface('top_left')

        self.paramWay[8][1] = self.rail_q_interface('left_top') + self.rail_q_interface('top_left')
        self.paramWay[9][1] = self.rail_q_interface('bottom_left') + self.rail_q_interface('left_bottom')
        self.paramWay[10][1] = self.rail_q_interface('right_bottom') + self.rail_q_interface('bottom_right')
        self.paramWay[11][1] = self.rail_q_interface('top_right') + self.rail_q_interface('right_top')

        print(self.paramWay)
if __name__ == "__main__":

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )
    for_mouse = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )


    n = []
    for x in range(60, WINDOW_WIDTH-30, 60):
        for y in range(60, WINDOW_HEIGHT-30, 60):  
             n.append(
                 Cross(cnv, x, y,
              randint(0,1), randint(0,1), randint(0,1), randint(0,1),
              randint(0,1), randint(0,1), randint(0,1), randint(0,1), 
              randint(0,1), randint(0,1), randint(0,1), randint(0,1)
                       )
                    )
             n[-1].draw()
             if len(n) % 2 == 0:
                 n[-1].destroy()    

    #cv2.ellipse(cnv, (330,330), (30,30), 0,  0, -90, (0, 0,255), 4)
    #cv2.ellipse(cnv, (330,330), (30,30), 0,  225, 270, (250, 200,30), 4)

    
    cv2.namedWindow('TRAINS')
    #cv2.setMouseCallback('TRAINS', set_cross)
    #cv2.setMouseCallback('TRAINS', d.set_cross)
    while True:
        cv2.imshow('TRAINS', cnv)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()

