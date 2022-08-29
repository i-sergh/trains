import cv2
import numpy as np


class Train:
    def __init__ (self, x, y, dot):

        # центр нашего поезда 
        self.x = x
        self.y = y

        self.width = 20
        self.height = 10

        self.grad = 0
            
        self.color =(100, 240, 50)

        self.my_dot = dot 
        
    def draw(self, cnv):
        # получили список точек
        box = cv2.boxPoints(
                    ( (self.y, self.x), (self.width, self.height), self.grad)
            )
        # округлили
        box = np.int0(box)
        # отрисовали
        cv2.drawContours(cnv, [box],0, self.color, -1 )
        
    def destroy(self, cnv):
        # получили список точек
        box = cv2.boxPoints(
                    ( (self.y, self.x), (self.width, self.height), self.grad)
            )
        # округлили
        box = np.int0(box)
        # отрисовали
        cv2.drawContours(cnv, [box],0, (0,0,0), -1 )

    def move(self, cnv, dx, dy):
        self.destroy(cnv)

        self.x += dx
        self.y += dy
        
        self.draw(cnv)
        
    def rotate(self):
        pass

    

if __name__ == "__main__":
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )


    
    tr = Train(10,10)

    
    
    while True:
        
        tr.destroy(cnv)        
        
        tr.grad+=1

        tr.draw(cnv)
        
        cv2.imshow('privrt', cnv)

        key = cv2.waitKey(1)
        if key == 27: # ESC
            break

        
        if key == ord('w'): #вперед
            tr.move(cnv, -2, 0)
            
        if key == ord('s'): # назазд
            tr.move(cnv, 2, 0)
        if key == ord('a'): # влево
            tr.move(cnv, 0, -2)
        if key == ord('d'): # вправо
            tr.move(cnv, 0, 2)
    cv2.destroyAllWindows()
