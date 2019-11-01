import cv2

# sample4 = cv2.imread("sample03-damaged.jpg")
sample4 = cv2.imread("sample04.jpg")
mask4 = cv2.cvtColor(sample4, cv2.COLOR_BGR2GRAY)
(_, mask4) = cv2.threshold(mask4, 210, 255, cv2.THRESH_BINARY)
mask4 = cv2.GaussianBlur(mask4, (5, 5), 10)

cv2.imwrite("sample04-mask.jpg", mask4)

radius = 20
result4 = cv2.inpaint(sample4, mask4, radius, cv2.INPAINT_NS)

cv2.imwrite("sample04-restored.jpg", result4)
