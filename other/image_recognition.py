import cv2

# Загрузка изображения
image = cv2.imread('test_img.jpg')

# Преобразование изображения в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск контуров на изображении
contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Отображение контуров на изображении
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Отображение изображения с контурами
cv2.imshow('Image with Contours', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()