import cv2
import numpy as np
import matplotlib.pyplot as plt


def gauss_value(x, y, sigma):
    tempt = -(x**2+y**2)/(2*sigma**2)
    gauss = np.exp(tempt)/(2*np.pi*sigma**2)
    return gauss


def gaussian_kernel(size, sigma):
    if size % 2 == 0:
        size = size + 1

    max_point = size // 2  # both directions (x,y) maximum

    min_point = - max_point  # both directions (x,y) minimum

    K = np.zeros((size, size))  # kernel matrix
    for x in range(min_point, max_point + 1):
        for y in range(min_point, max_point + 1):
            value = gauss_value(x, y, sigma)
            K[x - min_point, y - min_point] = value

    return K


img = cv2.imread("./pictures/2.jpg", 0)
sigmas = [2.5, 5, 10]
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')
for i in range(len(sigmas)):
    kernel = gaussian_kernel(5, sigmas[i])
    img_gauss = cv2.filter2D(img, -1, kernel)
    ax[i+1].imshow(img_gauss)
    ax[i+1].set_title(f'Kernel = {sigmas[i]}')
    ax[i+1].axis('off')

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
