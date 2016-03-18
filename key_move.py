#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see http://wiki.ros.org/keyboard

import rospy
from keyboard.msg import Key
from geometry_msgs.msg import Twist

code = 0

def key_down_cb(data):
    global code, key_up
    code = data.code
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.code)

def main():

    # pubs & subs
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("/keyboard/keydown", Key, key_down_cb)

    # parameters
    linear_vel = rospy.get_param('~linear_vel', 0.3)
    angular_vel = rospy.get_param('~angular_vel', 0.3)

    # create node
    rospy.init_node('key_move')

    r = rospy.Rate(10) # 10hz
    
    global code
    while not rospy.is_shutdown():
        vel = Twist()

        if code == Key.KEY_UP:
            vel.linear.x = linear_vel
        elif code == Key.KEY_DOWN:
            vel.linear.x = -linear_vel
        elif code == Key.KEY_LEFT:
            vel.angular.z = angular_vel
        elif code == Key.KEY_RIGHT:
            vel.angular.z = -angular_vel

        str = 'Pulishing (linear, angular)=({0}, {1})'.format(vel.linear.x, vel.angular.z)
        rospy.loginfo(str)

        # publish the velocity
        pub.publish(vel)

        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass