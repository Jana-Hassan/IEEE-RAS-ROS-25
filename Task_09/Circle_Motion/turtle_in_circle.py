#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def T_circle():
    rospy.init_node('circle_motion', anonymous=True)
    
    velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    status_pub = rospy.Publisher('/turtle_status', String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 2.0
        vel_msg.linear.y = 0.0
        vel_msg.angular.z = 1.0

        status_msg = String()
        status_msg.data = "rotating"
        
        velocity_pub.publish(vel_msg)
        status_pub.publish(status_msg)
        
        rospy.loginfo("rotating....")
        rate.sleep()

if __name__ == '__main__':
    try:
        T_circle()
    except rospy.ROSInterruptException:
        pass
