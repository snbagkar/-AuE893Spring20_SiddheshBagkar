#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
r=5
xco=[5,8,8,5,5] # added arrays
yco=[5,5,8,8,5]
class turtlebot():

    def __init__(self):
        print(1)
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        print(2)
        #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x,4)
        self.pose.y = round(self.pose.y,4)
        print(3)
    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance
        print(4)
    def move2goal(self):
        goal_pose = Pose()
        goal_pose.x = xco[i]
        goal_pose.y = yco[i]
        tolerance = 0.001
        vel_msg = Twist()

        #angle=self.pose.theta
        while((abs(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta))>0.0001):
            print(5)
            #angular velocity in the z-axis:
            vel_msg.angular.z = 2 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
            anglecorrect=abs(self.pose.theta-(atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)))
            self.velocity_publisher.publish(vel_msg)
            print(6)


        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))>= tolerance:
            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            self.velocity_publisher.publish(vel_msg)
            distance1= sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
        print(7)
    #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        print(8)

if __name__ == '__main__':

    for i in range(r):
        try:
    #Testing our function
            x = turtlebot()
            x.move2goal()
        except rospy.ROSInterruptException: pass
