< camera.py >

#TODO 1 
bridge = CvBridge()

#TODO 2
  global bridge
  global cv_image
  cv_image = bridge.imgmsg_to_cv2(img_data, "bgr8")

#TODO 3
rospy.init_node('Camera_receive_node')
rospy.Subscriber("/usb_cam/image_raw/", Image, img_callback)

  #TODO 4
  cv2.imshow('original', cv_image)
----------------------
< IMU.py > 
  #TODO 1
  global imu_data
  imu_data = data.status[0].values

#TODO 2 
rospy.init_node('IMU_receive_node')
rospy.Subscriber("/diagnostics", DiagnosticArray, callback, queue_size = 1)

  #TODO 3
  roll = imu_data[0].value
  pitch = imu_data[1].value
  yaw = imu_data[2].value
----------------------------
< lidar.py > 

#TODO 1
ranges_list = []

  #TODO 2
  global ranges_list
  ranges_list = data.ranges

  #TODO 3
  if ranges_list[89] <= 1:
    rospy.loginfo("WARNING !!! distance : {}".format(ranges_list[89]))

