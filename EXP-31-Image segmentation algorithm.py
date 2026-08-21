import cv2

def segment_image(image_path, threshold_value=127):
    # Read the input image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Apply thresholding for segmentation
    _, segmented_image = cv2.threshold(
        image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # Display the original and segmented images
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
segment_image(r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-08-01 144401.png", 127)
