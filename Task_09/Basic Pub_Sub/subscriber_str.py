#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received message: %s", msg.data)
    rospy.loginfo("Type of received message: %s", type(msg.data))

def sub_str():
    rospy.init_node('Subscriber_str', anonymous=True)
    rospy.Subscriber('str_message', String, callback)
    rospy.spin() 

if __name__ == '__main__':
    try:
        sub_str()
    except rospy.ROSInterruptException:
        pass
