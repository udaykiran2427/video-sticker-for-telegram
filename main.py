import cv2

# Open the input video
cap = cv2.VideoCapture('input.mp4')

# Get original width, height, and aspect ratio
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
aspect_ratio = original_width / original_height

# Calculate new dimensions
if original_width > original_height:
    new_width = 512
    new_height = int(512 / aspect_ratio)
else:
    new_height = 512
    new_width = int(512 * aspect_ratio)

# Define the codec for MP4 (H264 or mp4v)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'H264' for better compression if available
out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (new_width, new_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    out.write(resized_frame)

cap.release()
out.release()