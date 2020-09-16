cd ~/catkin_ws/src

catkin_create_pkg lecture_7_ex std_msgs rospy

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

----------------------
======================
yolo_ros

1. launch 파일
  <node pkg="yolo_ros" type="yolo_steering.py" name="yolo_xycar" output="screen" />
  
2. python 파일의 TODO
#TODO 1
    rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, callback)
#TDDO 2
        for i in range(len(boxes.bounding_boxes)):
            if boxes.bounding_boxes[i].Class == "person":
                nobody = False

        if nobody:
            drive(0, 1)
	    else:
		    drive(0,0)
	    print "stop"

  

