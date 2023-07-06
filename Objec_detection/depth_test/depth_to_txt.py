import pyrealsense2 as rs
import numpy as np

# Configure RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start streaming
pipeline.start(config)

try:
    # Wait for a new frame
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()

    if depth_frame:
        # Convert depth frame to numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Save depth data to a text file
        np.savetxt('depth_test/depth_data.txt', depth_image, fmt='%d')

        print("Depth data saved successfully.")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Stop streaming and close the RealSense pipeline
    pipeline.stop()
