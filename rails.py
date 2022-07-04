import cv2
import numpy as np
from random import randint, choice

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
               dtype=np.uint8() )


class Cross:
    def __init__(self, x, y, top, bottom, left, right,
                 top_right, right_bottom, bottom_left,  left_top,
                 top_left,  left_bottom,  bottom_right, right_top):
        '''
            x & y - center of the cross
        '''
        self.x = x
        self.y = y
        
        self.step = 30

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
                           [False, True],
                           [False, True],

                           [False, False],
                           [False, False],
                           [False, False],
                           [False, True]
                           
                        ]
    def draw(self):
        for i, zn in enumerate(self.nlist):
            if self.paramWay[i][1]:
                if self.paramWay[i][0]:
                    if zn:
                    
                        cv2.line(cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (250, 200,30), 4 )
                    else:
                        cv2.line(cnv, self.drawDots[i][0], self.drawDots[i][1],
                             (0, 0,255), 4 )
                else:
                    if zn:
                    
                        cv2.ellipse(cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (250, 200,30), 4 )
                    else:
                        cv2.ellipse(cnv, self.drawDots[i][0], (30,30), 0,
                                    self.drawDots[i][1], self.drawDots[i][2],
                                    (0, 0,255), 4 )
                
n = Cross(300, 300,
          False, True, False, True,
          True, True, True, True, 
          False, False, False, False)
n.draw()
#cv2.ellipse(cnv, (330,330), (30,30), 0,  0, -90, (0, 0,255), 4)
#cv2.ellipse(cnv, (330,330), (30,30), 0,  225, 270, (250, 200,30), 4)
while True:
    cv2.imshow('TRAINS', cnv)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
