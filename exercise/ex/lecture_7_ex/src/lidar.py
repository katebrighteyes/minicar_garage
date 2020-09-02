#!/usr/bin/env python

import rospy, time
from sensor_msgs.msg import LaserScan

#TODO 1

def callback(data):
  #TODO 2

rospy.init_node('Node_Name')
rospy.Subscriber("/scan", LaserScan, callback, queue_size = 1)

time.sleep(3) 

while not rospy.is_shutdown():
  #TODO 3
  
  time.sleep(0.01)
