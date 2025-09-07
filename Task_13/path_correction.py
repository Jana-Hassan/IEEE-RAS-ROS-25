#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import math

Kp = 1.0
Ki = 0.0
Kd = 0.2

target_yaw = None
error_sum = 0.0
last_error = 0.0
pub = None

def imu_callback(msg):
    global target_yaw, error_sum, last_error

    q = msg.orientation
    quaternion = [q.x, q.y, q.z, q.w]
    (_, _, yaw) = euler_from_quaternion(quaternion)

 
    yaw = math.atan2(math.sin(yaw), math.cos(yaw))

    if target_yaw is None:
        target_yaw = yaw
        rospy.loginfo("Target yaw saved: %.2f" % target_yaw)
        return

    error = target_yaw - yaw
    error = math.atan2(math.sin(error), math.cos(error))  


    error_sum += error
    derivative = error - last_error
    control = Kp * error + Ki * error_sum + Kd * derivative


    move = Twist()
    move.linear.x = 0.3      
    move.angular.z = control   

    pub.publish(move)
    print(f"Yaw: {yaw:.3f}, Error: {error:.3f}, Control: {control:.3f}")

    last_error = error

def main():
    global pub
    rospy.init_node("pid_straight_line", anonymous=True)

    rospy.Subscriber("/mpu6050", Imu, imu_callback)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
