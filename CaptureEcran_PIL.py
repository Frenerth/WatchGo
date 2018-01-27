import numpy as np
from PIL import ImageGrab
import cv2
import time

def capture_ecran(): 
    dernier_temps = time.time()
    while(True):
        # 1280*720 mode
        screenshot =  np.array(ImageGrab.grab(bbox=(0,40,1280,760)))
        print(f'{time.time()-dernier_temps} seconds - FPS = {1/(time.time()-dernier_temps)}')
        dernier_temps = time.time()
        cv2.imshow('window',cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
