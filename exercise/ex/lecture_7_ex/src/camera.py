#!/usr/bin/env python

import cv2, rospy, time
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

#TODO 1 


def img_callback(img_data):
  #TODO 2


#TODO 3


time.sleep(1.5)

while not rospy.is_shutdown():
  #TODO 4


  if cv2.waitKey(1) & 0Xff == ord('q'):
    break

cv2.destroyAllWindows()
