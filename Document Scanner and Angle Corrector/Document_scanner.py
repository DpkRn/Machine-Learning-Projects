import cv2
import numpy as np
import mapper

def biggest_contours(contours):
    biggest=np.array([])
    max_area=0
    for i in contours:
        area=cv2.contourArea(i)
        if(area>1000):
            peri=cv2.arcLength(i,True)
            approx=cv2.approxPolyDP(i,0.1*peri,True)
            print(len(approx))
            if area>max_area and len(approx)==4:
                print(len(approx))
                biggest=approx
                max_area=area

    return biggest

img=cv2.imread('z1.png')
# img=img[:,700:-700]
img=cv2.resize(img,(1300,800))
img_original=img.copy()

#getting Edges by bluring
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray,20,30,30)
edges=cv2.Canny(gray,10,20)

#Contours detection
contours,hierarchy=cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[:10]
contours=sorted(contours,key=cv2.contourArea,reverse=True)[:1]

biggest=biggest_contours(contours)
cv2.drawContours(img,[biggest],-1,(0,255,0),3)
biggest = mapper.mapp(biggest)  # find endpoints of the sheet

width=800;
height=int(width*1.141)

pts = np.float32([[0, 0], [width, 0], [width, height], [0, height]])  # map to 800*800 target window
op = cv2.getPerspectiveTransform(biggest, pts)  # get the top or bird eye view effect
dst = cv2.warpPerspective(img, op, (width,height))
cv2.imshow('Edges',edges)
cv2.imshow('dest',img)
cv2.imshow('gray',gray)
cv2.imshow("Scanned", dst)


# for i in contours:
#     cv2.drawContours(img,[i],-1,(0,255,0),1)
#
# cv2.imshow('original',img)
# cv2.imshow('bilaterialFilter',gray)
# cv2.imshow('edges',edges)


# print(img.shape)
# print(gray.shape)
# print(edges.shape)

#to show in one stack we need same shape so do it in same shape
# gray=np.stack((gray,)*3,axis=-1)
# edges=np.stack((edges,)*3,axis=-1)

# print(img.shape)
# print(gray.shape)
# print(edges.shape)

#now we can stack this
# img_hor=np.hstack((img_original,gray,edges,img))
# cv2.imshow('stack',img_hor)





cv2.waitKey(0)