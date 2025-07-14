#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def pub_str():
    rospy.init_node('Publisher_str', anonymous=True)
    pub = rospy.Publisher('str_message', String, queue_size=10)
    rate = rospy.Rate(1)  

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi Sub!!"
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_str()
    except rospy.ROSInterruptException:
        pass