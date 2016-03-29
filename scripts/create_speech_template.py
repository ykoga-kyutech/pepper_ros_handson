#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray

class CreateSpeech:

    def __init__(self):
        
        # init node
        rospy.init_node('create_speech')

        # Publisher
        self.pub = rospy.Publisher('speech', String, queue_size=1)

        # Subscriber
        rospy.Subscriber('objects', Float32MultiArray, self.callback)

    def callback(self, msg):

        if len(msg.data):
            rospy.loginfo('object found.')
        else:
            rospy.loginfo('object NOT found.')

def main():

    speech = CreateSpeech()

    # loop rate [Hz]
    r = rospy.Rate(0.3)

    while not rospy.is_shutdown():
        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
