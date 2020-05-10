import cv2
import parkingLocation
import detection
from detection import predict_on_image

cap = cv2.VideoCapture('testVideo.mp4')
count = 0
_, frame = cap.read()
spots = parkingLocation.get_points(frame)
# print('spots are : ', spots)

while (cap.isOpened()):

    _, frame = cap.read()
    count+=1
    if count == 50:
        count = 0
        detected_image = predict_on_image(frame, spots)
        cv2.imshow('detected_image', detected_image)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        continue

cap.release()
cv2.destroyAllWindows()