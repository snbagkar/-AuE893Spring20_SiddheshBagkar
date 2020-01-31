import rospy
from geometry_msgs.msg import Twist
#Defining a function
def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    i = 1
    while(i<5):#Looping strait and rotation movement
        i = i+1
        vel_msg.linear.x = 0.2 #setting linear speed
        t0 = rospy.Time.now().to_sec() #Setting the current time for distance calculus
        current_distance = 0
        while(current_distance < 2):#For strait movement
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec() #Storing actual time
            current_distance= 0.2*(t1-t0)
        vel_msg.linear.x = 0  #stopping the robot

        vel_msg.angular.z = 0.2
        t0 =  rospy.Time.now().to_sec() #Setting current time
        current_angle = 0 #Setting current angle
        while(current_angle<1.57):#for rotation of turtlesim
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec() #Using actual time for velocity
            current_angle= 0.2*(t1-t0)
        vel_msg.angular.z = 0#freezing the rotation


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
