#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def chat_callback(msg):
    rospy.loginfo("Chat topic says: %s", msg.data)

def status_callback(msg):
    rospy.loginfo("Status update: %s", msg.data)

def multi_listener():
    rospy.init_node("multi_topic_subscriber", anonymous=True)

    rospy.Subscriber("chatter", String, chat_callback)      
    rospy.Subscriber("robot_status", String, status_callback) 

    rospy.loginfo("Multi-topic subscriber is running...")
    rospy.spin()

if __name__ == "__main__":
    try:
        multi_listener()
    except rospy.ROSInterruptException:
        pass
