import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read image
img = cv2.imread("./pictures/1.jpg")

# Using Matplotlib to display image

plt.imshow(img)
plt.show()

# cau 2: chuyen thanh mau xam va hien thi
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img1)
plt.show()
# cau 3: Adjust brightness
# increate brightness
new_img = img.astype(np.float32) + 50
new_img = np.clip(new_img, 0, 255)
new_img = new_img.astype(np.uint8)
plt.imshow(new_img)
plt.show()
# decreate brightness
new_img = img.astype(np.float32) - 80
new_img = np.clip(new_img, 0, 255)
new_img = new_img.astype(np.uint8)
plt.imshow(new_img)
plt.title('Giảm độ sáng')
plt.show()
# crop image
height, width, _ = img.shape
left = 0
top = 0
cropped_image = img[left:left+100, top:top+100]

plt.imshow(cropped_image)
plt.title('Góc nhỏ của ảnh đã cắt')
plt.show()
