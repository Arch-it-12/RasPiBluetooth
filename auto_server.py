import sys

import cv2
import imutils
import picamera
from imutils.video import VideoStream

from methods import pyth, points, midpoint, center
from motor_server import ultrasonic, left, right, up, down, forward, no_movement, bot_off

# ArUco Constants
# STREAM = VideoStream(src=1).start()
ARUCO_DICT = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
ARUCO_PARAMS = cv2.aruco.DetectorParameters_create()

TARGET_TAG = 423
TARGET_PX_DISTANCE = 655

frame = None
picamera.capture(frame, format="png")
frame = imutils.resize(frame, width=1000)
FRAME_CENTER = (int(frame.shape[1] / 2), int(frame.shape[0] / 2))

flag = True
is_turning = False

while flag:
    frame = None
    picamera.capture(frame, format="png")
    frame = imutils.resize(frame, width=1000)

    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, ARUCO_DICT, parameters=ARUCO_PARAMS)

    cv2.rectangle(frame, (FRAME_CENTER[0] - 150, FRAME_CENTER[1] + 150), (FRAME_CENTER[0] + 150, FRAME_CENTER[1] - 150),
                  (255, 0, 0), 2)
    cv2.aruco.drawDetectedMarkers(frame, corners, borderColor=(255, 255, 0))

    cv2.circle(frame, FRAME_CENTER, 3, (255, 0, 0), -1)

    if len(corners) >= 1:
        for c, marker_id in zip(corners, ids):
            ptA, ptB, ptC, ptD = points(c)
            mp = midpoint(ptA, ptC)

            cv2.circle(frame, center(ptA, ptC, ptB, ptD), 3, (0, 255, 0), -1)  # Center of tag
            cv2.circle(frame, ptA, 3, (0, 0, 255), -1)  # Top left corner of tag

            if marker_id != TARGET_TAG:
                continue

            in_range = mp[0] in range(FRAME_CENTER[0] - 150, FRAME_CENTER[0] + 151) and mp[1] in range(
                FRAME_CENTER[1] - 150,
                FRAME_CENTER[1] + 159)

            if mp[0] in range(FRAME_CENTER[0] - 15, FRAME_CENTER[0] + 16) and mp[1] in range(FRAME_CENTER[1] - 15,
                                                                                             FRAME_CENTER[1] + 16):
                is_turning = False
                ultrasonic.threshold = ultrasonic.distance
                ultrasonic.when_in_range = up
                ultrasonic.when_out_of_range = bot_off

            if in_range and not is_turning:
                print("forward")
                forward()
            elif not in_range or is_turning:
                is_turning = True
                ultrasonic.when_in_range = None
                ultrasonic.when_out_of_range = None

                if mp[0] >= FRAME_CENTER[0] + 15:
                    print("right")
                    right()
                elif mp[0] <= FRAME_CENTER[0] - 15:
                    print("left")
                    left()

                if mp[1] >= FRAME_CENTER[1] + 15:
                    print("down")
                    down()
                elif mp[1] <= FRAME_CENTER[1] - 15:
                    print("up")
                    up()

            if max(pyth(ptA, ptB), pyth(ptB, ptC), pyth(ptC, ptD), pyth(ptD, ptA)) > TARGET_PX_DISTANCE:
                print("arrived")
                no_movement()

                ultrasonic.threshold = ultrasonic.distance
                ultrasonic.when_in_range = up
                ultrasonic.when_out_of_range = bot_off

                flag = False
                break

    cv2.imshow("Camera Feed", frame)
    x = cv2.waitKey(1)

    if x == ord("q"):
        sys.exit()
