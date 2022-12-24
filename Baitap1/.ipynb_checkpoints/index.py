import opencv-python
image = cv2.imread('onion.png)')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh xam',gray)