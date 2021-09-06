import rospy


from robo_proj.msg import fwd_motor

def fwd_motorCallback(msg):
    rospy.loginfo('speed of motor is '+ str(msg.speed))
    print('time to reach destination is '+str(msg.duration))


if __name__=='__main__':

    rospy.init_node('fwd_motor',anonymous=True)
    rospy.Subscriber('fwd_motor_topic',fwd_motor,fwd_motorCallback)
    rospy.spin()
    

