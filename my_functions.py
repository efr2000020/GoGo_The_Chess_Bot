import os
import cv2 as cv


#my functions

def open_in_location(winname,x,y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x,y)  # Move it to (40,30)
    cv.imshow(winname, img)

def resize_image(img,scale_percent):
    print('Original Dimensions : ' + str(i), img.shape)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    interpolation = cv.INTER_AREA
    img = cv.resize(img, dim, interpolation)
    print('Original Dimensions : ' + str(i), img.shape)
    return img

#funcitons from the internet

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename),0)
        if img is not None:
            images.append(img)
    return images