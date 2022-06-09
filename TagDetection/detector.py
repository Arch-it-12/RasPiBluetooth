import sys

import cv2
import imutils
from imutils.video import VideoStream

STREAM = VideoStream(src=0).start()
ARUCO_DICT = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
ARUCO_PARAMS = cv2.aruco.DetectorParameters_create()

while True:
    frame = STREAM.read()
    frame = imutils.resize(frame, width=1000)

    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, ARUCO_DICT, parameters=ARUCO_PARAMS)

    if len(corners) >= 1:
        for c, marker_id in zip(corners, ids):
            (ptA, ptB, ptC, ptD) = c.reshape((4, 2))

            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))

            # draw the bounding box of the AprilTag detection
            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

            cv2.line(frame, (abs(int((ptA[0] + ptB[0]) / 2)), abs(int((ptA[1] + ptB[1]) / 2))),
                     (abs(int((ptC[0] + ptD[0]) / 2)), abs(int((ptC[1] + ptD[1]) / 2))),
                     (0, 255, 0), 2)

            cv2.line(frame, (abs(int((ptA[0] + ptD[0]) / 2)), abs(int((ptA[1] + ptD[1]) / 2))),
                     (abs(int((ptB[0] + ptC[0]) / 2)), abs(int((ptB[1] + ptC[1]) / 2))),
                     (0, 255, 0), 2)

            cv2.putText(frame, str(marker_id), (ptA[0], ptD[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Camera Feed", frame)
    x = cv2.waitKey(1)

    if x == ord("q"):
        sys.exit()
