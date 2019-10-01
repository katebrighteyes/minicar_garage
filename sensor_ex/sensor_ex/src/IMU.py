#!/usr/bin/env python

import rospy, time
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue

imu_data = None

#TODO



time.sleep(15)

while not rospy.is_shutdown():
  roll = imu_data[0].value
  pitch = imu_data[1].value
  yaw = imu_data[2].value

  print("Roll : {}, Pitch : {}, Yaw : {}".format(roll, pitch, yaw))
  time.sleep(1)
