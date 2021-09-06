import rospy


from robo_proj.msg import lat_motor

def lat_motorCallback(msg):
    rospy.loginfo('angle of motor is '+ str(msg.angle))


if __name__=='__main__':

    rospy.init_node('lat_motor',anonymous=True)
    rospy.Subscriber('lat_motor_topic',lat_motor,lat_motorCallback)
    rospy.spin()
    