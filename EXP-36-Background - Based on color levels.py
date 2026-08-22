import cv2
import numpy as np

def subtract_background(image_path, lower_color, upper_color):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper HSV range for background color
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask for the background
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert the mask to keep the foreground
    mask_inv = cv2.bitwise_not(mask)

    # Extract the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask_inv)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted Image", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-08-01 144401.png"   # Replace with your image path

# HSV color range for the background (adjust as needed)
lower_color = [30, 30, 30]
upper_color = [255, 255, 255]

subtract_background(image_path, lower_color, upper_color)
