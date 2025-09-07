#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math


start_x = None
start_y = None

def odom_callback(msg):
    global start_x, start_y

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

  
    if start_x is None and start_y is None:
        start_x = x
        start_y = y
        return


    dist = math.sqrt((x - start_x)**2 + (y - start_y)**2)
    rospy.loginfo("distance = %.2f" % dist)

    move = Twist()
    if dist < 0.3:     
        move.linear.x = 0.1
    else:             
        move.linear.x = 0.0
        rospy.loginfo("Stopped!")

    pub.publish(move)

def main():
    rospy.init_node("move_forward", anonymous=True)


    global pub
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rospy.Subscriber("/odom", Odometry, odom_callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
