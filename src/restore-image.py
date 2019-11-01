import cv2

def create_mask(src):
  # convert image to grayscale
  mask = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  # only use values above a given threshold
  (_, mask) = cv2.threshold(mask, 210, 255, cv2.THRESH_BINARY)
  # blur the mask
  mask = cv2.GaussianBlur(mask, (5, 5), 10)
  return mask

def restore_image(filename, radius=10):
  src = cv2.imread(filename + "-damaged.jpg")
  mask = create_mask(src)

  result = cv2.inpaint(src, mask, radius, cv2.INPAINT_NS)
  return result

def restore_and_save_result(filename):
  print("Restoring " + filename + "...")
  result = restore_image(filename)
  cv2.imwrite(filename + "-restored.jpg", result)
  print("Done.")

result1 = restore_and_save_result("sample01")
result2 = restore_and_save_result("sample02")
result3 = restore_and_save_result("sample03")
result4 = restore_and_save_result("sample04")
