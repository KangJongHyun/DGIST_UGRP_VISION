import numpy as np
import cv2

def create_ground_base(height, angle, depth, g_angle):
    d_error = 0.1 #땅 탐지를 위한 거리 오차
    #need: 땅만 딱 찍은 사진
    #현재 땅 탐지가 애매하게 된다면, 경고
    #오차 계산을 어떻게 해야할지 모르겠음
    #g_angle은 땅의 기울기

    base = np.full((480, 640), height)

    grad = np.linspace(7000, 800, 480)
    #print(grad)
    grad = grad.reshape(480 , 1)
    #print(grad)
    t_grad = grad
    for i in range(639):
        grad = grad + (0)      #카메라 좌우 angle 값에 따라서 변경
        t_grad = np.hstack((t_grad, grad))

    return base + t_grad


def ground_detect(depth, ground_base):
    error = 300
    #expect = np.zeros(480, 640)
    data = depth - ground_base
    expect = np.where(abs(data) < error, 1, 0)
    return expect

depth_image = np.loadtxt("depth.txt")
ground_base = create_ground_base(100, 0, 0, 0)

ground_colormap = cv2.applyColorMap(cv2.convertScaleAbs(ground_base, alpha=0.03), cv2.COLORMAP_JET)
depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
#depth_colormap = ground_detect(100, 0, 0, 0)
expect = ground_detect(depth_image, ground_base)

expect_colormap = cv2.applyColorMap(cv2.convertScaleAbs(expect, alpha=100), cv2.COLORMAP_JET)

images = np.hstack((ground_colormap, depth_colormap))
images = np.hstack((images, expect_colormap))

while True:
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', images)
    if (cv2.waitKey(1)==27):
        break