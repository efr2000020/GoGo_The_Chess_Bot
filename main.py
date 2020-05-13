import cv2 as cv
import pause

#My fucntions
import my_functions


directory=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels'
imges= my_functions.load_images_from_folder(directory)


for i in range(len(imges)):
    print("Chess_image_"+str(i+1))
    img =my_functions.resize_image(imges[i],10)

    my_functions.open_in_location("Chess_image_"+str(i+1),-1347,-165)

    img = cv.GaussianBlur(img, (5, 5), 0)
    my_functions.open_in_location('Gaussian Blur '+str(i+1),-905,-165)

    img = cv.adaptiveThreshold(img, 255, 1, 1, 11, 4)
    my_functions.open_in_location('Adabtive Thresholding '+str(i+1),-462,-165)

    cv.waitKey()
    cv.destroyAllWindows()