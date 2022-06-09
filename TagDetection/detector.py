import cv2
import imutils

image = cv2.imread("image.png")
image = imutils.resize(image, width=600)

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,
                                                   parameters=arucoParams)
(ptA, ptB, ptC, ptD) = corners[0][0]
ptB = (int(ptB[0]), int(ptB[1]))
ptC = (int(ptC[0]), int(ptC[1]))
ptD = (int(ptD[0]), int(ptD[1]))
ptA = (int(ptA[0]), int(ptA[1]))

# draw the bounding box of the AprilTag detection
cv2.line(image, ptA, ptB, (0, 255, 0), 2)
cv2.line(image, ptB, ptC, (0, 255, 0), 2)
cv2.line(image, ptC, ptD, (0, 255, 0), 2)
cv2.line(image, ptD, ptA, (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
