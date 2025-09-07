#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range, LaserScan
from geometry_msgs.msg import Vector3

front_val = None
left_val = None
right_val = None
lidar_val = None

fused_msg = Vector3()
pub = None


def front_callback(msg):
    global front_val
    if 0.0 < msg.range < float("inf"):
        front_val = msg.range

def left_callback(msg):
    global left_val
    if 0.0 < msg.range < float("inf"):
        left_val = msg.range

def right_callback(msg):
    global right_val
    if 0.0 < msg.range < float("inf"):
        right_val = msg.range

def lidar_callback(msg):
    global lidar_val
    values = list(msg.ranges[0:10]) + list(msg.ranges[-10:])
    valid = [d for d in values if 0.0 < d < float("inf")]
    if valid:
        lidar_val = min(valid)


def fuse(event):
    global fused_msg
    if front_val and left_val and right_val and lidar_val:
        fused_front = min(front_val, lidar_val)

        rospy.loginfo(f"Front: {fused_front:.2f} m | Left: {left_val:.2f} m | Right: {right_val:.2f} m")

        fused_msg.x = fused_front
        fused_msg.y = left_val
        fused_msg.z = right_val
        pub.publish(fused_msg)


def main():
    global pub
    rospy.init_node("fusion_node", anonymous=True)

    rospy.Subscriber("/ultrasonic_front/sonar", Range, front_callback)
    rospy.Subscriber("/ultrasonic_left/sonar", Range, left_callback)
    rospy.Subscriber("/ultrasonic_right/sonar", Range, right_callback)
    rospy.Subscriber("/lidar_sensor_2D", LaserScan, lidar_callback)

    pub = rospy.Publisher("/fused_distances", Vector3, queue_size=10)
    rospy.Timer(rospy.Duration(0.5), fuse)

    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
