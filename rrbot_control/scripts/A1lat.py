#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)
rospy.init_node('robot_talker', anonymous=False)

def my_callback(event):
    print "6 seconds passed!"
    rospy.signal_shutdown("Just stopping the robot")

rospy.init_node('robot_talker', anonymous=False)
rate=rospy.Rate(2)
rospy.Timer(rospy.Duration(10), my_callback)



while not rospy.is_shutdown():
    position= -0.68
    rospy.loginfo(position) #printa il numero nella shell
    pub_1.publish(position) #pubblica nel topic
    pub_2.publish(position)
    rate.sleep()



