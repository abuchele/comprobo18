#!/usr/bin/env python

""" Investigate receiving a message using a callback function """

from geometry_msgs.msg import PointStamped
import rospy


class RecieveMessage(object):
	def __init__(self):
		super(RecieveMessage, self).__init__()
		rospy.init_node('receive_message')
		rospy.Subscriber("/my_point", PointStamped, self.process_point)
	def process_point(self, msg):
		print msg.header
	def run(self):
		rospy.spin()

if __name__ == '__main__':
	receiveMessage = RecieveMessage()
	receiveMessage.run()