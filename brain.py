import rospy
import math
import sys

from sensor_msgs.msg import Image, Range, LaserScan
from robo_proj.msg import fwd_motor, lat_motor
#def laserCallback(scan):
    #rospy.loginfo('Message recieved from Lidar')
    #print(scan)

#def imageCallback(img):
 #   rospy.loginfo('Message recieved from Camera')

#def sonarCallback(msg):
#    rospy.loginfo('Message recieved from Sonar')
#    print(msg)


#All ROS Topics need to be reviewed
if __name__ == '__main__':
    rospy.init_node('brain_node',anonymous=False)
    # LIDAR
    #rospy.Subscriber('/kobuki/laser/scan',LaserScan,laserCallback)

    # RGB CAMERA
    #rospy.Subscriber('/camera/Image',Image,imageCallback)

    #SONAR
    #rospy.Subscriber('/sonar/sensor0',Range,sonarCallback)

    # Forward motor 
    f_pub =rospy.Publisher('fwd_motor_topic',fwd_motor,queue_size=10)
    
    # Lat motor 
    l_pub = rospy.Publisher('lat_motor_topic',lat_motor, queue_size=10)

    while not rospy.is_shutdown():
        f_motor = fwd_motor()
        f_motor.speed = 10
        f_motor.duration = 2
        l_motor = lat_motor()
        l_motor.angle = math.radians(50)
        rospy.loginfo('----------Forward motor--------------' )
        rospy.loginfo( 'Speed of motor: '+ str(f_motor.speed) )
        rospy.loginfo('Time to reach destination is: '+ str(f_motor.duration))

        rospy.loginfo('-----------Lateral motor------------')
        rospy.loginfo('Angle of motor:-' + str(l_motor))

        f_pub.publish(f_motor)
        l_pub.publish(l_motor)
        rospy.sleep(2)

    sys.exit()