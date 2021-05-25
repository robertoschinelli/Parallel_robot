#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState


var = raw_input("enter coordinates: ")
print "you entered", var

if var in 'A1':
 	print ("sposto in posizione A1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num > -0.6115 or num_2 > -0.6115:
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'B1':
 	print ("sposto in posizione B1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num > -0.4365 or num < -0.4385) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()





elif var in 'C1':
 	print ("sposto in posizione C1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num > -0.2615 or num < -0.2635) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()



elif var in 'D1':
 	print ("sposto in posizione D1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num > -0.0865 or num < -0.0885) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*3)
    		rate.sleep()



elif var in 'E1':
 	print ("sposto in posizione E1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.0865 or num < 0.0885) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*4)
    		rate.sleep()



elif var in 'F1':
 	print ("sposto in posizione F1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.2615 or num > 0.2635) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*5)
    		rate.sleep()



elif var in 'G1':
 	print ("sposto in posizione G1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.4365 or num > 0.4385) or num_2 > -0.6115:
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*6)
    		rate.sleep()



elif var in 'H1':
 	print ("sposto in posizione H1")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num > 0.6115  or num_2 > -0.6115:
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*7)
    		rate.sleep()



#inizio
elif var in 'A2':
 	print ("sposto in posizione A2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num > -0.6115 or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'B2':
 	print ("sposto in posizione B2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.4385 or num > -0.4365) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'C2':
 	print ("sposto in posizione C2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.2635 or num > -0.2615) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


elif var in 'D2':
 	print ("sposto in posizione D2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.0885 or num > -0.0865) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()


elif var in 'E2':
 	print ("sposto in posizione E2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.0865 or num > 0.0885) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*3)
    		rate.sleep()


elif var in 'F2':
 	print ("sposto in posizione F2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.2615 or num > 0.2635) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*4)
    		rate.sleep()


elif var in 'G2':
 	print ("sposto in posizione G2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.4365 or num > 0.4385) or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*5)
    		rate.sleep()


elif var in 'H2':
 	print ("sposto in posizione H2")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num < 0.6115 or (num_2 < -0.4385 or num_2 > -0.4365):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*6)
    		rate.sleep()


#inizio
elif var in 'A3':
 	print ("sposto in posizione A3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num > -0.6115 or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'B3':
 	print ("sposto in posizione B3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.4385 or num > -0.4365) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'C3':
 	print ("sposto in posizione C3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.2635 or num > -0.2615) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'D3':
 	print ("sposto in posizione D3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.0885 or num > -0.0865) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


elif var in 'E3':
 	print ("sposto in posizione E3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.0865 or num > 0.0885) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()


elif var in 'F3':
 	print ("sposto in posizione F3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.2615 or num > 0.2635) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*3)
    		rate.sleep()


elif var in 'G3':
 	print ("sposto in posizione G3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.4365 or num > 0.4385) or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*4)
    		rate.sleep()


elif var in 'H3':
 	print ("sposto in posizione H3")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num < 0.6115 or (num_2 < -0.2635 or num_2 > -0.2615):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*5)
    		rate.sleep()


#inizio
elif var in 'A4':
 	print ("sposto in posizione A4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num > -0.6115 or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*3)
    		rate.sleep()


elif var in 'B4':
 	print ("sposto in posizione B4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.4385 or num > -0.4365) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'C4':
 	print ("sposto in posizione C4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.2635 or num > -0.2615) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'D4':
 	print ("sposto in posizione D4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < -0.0885 or num > -0.0865) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'E4':
 	print ("sposto in posizione E4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.0865 or num > 0.0885) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


elif var in 'F4':
 	print ("sposto in posizione F4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.2615 or num > 0.2635) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()


elif var in 'G4':
 	print ("sposto in posizione G4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while (num < 0.4365 or num > 0.4385) or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*3)
    		rate.sleep()


elif var in 'H4':
 	print ("sposto in posizione H4")
	rospy.init_node('listenernode')

	pub_1 = rospy.Publisher('/simple_model/bridge_to_platform_position_controller/command', Float64, queue_size=10)
	pub_2 = rospy.Publisher('/simple_model/up_to_shuttle_position_controller/command', Float64, queue_size=10)

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



	while num < 0.6115 or (num_2 < -0.0885 or num_2 > -0.0865):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*4)
    		rate.sleep()


#inizio
elif var in 'A5':
 	print ("sposto in posizione A5")
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



	while num > -0.6115 or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*4)
    		rate.sleep()


elif var in 'B5':
 	print ("sposto in posizione B5")
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



	while (num < -0.4385 or num > -0.4365) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*3)
    		rate.sleep()


elif var in 'C5':
 	print ("sposto in posizione C5")
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



	while (num < -0.2635 or num > -0.2615) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'D5':
 	print ("sposto in posizione D5")
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



	while (num < -0.0885 or num > -0.0865) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'E5':
 	print ("sposto in posizione E5")
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



	while (num < 0.0865 or num > 0.0885) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'F5':
 	print ("sposto in posizione F5")
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



	while (num < 0.2615 or num > 0.2635) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


elif var in 'G5':
 	print ("sposto in posizione G5")
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



	while (num < 0.4365 or num > 0.4385) or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()


elif var in 'H5':
 	print ("sposto in posizione H5")
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



	while num < 0.6115 or (num_2 < 0.0865 or num_2 > 0.0885):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*3)
    		rate.sleep()



#inizio
elif var in 'A6':
 	print ("sposto in posizione A6")
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



	while num > -0.6115 or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*5)
    		rate.sleep()


elif var in 'B6':
 	print ("sposto in posizione B6")
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



	while (num < -0.4385 or num > -0.4365) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*4)
    		rate.sleep()


elif var in 'C6':
 	print ("sposto in posizione C6")
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



	while (num < -0.2635 or num > -0.2615) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*3)
    		rate.sleep()


elif var in 'D6':
 	print ("sposto in posizione D6")
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



	while (num < -0.0885 or num > -0.0865) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'E6':
 	print ("sposto in posizione E6")
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



	while (num < 0.0865 or num > 0.0885) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'F6':
 	print ("sposto in posizione F6")
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



	while (num < 0.2615 or num > 0.2635) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'G6':
 	print ("sposto in posizione G6")
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



	while (num < 0.4365 or num > 0.4385) or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


elif var in 'H6':
 	print ("sposto in posizione H6")
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



	while num < 0.6115 or (num_2 < 0.2615 or num_2 > 0.2635):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175*2)
    		rate.sleep()



#inizio
elif var in 'A7':
 	print ("sposto in posizione A7")
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



	while num > -0.6115 or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*6)
    		rate.sleep()


elif var in 'B7':
 	print ("sposto in posizione B7")
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



	while (num < -0.4385 or num > -0.4365) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*5)
    		rate.sleep()


elif var in 'C7':
 	print ("sposto in posizione C7")
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



	while (num < -0.2635 or num > -0.2615) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*4)
    		rate.sleep()


elif var in 'D7':
 	print ("sposto in posizione D7")
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



	while (num < -0.0885 or num > -0.0865) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*3)
    		rate.sleep()


elif var in 'E7':
 	print ("sposto in posizione E7")
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



	while (num < 0.0865 or num > 0.0885) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'F7':
 	print ("sposto in posizione F7")
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



	while (num < 0.2615 or num > 0.2635) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'G7':
 	print ("sposto in posizione G7")
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



	while (num < 0.4365 or num > 0.4385) or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()


elif var in 'H7':
 	print ("sposto in posizione H7")
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



	while num < 0.6115 or (num_2 < 0.4365 or num_2 > 0.4385):
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position-0.175)
    		rate.sleep()


#inizio
elif var in 'A8':
 	print ("sposto in posizione A8")
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



	while num > -0.6115 or num_2 < 0.6115:
   		print num
    		print num_2
    		position= -0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*7)
    		rate.sleep()


elif var in 'B8':
 	print ("sposto in posizione B8")
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



	while (num < -0.4385 or num > -0.4365) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= -0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*6)
    		rate.sleep()


elif var in 'C8':
 	print ("sposto in posizione C8")
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



	while (num < -0.2635 or num > -0.2615) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= -0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*5)
    		rate.sleep()


elif var in 'D8':
 	print ("sposto in posizione D8")
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



	while (num < -0.0885 or num > -0.0865) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= -0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*4)
    		rate.sleep()


elif var in 'E8':
 	print ("sposto in posizione E8")
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



	while (num < 0.0865 or num > 0.0885) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= 0.0875
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*3)
    		rate.sleep()


elif var in 'F8':
 	print ("sposto in posizione F8")
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



	while (num < 0.2615 or num > 0.2635) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= 0.2625
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175*2)
    		rate.sleep()


elif var in 'G8':
 	print ("sposto in posizione G8")
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



	while (num < 0.4365 or num > 0.4385) or num_2 < 0.6115:
   		print num
    		print num_2
    		position= 0.4375
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position+0.175)
    		rate.sleep()


elif var in 'H8':
 	print ("sposto in posizione H8")
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



	while num < 0.6115 or num_2 < 0.6115:
   		print num
    		print num_2
    		position= 0.6125
    		rospy.loginfo(position)
    		pub_1.publish(position)
    		pub_2.publish(position)
    		rate.sleep()
