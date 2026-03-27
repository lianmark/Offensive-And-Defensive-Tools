from picamera2 import Picamera2
import cv2
import numpy as np 
import time

last = time.time()

min_x = None
max_x = None
min_y = None
max_y = None

pixel_changed = False

cam = Picamera2()
getArrayDim = False
lastFrame = []
cam.start()

while True:
    pixel_changed = False
    now = time.time()
    img = cam.capture_array()
    img = cv2.resize(img,(555,555))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("video", gray)
    frame = gray
    
    if cv2.waitKey(1) == 27:
        break
    
    # Get lastFrame Dimensions from original frame
    if not getArrayDim:
        lastFrame = frame * 0
        getArrayDim = True
    
    threshold = 15
    different = 0 
    
    # will only change pixel inn range of 15 which means every 15 pixels
    for y in range(0, len(frame), 15):
        # will only change pixel inn range of 15 which means every 15 pixels
        for x in range(0, len(frame[y]), 15):
                # if the threshold substraction of a pixel[x][y] from lastFrame - frame is greater than threshold variable = execute 
                if abs(int(lastFrame[y][x]) - int(frame[y][x])) > threshold:
                    if not pixel_changed:
                        min_x = x
                        max_x = x
                        min_y = y
                        max_y = y
                        pixel_changed = True
                    
                    if x < min_x: 
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y < min_y: 
                        min_y = y
                    if y > max_y:
                        max_y = y
                    different +=1
    if pixel_changed:
        if now - last > 0.1:               
            cv2.rectangle(img,(min_x,min_y), (max_x,max_y), (0,255,0), 2)
            last = now
    
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    print("Amount of difference detected:", different)
    # Updates the lastframe threshold value to the name frame threshold values
    lastFrame[:] = frame
    
    cv2.imshow("video2", img)
