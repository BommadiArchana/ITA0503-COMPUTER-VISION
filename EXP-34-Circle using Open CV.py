import numpy as np
import cv2


def create_circle_image(image_size):
    # Extract height and width
    height, width = image_size

    # Create a white RGB image
    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    # Define circle properties
    center = (
        width // 2,
        height // 2
    )

    radius = min(width, height) // 4

    # Draw a red circle
    # OpenCV uses BGR format, so (0, 0, 255) = Red
    cv2.circle(
        image,
        center,
        radius,
        (0, 0, 255),
        2
    )

    # Display the image
    cv2.imshow("Circle Image", image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()


# ==========================================================
# GET IMAGE SIZE FROM USER
# ==========================================================

user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))

# Create circle image
create_circle_image(
    (user_height, user_width)
)
