#!/usr/bin/env python

import cv2, time
import rospy, rospkg
import numpy as np

from ackermann_msgs.msg import AckermannDriveStamped

ack_publisher = None

cv_image = np.empty(shape=[0])

# TODO 1 drive function

video_path = str(rospkg.RosPack().get_path('drive_ex')) + "/video/1.avi"
cap = cv2.VideoCapture(video_path)

rospy.init_node('go_video')

# TODO 2 ack_publisher

brightness = 60

width = 640
height = 480

rec_width = 20
rec_height = 10

rpos_offset = 320

line_height_offset = 15 
thresh_line_pixel_cnt = 150

r_center = 0
x_location = None

while not rospy.is_shutdown():
  ret, cv_image = cap.read()

  if cv2.waitKey(1) & 0Xff == 27:
    break

  if not ret:
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    continue

# TODO 3 opencv2 process part

  if x_location == None:
    r_center = rpos

  x_location = (r_center - rpos)
  x_location = (x_location/3) * (0.017)
    
  detect_area = hsv_line[2:15,120:520]
  cntzero = cv2.countNonZero(detect_area)

  if cntzero > 2400:
    drive(0,0)
    time.sleep(3)

  drive(x_location, 0.5)

  cv2.imshow("origin", cv_image)
  cv2.imshow("view", view)

  time.sleep(0.01)

cv2.destroyAllWindows()
