import cv2
import pytesseract

# ==========================================================
# TESSERACT OCR LOCATION
# ==========================================================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ==========================================================
# EXTRACT TEXT FROM VIDEO
# ==========================================================
def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ERROR: Video cannot be opened!")
        print("Check the video path.")
        return

    print("Video opened successfully!")
    print("Press Q to stop the video.")

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Video finished.")
            break

        frame_count += 1

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize frame for better OCR
        gray = cv2.resize(gray, None, fx=1.5, fy=1.5)

        # Extract text using Tesseract
        text = pytesseract.image_to_string(
            gray,
            config="--psm 6"
        )

        # Display detected text
        if text.strip():
            print("\nDetected Text:")
            print(text.strip())

        # Display video
        cv2.imshow("Text Extraction from Video", frame)

        # Press Q to stop
        if cv2.waitKey(30) & 0xFF == ord('q'):
            print("Stopped by user.")
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Total frames processed:", frame_count)


# ==========================================================
# INPUT VIDEO PATH
# ==========================================================
extract_text_from_video(
    r"C:\Users\ARCHANA\Downloads\sample video.mp4"
)
