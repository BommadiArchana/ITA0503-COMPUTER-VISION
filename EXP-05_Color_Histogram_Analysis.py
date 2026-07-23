import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\ARCHANA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-21 114931.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create figure
plt.figure(figsize=(8,6))

# Display image
plt.subplot(2,1,1)
plt.imshow(img)
plt.title("Input Image")
plt.axis("off")

# Display histogram
plt.subplot(2,1,2)

colors = ('r', 'g', 'b')
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=color)

plt.title("Color Histogram Analysis")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0,256])

plt.tight_layout()
plt.show()
