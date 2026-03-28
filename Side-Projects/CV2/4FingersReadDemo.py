import numpy as np
from picamera2 import Picamera2
import cv2
import time
last = 0
# np.set_printoptions(threshold=np.inf)

# array_hand = [] 
# array_handwidth = []

# for line in open("hand.txt"):
#     row = []
#     for c in line.strip():
#         row.append(int(c))
#     array_hand.append(row)    
# array_hand = np.array(array_hand)

yarray = []
xarray = []
y = 0

cam = Picamera2()
cam.start()
fingerWidth = 0
fingerCount = 0
gap = 0
while True:
    
    img = cam.capture_array()
    img = cv2.resize(img, (320, 240))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    now = time.time()
    if now - last >= 0:
        frame_array = (thresh == 255).astype(int) # convert to 1/0
        print("hand not found")
        
        last = now
        
    for row in frame_array:                 
        fingerWidth = 0

        for i in range(len(row) - 1):
            if row[i] == 0:
                fingerWidth += 1
                
                # if the next column is not Finger or an Object
                if row[i + 1] == 1:
                    if 8 < fingerWidth < 35:
                        gap = 0
                        j = i + 1
                        while j < len(row) and row[j] == 1:
                            gap += 1
                            j+=1

                        if gap < 35:
                            xarray.append(int(i))
                            yarray.append(y +1)
                            fingerCount+=1
                    
                    fingerWidth = 0

        if fingerCount == 4:
            print("hand found")
        fingerCount = 0
        fingerWidth = 0
        y+=1
  #  cv2.imshow("threshold", thresh)

    for k in range(len(xarray)):
        cv2.circle(img, (xarray[k], yarray[k]), 2, (0,255,0), -1)

    cv2.imshow("video", img)

    xarray = []
    yarray = []
    y = 0
    if cv2.waitKey(1) == 27: # aka if Press ESC button
        break
cam.stop()
cv2.destroyAllWindows()
