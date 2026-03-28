## this code is atleast 20-30% made by CHATGPT - the rest is by me
# it detects multipule objects at once compared to the previous version where it could only detect one bolb object

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


group = []
visited = []

cam = Picamera2()
getArrayDim = False
lastFrame = []
cam.start()

while True:
    seed_found = False
    pixel_changed = False
    now = time.time()
    img = cam.capture_array()
    img = cv2.resize(img,(320,240))

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    
    frame = gray
    
    length = len(frame)
    width = len(frame[0])
    
    #CHATGPT 
    visited = [[False for _ in range(width)] for _ in range(length)]
    
    if cv2.waitKey(1) == 27:
        break

    # Get lastFrame Dimensions from original frame
    if not getArrayDim:
        lastFrame = frame * 0
        getArrayDim = True

    threshold = 22
    different = 0

    if not seed_found:    
        for y in range(length):
            for x in range(width):
                if not visited[y][x] and abs(int(lastFrame[y][x]) - int(frame[y][x])) > threshold:                    
                    
                    min_x = max_x = x
                    min_y = max_y = y 
                    
                    group = [[y,x]]
                    visited[y][x] = True

                    i = 0

                    while i < len(group):
                        gy = group[i][0]
                        gx = group[i][1]
                    
                        #check left neighbor
                        if gx >= 1 and not visited[gy][gx-1]:
                            visited[gy][gx-1] = True
                            if abs(int(lastFrame[gy][gx-1]) - int(frame[gy][gx-1])) > threshold:
                                group.append([gy, gx-1])
                                different+=1
                                
                        #check right neigbor            
                        if gx + 1 < width and not visited[gy][gx+1]:
                            visited[gy][gx+1] = True
                            if abs(int(lastFrame[gy][gx+1]) - int(frame[gy][gx+1])) > threshold:
                                group.append([gy,gx+1])
                                different+=1
                                
                        #check top neighbor
                        if gy >= 1  and not visited[gy-1][gx]:
                            visited[gy-1][gx] = True
                            if abs(int(lastFrame[gy - 1][gx]) - int(frame[gy - 1][gx])) > threshold:
                                group.append([gy-1,gx])
                                different+=1
                        #check bottom neighbor
                        if gy + 1 < length and not visited[gy+1][gx]:
                            visited[gy+1][gx] = True
                            if abs(int(lastFrame[gy+1][gx]) - int(frame[gy+1][gx])) > threshold:
                                group.append([gy+1,gx])
                                different+=1
                        #check top-left
                        if gx >= 1 and gy >= 1 and not visited[gy-1][gx-1]:
                            visited[gy-1][gx-1] = True
                            if abs(int(lastFrame[gy-1][gx-1]) - int(frame[gy-1][gx-1])) > threshold:
                                group.append([gy-1,gx-1])
                                different+=1
                        #check bottom-left
                        if gx >= 1 and gy+1 < length and not visited[gy+1][gx-1]:
                            visited[gy+1][gx-1] = True
                            if abs(int(lastFrame[gy+1][gx-1]) - int(frame[gy+1][gx-1])) > threshold:
                                group.append([gy+1,gx-1])
                                different+=1
                        #check bottom-right
                        if gx + 1 < width and gy + 1 < length and not visited[gy+1][gx+1]:
                            visited[gy+1][gx+1] = True
                            if abs(int(lastFrame[gy+1][gx+1]) - int(frame[gy+1][gx+1])) > threshold:
                                group.append([gy+1,gx+1])
                                different+=1
                                
                        #check top-right
                        if gy >=1 and gx + 1 < width and not visited[gy-1][gx+1]:
                            visited[gy-1][gx+1] = True
                            if abs(int(lastFrame[gy-1][gx+1]) - int(frame[gy-1][gx+1])) > threshold:
                                group.append([gy-1,gx+1])

                                different+=1
                                
                        #update min_x max_y max_x min_y
                        if gx < min_x:
                            min_x = gx
                        if gy < min_y:
                            min_y = gy
                        if gx > max_x:
                            max_x = gx
                        if gy > max_y:
                            max_y = gy
                        i+=1
                        pixel_changed = True

                    if len(group) > 15:
                        cv2.rectangle(img,(min_x,min_y),(max_x,max_y),(0,255,0),2)


        print("Amount of difference detected:", different)
        # Updates the lastframe threshold value to the name frame threshold values
    lastFrame[:] = frame
    group = []
    cv2.imshow("video2", img)
