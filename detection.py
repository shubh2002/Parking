import cv2
import numpy as np 
import writeCSV
from writeCSV import write_csv

font = cv2.FONT_HERSHEY_SIMPLEX
class_dictionary = {}
class_dictionary[0] = 'Empty'
class_dictionary[1] = 'Occupied'
i=0


def make_prediction(img):
    img = img/255.
    img = np.expands_dims(img, axis=0)
    class_predict = model.predict(img)
    inID = np.argmax(class_predict[0])
    label = class_dictionary[inID]
    return label


def predict_on_image(image, spot_dict, make_copy = True, alpha=0.5, save=True, color=[0,255,0]):
    all_spot = len(spot_dict.keys())
    empty_spot = 0
    if make_copy:
        new_image = np.copy(image)
        overlay = np.copy(image)

    for spot in spot_dict.values():
        (x1, y1, x2, y2) = spot
        (x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
        spot_img = image[y1:y2, x1:x2]
        spot_img = cv2.resize(spot_img, (52, 52))
        label = make_prediction(spot_img)

        if label == 'Empty':
            empty_spot +=1
            cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
        
        cv2.addWeighted(overlay, alpha, new_image, 1-alpha, 0, new_image)

        cv2.putText(new_image, "Available: %d spots" %empty_spot, (30, 95),font, 0.7, (255,255,255), 2)

        if save:
            filename = 'with_marking'+str(i)+'.jpg'
            cv2.imwrite(filename, new_image)
            write_csv(empty_spot, True )
            i+=1

        return new_image


    
