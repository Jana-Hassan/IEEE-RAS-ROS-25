#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def T_square():
    rospy.init_node('square_motion', anonymous=True)

    pub_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub_stat = rospy.Publisher('/turtle_status', String, queue_size=10)

    move = Twist()
    rotate = Twist()
    stop = Twist()

    move.linear.x = 2.0
    rotate.angular.z = 1.57

    for i in range(4):
        pub_stat.publish(String(data="forward"))
        pub_vel.publish(move)
        rospy.loginfo("T is moving forward....")
        rospy.sleep(2.5)

        pub_vel.publish(stop)
        rospy.sleep(0.3)

        pub_stat.publish(String(data="rotating"))
        pub_vel.publish(rotate)
        rospy.loginfo("T is rotating....")
        rospy.sleep(1.5)

        pub_vel.publish(stop)
        rospy.sleep(0.3)

    pub_stat.publish(String(data="forward"))
    pub_vel.publish(move)
    rospy.loginfo("T is returning to start...")
    rospy.sleep(2.5)

    pub_vel.publish(stop)
    pub_stat.publish(String(data="stopped!"))
    rospy.loginfo("T has stopped.")

if __name__ == '__main__':
    try:
        T_square()
    except rospy.ROSInterruptException:
        pass





