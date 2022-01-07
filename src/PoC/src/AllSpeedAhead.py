#!/usr/bin/env python3

from std_msgs.msg import String

import rospy

class AllSpeedAhead():
    def __init__(self):
        rospy.init_node('EXAMPLEnode', anonymous=False)     
        self.publisher = rospy.Publisher('/automobile/command', String, queue_size=1)
    
    def run(self):
        while True: 
            self.publisher.publish('{"action":"1","speed":2.0}') 

if __name__ == '__main__':
    try:
        nod = AllSpeedAhead()
        nod.run()
    except rospy.ROSInterruptException:
        pass
