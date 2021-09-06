
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()
globalValue = 'hello'

def imageCallback(ros_img):
    rospy.loginfo('Recieved img in ros format')

    #global bridge
    #cv_img = bridge.imgmsg_to_cv2(ros_img,'bgr8')

    #Perfrom required operation on openCV image
    #global globalValue
    #set globalValue value based on openCV image
    return True


if __name__ == '__main__':
    rospy.init_node('camera_node', anonymous=True)
    rospy.Subscriber('/usb_cam/image_raw',Image,imageCallback)
    rospy.loginfo(globalValue)
    rospy.spin()