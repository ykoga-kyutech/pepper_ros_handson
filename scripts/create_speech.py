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

        # object dictionary
        self.known_objects = {1:"らんま", 2:"ペッパーのおしらせ"}

        # recognized object
        self.obj_name = ''

    def callback(self, msg):

        if len(msg.data):
            rospy.loginfo('object found.')

            # get object ID
            idx = int(msg.data[0])

            # if the dictionary includes the object ID
            if idx in self.known_objects:
                self.obj_name = self.known_objects[idx]
        else:
            rospy.loginfo('object NOT found.')
            self.obj_name = ''

    def pub_speech(self):
        
        if self.obj_name != '':
            speech_str = self.obj_name + 'だね'
            self.pub.publish(speech_str)

def main():

    speech = CreateSpeech()

    # loop rate [Hz]
    r = rospy.Rate(0.3)

    while not rospy.is_shutdown():
        speech.pub_speech()
        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
