#!/usr/bin/env python

import rospy, time
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue

imu_data = None

def callback(data):
  #TODO 1

#TODO 2 

time.sleep(15)

while not rospy.is_shutdown():
  #TODO 3

  print("Roll : {}, Pitch : {}, Yaw : {}".format(roll, pitch, yaw))
  time.sleep(1)
