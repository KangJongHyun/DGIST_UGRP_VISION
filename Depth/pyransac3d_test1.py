import pyransac3d as pyrsc
import numpy as np
import matplotlib.pyplot as plt


plane1 = pyrsc.Plane()
#best_eq, best_inliers = plane1.fit(points, 0.01)

imagedot = np.loadtxt("imagedot_stride3.txt")
#np.savetxt("./imagedot.txt", image, fmt="%d")

best_eq, best_inliers=plane1.fit(imagedot)
print(best_eq, best_inliers)

plt.show()

