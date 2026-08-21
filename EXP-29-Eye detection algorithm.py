import cv2

def detect_eyes(image_path):
    # Load pre-trained Haar cascades
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye.xml"
    )

    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("ERROR: Image not found!")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Detect eyes inside each detected face
    for (x, y, w, h) in faces:

        face_roi_gray = gray[y:y+h, x:x+w]
        face_roi_color = image[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_roi_gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(15, 15)
        )

        # Draw rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                face_roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (255, 0, 0),
                2
            )

    # Display output
    cv2.imshow("Eye Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Input image path
detect_eyes(
    r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-08-13 095609.png"
)
