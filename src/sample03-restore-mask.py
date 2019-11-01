import cv2

sample1 = cv2.imread("sample03-damaged.jpg")
mask1 = cv2.imread("sample03-mask.jpg")
mask1 = mask1[:, :, 0] # mask needs to be one channel only

radius = 10
result1 = cv2.inpaint(sample1, mask1, radius, cv2.INPAINT_TELEA)

cv2.imwrite("sample03-restored.jpg", result1)
