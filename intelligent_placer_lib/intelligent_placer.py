import os
import matplotlib.pyplot as plt
from pathlib import Path
import cv2
import numpy as np
import glob
import os

def FixSize(img):
    coefficient = 30/100
    width = int(img.shape[1] * coefficient)
    height = int(img.shape[0] * coefficient)
    dim = (width, height)
    newImg = cv2.resize(img, dim)
  
    return newImg

def FixEdge(img):
        kernel = np.ones((5, 5), np.uint8)
        imgNew = cv2.dilate(img, kernel, iterations=1)
        return imgNew

def fillhole(input_image):
    '''
    input gray binary image  get the filled image by floodfill method
    Note: only holes surrounded in the connected regions will be filled.
    :param input_image:
    :return:
    '''
    im_flood_fill = input_image.copy()
    h, w = input_image.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    im_flood_fill = im_flood_fill.astype("uint8")
    cv2.floodFill(im_flood_fill, mask, (0, 0), 255)
    im_flood_fill_inv = cv2.bitwise_not(im_flood_fill)
    img_out = input_image | im_flood_fill_inv
    
    return img_out 

def findPolyGon_Object(nameImage):
    image1 = cv2.imread(nameImage)
    image = FixSize(image1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3,3), 0)
    canny = cv2.Canny(blurred, 120, 255, 1)

    canny_New = FixEdge(canny)
    fill_hole_ima = fillhole(canny_New)

    '''f, ax = plt.subplots(2, 2, figsize=(10, 10))
    ax[0,0].set_title(f"Input")
    ax[0,1].set_title(f"Method Canna")
    ax[1, 0].set_title(f"Fill hole")
    ax[0,0].imshow(image,cmap="gray")
    ax[0,1].imshow(canny,cmap="gray")
    ax[1, 0].imshow(fill_hole_ima,cmap="gray")  '''
    #plt.savefig(f"output/result_{os.path.basename(nameImage)}")
    plt.close()
    return image , fill_hole_ima


def CheckPolygon_Object(image ,  fill_hole_ima):
    # tìm toạ độ các đường viền
    contours, hierarchy = cv2.findContours(fill_hole_ima, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img2 = image.copy()
    index = 0
    areas_orig = []
    areas_bboxes = []
    all_width = []
    all_height =[]
    ymax = 0
    for i,contour in enumerate(contours):
        # lấy toạ độ các vật thể với xleft, ytop, width,height
        x,y,w,h = cv2.boundingRect(contour)
        # loại bỏ các viền có diện tích nhở hơn 5 
        if cv2.contourArea(contour)<5:
            continue
        # lấy toàn bộ kích thước của các vật thể và hình
        all_width.append(w)
        all_height.append(h)
        # tìm toạ độ của hình
        if ymax == 0:
            ymax = y
        else:
            if y>ymax:
               ymax = y
               index = i
            

    all_width = np.array(all_width)
    all_height =np.array(all_height)
    # tìm vật thể có kích thước lớn nhất
    width_max = np.argmax(all_width)
    height_max = np.argmax(all_height)


    # kiểm tra xem vật thể có  kích thước lớn nhất đó có phải là hình hay không
    # đúng thì vật thể nằm, còn sai thì vật thể nằm ngoài
    if (width_max == index and height_max == index):#area_max==index and 
        if((2 *max(all_width) < sum(all_width)) and (2 * max(all_height) < sum(all_height))):
            return False
        else:
          return True
    else:
        return False 

def checkImage(strPathToImg):
    image ,  fill_hole_ima = findPolyGon_Object(strPathToImg)
    bool_Check = CheckPolygon_Object(image ,  fill_hole_ima)
    return bool_Check