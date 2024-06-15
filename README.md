# Real-Time-Traffic-Monitoring-System

This projects implement a system for tracking objects (likely vehicles) in a highway video. Here's a breakdown of the functionalities and packages used in each file:

#### 1. video_capture.py:

**Packages:** OpenCV (cv2)

**Task:** This script is to capture video using OpenCV. It reads frames from a specified video file ("highway.mp4") and displays them in a window. It also allows exiting the program by pressing the 'Esc' key (key code 27).


#### 2. White_Mask.py:

**Packages:** OpenCV (cv2)

**Task:** This script implements background subtraction for object detection. It uses OpenCV's createBackgroundSubtractorMOG2 algorithm to create a background model and then identifies foreground objects (likely vehicles) that deviate from the background in each frame.


#### 3. main.py:

**Packages:** OpenCV (cv2), tracker (custom module)

**Task:**
- This script combines object detection and tracking.

- It utilizes the object_detector from White_Mask.py for background subtraction.

- It defines a Region of Interest (ROI) within the frame to focus on the highway lane.
  
- It uses a custom EuclideanDistTracker class (from tracker.py) to track objects. This tracker identifies objects (vehicles) in each frame and assigns unique IDs to them. It likely uses the Euclidean distance between object centroids to determine if an object is the same as one detected in previous frames.

- The script displays the original frame, the mask (foreground objects), and a frame with bounding boxes and ID labels for the tracked objects.


#### 4. tracker.py:

**Packages:** math

**Task:** This script defines the EuclideanDistTracker class used for object tracking in main.py.

**The class:**
- Stores the center points of detected objects.
  
- Maintains a count for assigning unique IDs to new objects.

- Takes a list of object bounding boxes as input.

- Compares the center points of new objects with existing ones using Euclidean distance.

- If an object is close enough to a previously detected one (within a threshold distance), it considers it the same object and updates its center point. Otherwise, it assigns a new ID to the new object.

- It removes unused IDs from the tracked objects dictionary to maintain efficiency.

- It returns a list containing bounding boxes and corresponding IDs for the tracked objects.
