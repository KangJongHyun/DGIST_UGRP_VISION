import cv2
import numpy as np
import open3d as o3d
import pyrealsense2 as rs

# Configure RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

# Create Open3D visualizer
vis = o3d.visualization.Visualizer()

try:
    # Create Open3D visualizer window
    vis.create_window()

    while True:
        # Wait for a new frame
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Convert depth frame to numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Create point cloud from depth frame
        point_cloud = o3d.geometry.PointCloud.create_from_depth_image(
            o3d.geometry.Image(depth_image),
            o3d.camera.PinholeCameraIntrinsic(
                width=640, height=480, fx=640, fy=480, cx=320, cy=240
            ),
        )

        # Convert color frame to numpy array
        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

        # Update point cloud colors with color frame
        point_cloud.colors = o3d.utility.Vector3dVector(color_image.reshape(-1, 3) / 255.0)

        # Clear visualizer
        vis.clear_geometries()

        # Add point cloud to visualizer
        vis.add_geometry(point_cloud)

        # Update and visualize the scene
        vis.update_geometry(point_cloud)
        vis.poll_events()
        vis.update_renderer()

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Stop streaming and close the RealSense pipeline
    pipeline.stop()

    # Close the visualizer window
    vis.destroy_window()
