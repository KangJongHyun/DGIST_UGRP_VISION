import numpy as np
import cv2

# Load depth data from the text file
depth_data = np.loadtxt('depth_data.txt', dtype=np.uint16)

# Reshape depth data to image dimensions
depth_image = depth_data.reshape((480, 640))

# Scale depth values for visualization (optional)
depth_image = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Display the depth image
cv2.imshow('Depth Image', depth_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
