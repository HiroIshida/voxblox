import rospy
from voxblox_msgs.srv import SignedDistance
from geometry_msgs.msg import PointStamped

srv_name = "/voxblox_node/compute_sd"
rospy.wait_for_service(srv_name)
compute_sd = rospy.ServiceProxy(srv_name, SignedDistance)

origin = PointStamped()
compute_sd(origin, 10, 10, 10, 0.1)

