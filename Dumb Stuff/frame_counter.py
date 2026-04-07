# LEARNING Goal: Functions, External Libraries (OpenCV), and Data Processing
# This script analyzes video files and extracts metadata like resolution, frame count, and FPS.
# It teaches: function definition, importing modules, video processing, data structures (defaultdict),
# conditional logic, loops, and formatting output.

import cv2
from collections import defaultdict

def analyze_video(video_path):
    """Analyzes a video file and prints metadata and frame statistics."""
    # Open the video file using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    # Extract video metadata
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = 0
    frames_per_second = defaultdict(int)  # Dictionary to count frames per second
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Video width in pixels
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Video height in pixels

    # Determine common quality label based on resolution
    resolution_label = f"{width}x{height}"
    if width >= 3840 or height >= 2160:
        resolution_label += " (4K)"
    elif width >= 2560 or height >= 1440:
        resolution_label += " (2K/QHD)"
    elif width >= 1920 or height >= 1080:
        resolution_label += " (1080p/Full HD)"
    elif width >= 1280 or height >= 720:
        resolution_label += " (720p/HD)"
    else:
        resolution_label += " (SD or lower)"

    # Read through the entire video frame by frame
    while True:
        # Read the next frame from the video
        ret, frame = cap.read()
        # If ret is False, we've reached the end of the video
        if not ret:
            break
        # Get the current position in milliseconds and convert to seconds
        current_time_sec = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
        # Increment the frame count for this second
        frames_per_second[current_time_sec] += 1
        # Increment the total frame count
        total_frames += 1

    # Release the video capture object
    cap.release()

    # Print the analysis results
    print(f"Video path: {video_path}")
    print(f"Resolution: {resolution_label}")
    print(f"Total frames: {total_frames}")
    print(f"Video FPS (reported): {fps:.2f}")
    print("\nFrames per second:")

    # Print frame count for each second
    for second in sorted(frames_per_second.keys()):
        print(f"Second {second}: {frames_per_second[second]} frames")

# Example usage
video_file = "/mnt/chromeos/MyFiles/Downloads/VID-20260215-WA0031.mp4"  # Update to your actual path
analyze_video(video_file)