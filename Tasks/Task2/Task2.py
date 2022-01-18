import cv2 as cv
import numpy as np

# BERAT DALSUNA

video = cv.VideoCapture("Örnek Video.mp4")

boundary = [[0, 0, 225], [255, 255, 255]]
boundary[0] = np.array(boundary[0], dtype= "uint8") 
boundary[1] = np.array(boundary[1], dtype= "uint8")
coordinates = []
COLUMN_COUNT = 10
X_LENGTH = 0
COLUMN_PIXEL = 0

while True:

    isTrue, frame = video.read()

    if isTrue:

        for i in range(1,COLUMN_COUNT):
           frame = cv.line(frame, (COLUMN_PIXEL*i,0), (COLUMN_PIXEL*i, X_LENGTH), (0,0,0), 1)

        if COLUMN_PIXEL == 0:
            X_LENGTH = frame.shape[1]
            COLUMN_PIXEL = X_LENGTH // COLUMN_COUNT

        mask = cv.inRange(frame, boundary[0], boundary[1])
        new_img = cv.bitwise_and(frame, frame, mask=mask)

        points = np.where((new_img>[0, 0, 0]).all(axis=2))
        try:
            coordinates.append(points[1][0])
        except:
            pass

        cv.imshow('Ornek Video',frame)

        if cv.waitKey(20) & 0XFF==ord('d'):
            break

    else: break

x = sum(coordinates) / len(coordinates)
count = 1

for i in range(0, X_LENGTH, COLUMN_PIXEL):
    if x < i + COLUMN_PIXEL:
        break
    else: 
        count += 1

print("Kare {}. sütunda tespit edildi.".format(count))