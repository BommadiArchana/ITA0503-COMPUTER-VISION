import cv2
import numpy as np

def subtract_foreground(image_path, lower_color, upper_color):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper HSV range for the foreground color
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create mask for the foreground
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert the mask to keep only the background
    background_mask = cv2.bitwise_not(mask)

    # Extract the background
    background = cv2.bitwise_and(image, image, mask=background_mask)

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Subtracted Image (Only Background)", background)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-08-01 144401.png"   # Replace with your image path

# HSV range for the foreground color (adjust as needed)
lower_color = [0, 50, 50]
upper_color = [120, 255, 255]

subtract_foreground(image_path, lower_color, upper_color)
