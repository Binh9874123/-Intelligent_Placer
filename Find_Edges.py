import cv2
import numpy as np
from paint import paint


# Понизить размерность
def FixSize(img):
    coefficient = 30/100
    width = int(img.shape[1] * coefficient)
    height = int(img.shape[0] * coefficient)
    dim = (width, height)
    newImg = cv2.resize(img, dim)
    return newImg

# Сделать шумоподавление
def FixNoise(img):
    newImg = cv2.bilateralFilter(img, d=3, sigmaColor=10, sigmaSpace=10)
    return newImg


# Разширять границы, чтобы они стали толще
def FixEdge(imgEdge):
    kernel = np.ones((5, 5), np.uint8)
    imgThick = cv2.dilate(imgEdge, kernel, iterations=1)
    return imgThick

# Метод наводнение
def flood_method(img):
    newImg = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    startPoint = (0, 0)
    cv2.floodFill(newImg, mask, startPoint, 255)
    img1 = cv2.bitwise_not(newImg)
    return img1

