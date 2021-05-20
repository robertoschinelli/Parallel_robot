#!/usr/bin/env python
import rospy
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64


rospy.init_node('listenernode')

pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

rate=rospy.Rate(2)

num = -0.7

def callback(msg):
    
    global num    
    num = msg.process_value
 
rospy.Subscriber("/simple_model/bridge_to_platform_position_controller/state", JointControllerState, callback)


num_2 = -0.7

def callback_2(msg):
    
    global num_2    
    num_2 = msg.process_value
 
rospy.Subscriber("/simple_model/up_to_shuttle_position_controller/state", JointControllerState, callback_2)



while (abs(num - 0.0875) < -0.001 or abs(num - 0.0875) > 0.001) or (abs(num_2 - 0.0875) < -0.001 or abs(num_2 - 0.0875) > 0.001):  
    print num
    print num_2
    position= -0.0875
    rospy.loginfo(position) 
    pub_1.publish(position+0.175) 
    pub_2.publish(position+0.175)
    rate.sleep()
