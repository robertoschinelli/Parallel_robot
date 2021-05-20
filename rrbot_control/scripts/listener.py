#!/usr/bin/env python
import rospy
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64


#def callback(msg):
    #print msg.process_value
    
#rospy.init_node('listenernode')
#numero = rospy.Subscriber("/simple_model/bridge_to_platform_position_controller/state", JointControllerState, callback)

#rospy.spin()


#pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
#pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)
#rospy.init_node('robot_talker', anonymous=False)

#def my_callback(event):
    #print "6 seconds passed!"
    #rospy.signal_shutdown("Just stopping the robot")

#rospy.init_node('robot_talker', anonymous=False)
#rate=rospy.Rate(2)
#rospy.Timer(rospy.Duration(6), my_callback)


#while not rospy.is_shutdown(): #msg.process_value < 0.5:
    #position= -1.0
    #rospy.loginfo(position) #printa il numero nella shell
    #pub_1.publish(position) #pubblica nel topic
    #pub_2.publish(position)
    #rate.sleep()



rospy.init_node('listenernode')

pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)
#rospy.init_node('robot_talker', anonymous=False)

#def my_callback(event):
    #print "6 seconds passed!"
    #rospy.signal_shutdown("Just stopping the robot")

#rospy.init_node('robot_talker', anonymous=False
rate=rospy.Rate(2)
#rospy.Timer(rospy.Duration(6), my_callback)

num = 0.6

def callback(msg):
    

    global num    
    num = msg.process_value
    #num.process_value = msg.process_value
    #print msg.process_value
    #num=msg.process_value
    #msg.process_value = goal_pose
    
rospy.Subscriber("/simple_model/bridge_to_platform_position_controller/state", JointControllerState, callback)
#print msg.process_value
#rospy.spin()

#print num

while not num < -0.499: #num > 0: #rospy.is_shutdown(): #num.value < 0.5: 
    print num
    position= -0.5
    rospy.loginfo(position) #printa il numero nella shell
    pub_1.publish(position) #pubblica nel topic
    pub_2.publish(position)
    rate.sleep()
