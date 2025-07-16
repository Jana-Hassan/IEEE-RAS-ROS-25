#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def moving_forward():
    rospy.init_node('moving_forward', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    vel = Twist()
    vel.linear.x = 0.3  
    dis = 0.3          
    t = dis / vel.linear.x  

    rospy.loginfo("Moving forward....")

    rate = rospy.Rate(10)  
    start = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        now = rospy.Time.now().to_sec()
        if now - start < t:
            pub.publish(vel)
        else:
            vel.linear.x = 0.0
            pub.publish(vel)
            rospy.loginfo("30cm done in %.1f seconds!" % t)
            break
        rate.sleep()

if __name__ == '__main__':
    try:
        moving_forward()
    except rospy.ROSInterruptException:
        pass

