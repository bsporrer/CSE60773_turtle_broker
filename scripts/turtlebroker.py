#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' I heard %s', [data.linear.x, data.linear.y, data.linear.z])
    #rospy.loginfo(rospy.get_caller_id() + ' I heard %s', [data.angular.x, data.angular.y, data.angular.z])
    pub = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=10)
    move = Twist()
    move.linear.x = data.linear.x
    move.linear.y = data.linear.y
    move.linear.z = data.linear.z
    move.angular.x = data.angular.x
    move.angular.y = data.angular.y
    move.angular.z = data.angular.z
    rospy.loginfo(move)
    pub.publish(move)

def listener():

    rospy.init_node('turtlebroker', anonymous=True)
     
    rospy.Subscriber('turtle1/cmd_vel', Twist, callback)
    
    rate = rospy.Rate(10) # 10 h
		
    rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
