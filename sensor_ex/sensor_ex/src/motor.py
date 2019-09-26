#!/usr/bin/env python

import rospy,time
from ackermann_msgs.msg import AckermannDriveStamped

ack_publisher = None

# TODO

while not rospy.is_shutdown():
  for straight_cnt in range(100): 
    drive(0,1)
    time.sleep(0.1)

  for left in range(100):
    drive(0.34,1)
    time.sleep(0.1)

  for right in range(100):
    drive(-0.34,1)
    time.sleep(0.1)

