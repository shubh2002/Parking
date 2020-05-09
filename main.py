import cv2
import parkingLocation

cap = cv2.VideoCapture('testVideo.mp4')

_, frame = cap.read()
spots = parkingLocation.get_points(frame)
print('spots are : ', spots)

while (cap.isOpened()):

    _, frame = cap.read()
    for points in spots.values():

        (x, y, w, h) = (points[0][0], points[0][1], points[1][0], points[1][1])
        print(x,y,w,h)
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)

    cv2.imshow('rectangle', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()