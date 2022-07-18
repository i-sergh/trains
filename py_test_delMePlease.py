print("я основной файлБ меня зовут", __name__)
import cv2
import numpy as np
import way_creator

print("а это мой друг, я говорю, что ему делать. Его зовут ",
      way_creator.__name__)


def dotsDestroy(event, x, y, flags, param):
    global d
    
    for i in range(len(d)):
        d[i].set_cross(event, x, y, flags, param)

if __name__ == '__main__':
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )
    for_mouse = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
                   dtype=np.uint8() )



    cv2.namedWindow('TRAINS')
    cv2.setMouseCallback( 'TRAINS',  dotsDestroy )
    #cv2.moveWindow('TRAINS', -16,-31) 
    global d
    d = [] 
    for x in range(60, WINDOW_WIDTH-30, 60 ):
        for y in range(60, WINDOW_HEIGHT-30, 60 ):
            d.append( way_creator.Dot(cnv,x, y) )
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
