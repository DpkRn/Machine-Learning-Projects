import cv2
import numpy as np

def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Display coordinates on image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f'{x}, {y}', (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow('original', img)


img=cv2.imread("z1.png")
img=img[:,400:]
img=cv2.resize(img,(1000,800))
cv2.imshow('original',img)

#getting manually pixel corner points by mouse click
input_points=np.float32([[174,88],[612,22],[248,776],[684,706]])

#setting output size of A4
width=400;
height=int(width*1.414)

#desired pixel cordinates of output image
converted_points=np.float32([[0,0],[width,0],[0,height],[width,height]]);
#perspective transformation
matrix=cv2.getPerspectiveTransform(input_points,converted_points);
img_output=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Image',img_output)

cv2.setMouseCallback('original',click_event)

cv2.waitKey(0)
