#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def my_callback(event):
    print "6 seconds passed!"
    rospy.signal_shutdown("Just stopping the robot")

rospy.init_node('robot_talker', anonymous=False)
rate=rospy.Rate(2)
rospy.Timer(rospy.Duration(10), my_callback)

pub = rospy.Publisher('/simple_model/sup_to_nav_position_controller/command', Float64, queue_size=10)

while not rospy.is_shutdown():
    position= 0.0
    rospy.loginfo(position) #printa il numero nella shell
    pub.publish(position) #pubblica nel topic
    rate.sleep()
