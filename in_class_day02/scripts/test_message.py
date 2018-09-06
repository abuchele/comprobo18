#!/usr/bin/env python

""" This script explores publishing ROS messages in ROS using Python """

from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy


class PublishMessage(object):
	def __init__(self, point):
		super(PublishMessage, self).__init__()
		rospy.init_node('test_message')
		self.point = point
		self.publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
	def publish_point(self):
		my_point_stamped = PointStamped(header=Header(stamp=rospy.Time.now(), frame_id="odom"), point=self.point)
		self.publisher.publish(my_point_stamped)
	def run(self):
		r = rospy.Rate(2)
		while not rospy.is_shutdown():
			self.publish_point()
			r.sleep()

if __name__ == '__main__':
	publishMessage = PublishMessage(Point(1.0, 1.0, 1.0))
	publishMessage.run()