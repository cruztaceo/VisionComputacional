import numpy as np
import cv2 as cv

img = cv.imread('Actividades/Actividad_03/Sudoku_Small.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray_img, 50, 100)
cv.imshow('Canny', edges)
# cv.waitKey()

minLineLength = 700
maxLineGap = 13
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 25, minLineLength, maxLineGap)
print(lines.shape)
for i in range(lines.shape[0]):
    cv.line(img, (lines[i, 0, 0], lines[i, 0, 1]),
            (lines[i, 0, 2], lines[i, 0, 3]),
            (0, 0, 255), 2)

cv.imshow('Hough', img)
cv.waitKey()

cv.destroyAllWindows()
cv.imwrite('houghlines.jpg', img)
