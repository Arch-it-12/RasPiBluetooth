import sys

import cv2
import imutils
from imutils.video import VideoStream

from methods import pyth, points, midpoint, center

# ArUco Constants
STREAM = VideoStream(src=0).start()
ARUCO_DICT = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
ARUCO_PARAMS = cv2.aruco.DetectorParameters_create()

# Distance Constants
ACTUAL_LENGTH = 10.5  # Actual length of the side of the april tag (cm)
TEST_DISTANCE = 100  # Distance from which the measurement was taken (cm)
PIXEL_LENGTH_INBUILT = 85
PIXEL_LENGTH_EXTERNAL = 113  # Length of the side in pixels at TEST_DISTANCE cm away (px)

FOCAL_LENGTH = (PIXEL_LENGTH_INBUILT * TEST_DISTANCE) / ACTUAL_LENGTH
FW = ACTUAL_LENGTH * FOCAL_LENGTH

while True:
    frame = STREAM.read()
    frame = imutils.resize(frame, width=1000)

    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, ARUCO_DICT, parameters=ARUCO_PARAMS)

    midY = int(frame.shape[0] / 2)
    midX = int(frame.shape[1] / 2)

    cv2.rectangle(frame, (midX - 200, midY + 200), (midX + 200, midY - 200), (255, 0, 0), 2)
    cv2.circle(frame, (midX, midY), 2, (255, 0, 0), -1)

    if len(corners) >= 1:
        for c, marker_id in zip(corners, ids):
            ptA, ptB, ptC, ptD = points(c)
            mp = midpoint(ptA, ptC)

            side_length = max(pyth(ptA, ptB), pyth(ptB, ptC), pyth(ptC, ptD), pyth(ptD, ptA))
            measured_distance_cm = FW / side_length

            # draw the bounding box of the AprilTag detection
            cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
            cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
            cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
            cv2.line(frame, ptD, ptA, (0, 255, 0), 2)
            cv2.circle(frame, center(ptA, ptC, ptB, ptD), 2, (0, 255, 0), 2)

            cv2.putText(frame, str(marker_id), (ptA[0], ptD[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(frame, "%.2fm" % (measured_distance_cm / 100), (ptB[0], ptC[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)

    cv2.imshow("Camera Feed", frame)
    x = cv2.waitKey(1)

    if x == ord("q"):
        sys.exit()
