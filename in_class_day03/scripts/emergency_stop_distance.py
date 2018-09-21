#!/usr/bin/env python

""" Emergency stop upon receipt of bump message """

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool


class EmergencyStopController(object):
	def __init__(self):
		super(EmergencyStopController, self).__init__()
		rospy.init_node('emergency_stop_distance')
		rospy.Subscriber("/scan", LaserScan, self.process_scan)
		self.publisher = rospy.Publisher('/emergency_stop', Bool, queue_size=10)
	def process_scan(self, msg):
		outmsg = Bool()
		clean_ranges = self.remove_zeros(self.get_front_ranges(msg.ranges))
		if len(clean_ranges > 0):
			if (min(clean_ranges) < 0.5):
				outmsg.data = True
			else:
				outmsg.data = False
		else:
			outmsg.data = False
		self.publisher.publish(outmsg)
	def remove_zeros(self, ranges):
		ranges_out = []
		for val in ranges:
			if (val > 0):
				ranges_out.append(val)
		return ranges_out
	def get_front_ranges(self, ranges):
		return ranges[90:0:-1] + ranges[361:270:-1]
	def run(self):
		rospy.spin()


if __name__ == '__main__':
	emergency_stop = EmergencyStopController()
	emergency_stop.run()