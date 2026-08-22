import cv2

# GIVE YOUR VIDEO PATH HERE
cap = cv2.VideoCapture(
    r"C:\Users\ARCHANA\Downloads\sample video.mp4"
)

# Check video
if not cap.isOpened():
    print("Video not found! Check the path.")
else:

    # Create background detector
    detector = cv2.createBackgroundSubtractorMOG2(
        history=100,
        varThreshold=40
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Detect moving objects
        mask = detector.apply(frame)

        # Remove noise
        _, mask = cv2.threshold(
            mask,
            200,
            255,
            cv2.THRESH_BINARY
        )

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Detect vehicles
        for contour in contours:

            if cv2.contourArea(contour) > 1000:

                x, y, w, h = cv2.boundingRect(contour)

                # Draw box
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Add label
                cv2.putText(
                    frame,
                    "Vehicle",
                    (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        # Show video
        cv2.imshow("Vehicle Detection", frame)

        # Press Q to stop
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
