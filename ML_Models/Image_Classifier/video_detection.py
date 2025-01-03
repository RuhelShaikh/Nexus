import cv2
import os
from roboflow import Roboflow

# Configuration Parameters
API_KEY = "W6DgvDUjwI7kvKIKjVmr"
PROJECT_NAME = "drug-detection-z6yhe"
MODEL_VERSION = "1"
VIDEO_PATH = r"D:\Projects\Project-Nexus-main\ML_Models\Image_Classifier\test_video.mp4"
OUTPUT_VIDEO_PATH = r"annoted_outputt.mp4"
CONFIDENCE_THRESHOLD = 0.8  # Define what confidence is considered 'high'
MIN_HIGH_CONF_DETECTIONS = 5  # Minimum number of high-confidence detections to flag
RISKY_FRAMES_FOLDER = "risky_frames"

# Initialize Roboflow and load the model
rf = Roboflow(api_key=API_KEY)
workspace = rf.workspace()
project = workspace.project(PROJECT_NAME)
model = project.version(MODEL_VERSION).model

# Create a folder for risky frames
if not os.path.exists(RISKY_FRAMES_FOLDER):
    os.makedirs(RISKY_FRAMES_FOLDER)

def save_risky_frame(frame, frame_index):
    """Save a risky frame to the risky_frames folder."""
    file_name = os.path.join(RISKY_FRAMES_FOLDER, f"frame_{frame_index}.jpg")
    cv2.imwrite(file_name, frame)
    print(f"Risky frame saved: {file_name}")

# Predict on the video
print("Starting video prediction...")
job_id, signed_url, expire_time = model.predict_video(
    VIDEO_PATH,
    fps=5,
    prediction_type="batch-video",
)
print(f"Job ID: {job_id}, Signed URL: {signed_url}, Expire Time: {expire_time}")

# Poll until results are ready
print("Polling for video results...")
results = model.poll_until_video_results(job_id)
print("Prediction results received.")

# Open the original video
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"Error: Unable to open video file {VIDEO_PATH}")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 5  # Use original FPS or default to 5 if unavailable

# Initialize VideoWriter to save the annotated video
out = cv2.VideoWriter(
    OUTPUT_VIDEO_PATH,
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

# Initialize variables for flagging
high_conf_detections_count = 0
flagged = False

# Ensure the results are in the correct format
predictions = results.get(PROJECT_NAME, [])

# Iterate over each frame and its corresponding predictions
print("Processing video frames...")
for idx, frame_result in enumerate(predictions):
    ret, frame = cap.read()
    if not ret:
        print(f"Warning: Unable to read frame {idx}. Skipping...")
        continue

    risky_frame = False  # Track if the current frame has high-confidence detections

    # Loop through each prediction in the current frame
    for prediction in frame_result.get('predictions', []):
        confidence = prediction.get('confidence', 0)
        if confidence >= CONFIDENCE_THRESHOLD:
            high_conf_detections_count += 1
            risky_frame = True

        x = int(prediction.get('x', 0))
        y = int(prediction.get('y', 0))
        width = int(prediction.get('width', 0))
        height = int(prediction.get('height', 0))
        label = f"{prediction.get('class', 'N/A')} ({confidence:.2f})"

        # Draw rectangle around the detected object
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        # Put label above the rectangle
        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    # Save the frame if it contains high-confidence detections
    if risky_frame:
        save_risky_frame(frame, idx)

    # Display the annotated frame
    cv2.imshow("Predicted Video", frame)

    # Write the annotated frame to the output video
    out.write(frame)

    # Check if flagging criteria are met
    if not flagged and high_conf_detections_count >= MIN_HIGH_CONF_DETECTIONS:
        flagged = True
        print(f"Video flagged at frame {idx} with {high_conf_detections_count} high-confidence detections.")

    # Press 'q' to exit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Early exit triggered by user.")
        break

# Release all resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Final flagging decision based on detections
if high_conf_detections_count >= MIN_HIGH_CONF_DETECTIONS:
    print(f"Video '{VIDEO_PATH}' has been flagged with {high_conf_detections_count} high-confidence detections.")
else:
    print(f"Video '{VIDEO_PATH}' is clean with {high_conf_detections_count} high-confidence detections.")

print(f"Annotated video has been saved as '{OUTPUT_VIDEO_PATH}'")
print(f"Risky frames have been saved in the folder: '{RISKY_FRAMES_FOLDER}'")