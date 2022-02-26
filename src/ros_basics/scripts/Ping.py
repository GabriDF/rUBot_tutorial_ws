#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('ping_node', anonymous=True)
    pub = rospy.Publisher('Ping', String, queue_size=10)
    rate = rospy.Rate(1) #1Hz = 1 Second.
    while not rospy.is_shutdown():
        Phrase = "Ping"
        rospy.loginfo(Phrase)
        pub.publish(Phrase)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
