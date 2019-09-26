#!/usr/bin/env python

import cv2, rospy, time
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

# TODO

while not rospy.is_shutdown():
  cv2.imshow('original', cv_image)

  if cv2.waitKey(1) & 0Xff == ord('q'):
    break

cv2.destroyAllWindows()
