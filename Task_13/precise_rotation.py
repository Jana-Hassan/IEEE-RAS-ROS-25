#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import math

Kp = 1.2
Ki = 0.0
Kd = 0.3

current_yaw = None
target_yaw = None
error_sum = 0.0
last_error = 0.0
cmd_pub = None
tolerance = math.radians(1)

def wrap_angle(angle):
    while angle > math.pi:
        angle -= 2*math.pi
    while angle < -math.pi:
        angle += 2*math.pi
    return angle

def imu_callback(msg):
    global current_yaw
    q = msg.orientation
    (_, _, current_yaw) = euler_from_quaternion([q.x, q.y, q.z, q.w])
    current_yaw = wrap_angle(current_yaw)

def stop_robot():
    twist = Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    cmd_pub.publish(twist)

def control_loop(event):
    global error_sum, last_error
    if current_yaw is None or target_yaw is None:
        return

    error = wrap_angle(target_yaw - current_yaw)
    if abs(error) < tolerance:
        stop_robot()
        rospy.signal_shutdown("Finished 90° turn")
        return

    error_sum += error
    derivative = error - last_error
    angular_z = Kp*error + Ki*error_sum + Kd*derivative
    last_error = error

    angular_z = max(min(angular_z, 0.5), -0.5)
    twist = Twist()
    twist.angular.z = angular_z
    twist.linear.x = 0.0
    cmd_pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node("rotate_90")
    cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("/mpu6050", Imu, imu_callback)


    while current_yaw is None and not rospy.is_shutdown():
        rospy.sleep(0.1)

    target_yaw = wrap_angle(current_yaw + math.radians(90))

    rospy.Timer(rospy.Duration(0.05), control_loop)
    rospy.spin()

