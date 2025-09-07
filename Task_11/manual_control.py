#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Range
from nav_msgs.msg import Odometry


def imu_callback(msg):
    rospy.loginfo("IMU data")

def ultrasonic_front_callback(msg):
    rospy.loginfo("Front ultrasonic: %f" % msg.range)

def ultrasonic_left_callback(msg):
    rospy.loginfo("Left ultrasonic: %f" % msg.range)

def ultrasonic_right_callback(msg):
    rospy.loginfo("Right ultrasonic: %f" % msg.range)

def odom_callback(msg):
    rospy.loginfo("odometry data")

def listener():
    rospy.init_node("listener", anonymous=True)

    rospy.Subscriber("/mpu6050", Imu, imu_callback)
    rospy.Subscriber("/ultrasonic_front/sonar", Range, ultrasonic_front_callback)
    rospy.Subscriber("/ultrasonic_left/sonar", Range, ultrasonic_left_callback)
    rospy.Subscriber("/ultrasonic_right/sonar", Range, ultrasonic_right_callback)
    rospy.Subscriber("/odom", Odometry, odom_callback)

    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass