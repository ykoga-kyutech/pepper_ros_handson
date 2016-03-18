#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see http://wiki.ros.org/keyboard

import rospy
from std_msgs.msg import String
from keyboard.msg import Key

code = 0

def key_down_cb(data):
    global code
    code = data.code
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.code)

def main():

    # pubs & subs
    pub = rospy.Publisher('/sound', String, queue_size=10)
    rospy.Subscriber("/keyboard/keydown", Key, key_down_cb)

    # create node
    rospy.init_node('key_sound')

    r = rospy.Rate(10) # 10hz
    
    global code
    last_code = 0
    while not rospy.is_shutdown():
        sound_str = String()

        if last_code != code:
            if code == Key.KEY_UP:
                sound_str = 'forward'
            elif code == Key.KEY_DOWN:
                sound_str = 'back'
            elif code == Key.KEY_LEFT:
                sound_str = 'turn left'
            elif code == Key.KEY_RIGHT:
                sound_str = 'turn right'
            else:
                sound_str = "stop"

            str = 'Pulishing %s'%sound_str
            rospy.loginfo(str)

            # publish the sound
            pub.publish(sound_str)

        last_code = code

        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass