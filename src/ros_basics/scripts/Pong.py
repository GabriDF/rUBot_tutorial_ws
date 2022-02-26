#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    response = String()
    if (msg.data == "Ping"):
        response.data = "Pong"
        rospy.loginfo(response)
        pub.publish(response)
    else (msg.data != "Ping"):
         response.data =  "Failed!"
         rospy.loginfo(response)
         pub.publish(response)   

rospy.init_node('pong_node')
sub = rospy.Subscriber('Ping', String, callback)
pub = rospy.Publisher('Pong', String, queue_size=10)
rospy.spin()