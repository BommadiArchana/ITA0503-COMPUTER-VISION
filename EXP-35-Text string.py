import numpy as np
import cv2

def add_text_to_image(image_size, text):
    # Extract height and width
    height, width = image_size

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (0, 0, 255)  # Red (BGR)

    # Get text size
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    # Calculate text position (centered)
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    # Draw text on the image
    cv2.putText(
        image,
        text,
        (text_x, text_y),
        font,
        font_scale,
        text_color,
        font_thickness
    )

    # Display the image
    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main Program
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))
user_text = input("Enter the text to display: ")

add_text_to_image((user_height, user_width), user_text)
