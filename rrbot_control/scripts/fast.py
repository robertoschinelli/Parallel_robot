#!/usr/bin/env python
# license removed for brevity
import rospy
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64

var = raw_input("enter coordinates: ")
print "you entered", var

letter = float(ord(var[0].upper())-69)
number = float(var[1]) - 5


if (letter < 0):
    letter = (letter/4)/1.4285714285714+0.175/2
    #print letter
elif (letter >= 0):
    letter = ((letter + 1)/4)/1.4285714285714-0.175/2
    #print letter

if (number < 0):
    number = (number/4)/1.4285714285714+0.175/2
    #print number
elif (number >= 0):
    number = ((number + 1)/4)/1.4285714285714-0.175/2
    #print number

#defining node and publisher
rospy.init_node('listenernode')
pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)
#frequency
rate=rospy.Rate(2)

num = 0.7
def callback(msg):
    global num
    num = msg.process_value
rospy.Subscriber("/simple_model/bridge_to_platform_position_controller/state", JointControllerState, callback)


num_2 = 0.7
def callback_2(msg):
    global num_2
    num_2 = msg.process_value
rospy.Subscriber("/simple_model/up_to_shuttle_position_controller/state", JointControllerState, callback_2)

#conditions
while (abs(letter - (num-0.001)) > 0.005) or (abs(number - (num_2-0.001)) > 0.005):
    if (num != 0.700 and num_2 != 0.700):
        print ("Platform position:        " "%.3f" % num)
        print ("Support position:         " "%.3f" % num_2)
    position= letter
    position_2= number
    rospy.loginfo(position)
    pub_1.publish(position)
    pub_2.publish(position_2)
    rate.sleep()
