import cv2 as cv
import numpy as np

# Resmi okuma
img = cv.imread("p1.png")
cv.imshow("Asil Goruntu", img)

# Kırmızı renk için sınırları belirleme ve numpy arraylere dönüştürme (225-255)
boundary = [[0, 0, 225], [255, 255, 255]]
# 225 değeri istenilen çıktıyı verdiği için keyfi olarak verilmiştir, 
# daha büyük ve küçük değerler de aynı çıktıyı verebilir.
boundary[0] = np.array(boundary[0], dtype= "uint8") 
boundary[1] = np.array(boundary[1], dtype= "uint8")

# Sınırlar arasındaki renk değerleri için mask oluşturma 
mask = cv.inRange(img, boundary[0], boundary[1])

# And ile sadece kırmızı şekilleri seçme
new_img = cv.bitwise_and(img, img, mask=mask)

# Siyah olmayan bölgeleri beyaz renk yapma
new_img[np.where((new_img>[0, 0, 0]).all(axis=2))] = [255,255,255]

# Yeni görüntüyü gösterme
cv.imshow("Yeni Goruntu", new_img)

cv.waitKey(0)

