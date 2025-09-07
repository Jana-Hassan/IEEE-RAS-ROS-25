#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    valid_ranges = []
    for r in msg.ranges:
        if r > 0.0 and r < 100.0:   # بنعتبر أي قيمة موجبة ومعقولة صالحة
            valid_ranges.append(r)

    if valid_ranges:
        min_dist = min(valid_ranges)
        rospy.loginfo("Closest object: %.2f m" % min_dist)
    else:
        rospy.loginfo("Nothing detected!")

def listener():
    rospy.init_node('lidar_object_detection', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

