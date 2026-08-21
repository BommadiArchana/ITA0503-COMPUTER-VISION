import cv2

def play_video_reverse_slow(video_path):

    # Open the video
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Store all frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Total frames:", len(frames))

    # Play video in reverse slow motion
    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion Video", frame)

        # 150 ms delay for slow motion
        key = cv2.waitKey(150) & 0xFF

        # Press Q to stop
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


# ==========================================================
# INPUT VIDEO PATH
# ==========================================================

video_path = r"C:\Users\ARCHANA\Downloads\another_sample_input.mp4"

# Run the function
play_video_reverse_slow(video_path)
