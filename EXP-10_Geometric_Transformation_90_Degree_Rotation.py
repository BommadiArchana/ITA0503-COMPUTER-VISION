import cv2 
# Load the image 
img = cv2.imread(r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-16 103733.png") 
# Rotate 90 degrees clockwise 
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 
# Display the rotated image 
cv2.imshow("Rotated Image", rotated_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
