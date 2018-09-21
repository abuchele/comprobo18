#!/usr/bin/env python

""" Runs motors """

import rospy
from neato_node.msg import Bump
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist

single_stop = False

class MotorController(object):
	def __init__(self):
		super(MotorController, self).__init__()
		rospy.init_node('motors')
		rospy.Subscriber("/emergency_stop", Bool, self.run_motors)
		self.publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		self.e_stopped = False
	def run_motors(self, msg):
		outmsg = Twist()
		outmsg.linear.y = 0
		outmsg.linear.z = 0
		outmsg.angular.x = 0
		outmsg.angular.y = 0
		outmsg.angular.z = 0
		if (msg.data):
			outmsg.linear.x = 0
			self.e_stopped = True
		else:
			outmsg.linear.x = 0.3
		if (single_stop):
			if (self.e_stopped):
				outmsg.linear.x = 0
		self.publisher.publish(outmsg)
	def run(self):
		rospy.spin()


if __name__ == '__main__':
	motors = MotorController()
	motors.run()