import numpy as np
from ransac import *

def augment(xyzs):
    axyz = np.ones((len(xyzs), 4))
    axyz[:, :3] = xyzs
    return axyz

def estimate(xyzs):
    axyz = augment(xyzs[:3])
    return np.linalg.svd(axyz)[-1][-1, :]

def is_inlier(coeffs, xyz, threshold):
    return np.abs(coeffs.dot(augment([xyz]).T)) < threshold

if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    import pyransac3d as pyrsc
    fig = plt.figure()
    ax = mplot3d.Axes3D(fig)

    def plot_plane(a, b, c, d):
        xx, yy = np.mgrid[:10, :10]
        return xx, yy, (-d - a * xx - b * yy) / c

    n = 100
    max_iterations = 100
    goal_inliers = n * 0.3

    # test data
    
    image = np.loadtxt("depth.txt")
    imagedot1 = np.array([0, 0, 0])
    imagedot2 = np.array([0, 0, 0])
    imagedot3 = np.array([0, 0, 0])
    imagedot4 = np.array([0, 0, 0])
    for i in range(0, 120, 2):
        print(i)
        for j in range(0, 640, 2):
            imagedot1 = np.vstack([imagedot1 ,[i/2, j/2, image[i][j]/3276.8]])
            imagedot2 = np.vstack([imagedot2 ,[(i+120)/2, j/2, image[i+120][j]/3276.8]])
            imagedot3 = np.vstack([imagedot3 ,[(i+240)/2, j/2, image[i+240][j]/3276.8]])
            imagedot4 = np.vstack([imagedot4 ,[(i+360)/2, j/2, image[i+360][j]/3276.8]])
            #print(imagedot)
    imagedot = np.vstack([np.vstack([imagedot1, imagedot2]) ,np.vstack([imagedot3, imagedot4])])
    np.savetxt("./imagedot_stride3.txt", imagedot, fmt="%d")
    
    #imagedot=np.loadtxt("imagedot_stride2.txt")
    print(imagedot)
    xyzs = np.random.random((n, 3)) * 10
    print(xyzs)
    xyzs[:50, 2:] = xyzs[:50, :1]

    ax.scatter3D(imagedot.T[0], imagedot.T[1], imagedot.T[2], marker='o', c=imagedot.T[2]/10, cmap="Greens")

    # RANSAC
    m, best_inliers = run_ransac(imagedot, estimate, lambda x, y: is_inlier(x, y, 1), 3, goal_inliers, max_iterations)
    a, b, c, d = m
    """
    plane1 = pyrsc.Plane()
    best_eq, best_in = plane1.fit(imagedot)
    a, b, c, d = best_eq
    """
    xx, yy, zz = plot_plane(a, b, c, d)
    ax.plot_surface(xx, yy, zz, color='b')

    plt.show()
