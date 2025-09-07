#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

# global vars
front = None
left = None
right = None
pub = None

def fused_callback(msg):
    global front, left, right
    front = msg.x
    left = msg.y
    right = msg.z

    move = Twist()

    if front < 0.5:
        move.linear.x = 0.0
        if left > right:
            move.angular.z = 0.5   
            rospy.loginfo("Turning LEFT")
        else:
            move.angular.z = -0.5  
            rospy.loginfo("Turning RIGHT")
    else:
        move.linear.x = 0.8
        move.angular.z = 0.0
        rospy.loginfo("Moving forward")

    pub.publish(move)

def main():
    global pub
    rospy.init_node("obstacle_avoidance", anonymous=True)

    rospy.Subscriber("/fused_distances", Vector3, fused_callback)

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
