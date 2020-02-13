#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

import sys

def move_turtle(twist,twist):

    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10) # 10hz
 
    twist = Twist()
    while not rospy.is_shutdown():
        
	twist.linear.x = twist
	twist.linear.y = 0
	twist.linear.z = 0

	twist.angular.x = 0
	twist.angular.y = 0
	twist.angular.z = twist



        rospy.loginfo("Linear Vel = %f: Angular Vel = %f",twist,twist)

        pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(0.3),float(0.3))
    except rospy.ROSInterruptException:
        pass
