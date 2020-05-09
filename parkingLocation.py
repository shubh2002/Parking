import cv2
import numpy as np 

points = []
spot_dict = {}
title = 'Frame'
i = 0
current_frame = None

def get_frame(events, x, y, flags, param):
    global current_frame, points, i
    if events == cv2.EVENT_LBUTTONDOWN:
        print(f'{x},{y}')
        points.append([x,y])
        if len(points) == 2:
            spot_dict['spot_id :'+ str(i)] = points
            points = []
            i += 1

def get_points(frame):
    current_frame = frame.copy()
    cv2.imshow(title, current_frame)
    cv2.setMouseCallback(title, get_frame)
    cv2.waitKey(0)
    cv2.destroyWindow(title)
    return spot_dict
