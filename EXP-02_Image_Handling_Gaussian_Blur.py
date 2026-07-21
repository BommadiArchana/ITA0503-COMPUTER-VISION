import cv2 
image = cv2.imread(r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-16 103733.png")  # Replace with your image file 
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)  # (15, 15) is the kernel size 
cv2.imshow("Original Image", image) 
cv2.imshow("Blurred Image", blurred_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
