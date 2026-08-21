import cv2

def reverse_video(input_video_path, output_video_path):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Read all frames
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Reverse the frames
    frames = frames[::-1]

    # Save reversed video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()

    print("Reversed video saved successfully!")
    print("Saved at:", output_video_path)


# Input and Output paths
input_video = r"C:\Users\ARCHANA\Downloads\input_video.mp4"
output_video = r"C:\Users\ARCHANA\Downloads\output_reversed.mp4"

reverse_video(input_video, output_video)
