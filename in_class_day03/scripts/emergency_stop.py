#!/usr/bin/env python

""" Emergency stop upon receipt of bump message """

import rospy
from neato_node.msg import Bump
from std_msgs.msg import Bool


class EmergencyStopController(object):
	def __init__(self):
		super(EmergencyStopController, self).__init__()
		rospy.init_node('emergency_stop')
		rospy.Subscriber("/bump", Bump, self.process_bump)
		self.publisher = rospy.Publisher('/emergency_stop', Bool, queue_size=10)
	def process_bump(self, msg):
		outmsg = Bool()
		if (msg.leftFront or msg.leftSide or msg.rightFront or msg.rightSide):
			outmsg.data = True
		else:
			outmsg.data = False
		self.publisher.publish(outmsg)
	def run(self):
		rospy.spin()


if __name__ == '__main__':
	emergency_stop = EmergencyStopController()
	emergency_stop.run()