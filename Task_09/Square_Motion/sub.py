#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(stat_msg):
    rospy.loginfo("Turtle Status: %s", stat_msg.data)

def sub_status():
    rospy.init_node('sub_status', anonymous=True)
    rospy.Subscriber('/turtle_status', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        sub_status()
    except rospy.ROSInterruptException:
        pass
