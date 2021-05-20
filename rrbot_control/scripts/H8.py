#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)
rospy.init_node('robot_talker', anonymous=False)
pub_3 = rospy.Publisher('/simple_model/sup_to_nav_position_controller/command', Float64, queue_size=10)
rospy.init_node('robot_talker', anonymous=False)

def my_callback(event):
    print "6 seconds passed!"
    rospy.signal_shutdown("Just stopping the robot")

rospy.init_node('robot_talker', anonymous=False)
rate=rospy.Rate(2)
rospy.Timer(rospy.Duration(6), my_callback)



while not rospy.is_shutdown():
    position= -1.0
    rospy.loginfo(position) #printa il numero nella shell
    pub_1.publish(position+2) #pubblica nel topic
    pub_2.publish(position+2)
    pub_3.publish(position-0.5)
    rate.sleep()



