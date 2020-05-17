import cv2 as cv
import numpy as np

# My fucntions
import my_functions

source = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels_2'
directory=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\all_cropped'
c = 0
frame_BGR_original = my_functions.load_images_from_source(source, 3)
while 1:

    frame_BGR_resized = my_functions.resize_image(frame_BGR_original[c], 10)

    cv.imshow("blur", frame_BGR_resized)
    cv.waitKey()
    cv.destroyAllWindows()

    frame_GRAY = cv.cvtColor(frame_BGR_resized, cv.COLOR_BGR2GRAY)
    frame_GRAY_blured=cv.GaussianBlur(frame_GRAY,(5,5),0)
    th=cv.adaptiveThreshold(frame_GRAY_blured, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11 ,2)





    GRAY_corners = cv.goodFeaturesToTrack(frame_GRAY, 100, 0.4, 5)
    corners_array = np.int0(GRAY_corners)


    #Display the corners found int he image 

    for i in corners_array:
        x, y = i.ravel()
        cv.circle(frame_BGR_resized, (x, y), 3, [255, 255, 0], -1)



    #frame_GRAY_cropped = my_functions.crop_image(frame_GRAY, corners_array)
    frame_BGR_cropped= my_functions.crop_image(frame_BGR_resized,corners_array)

    cv.imshow("cropped", frame_BGR_cropped)
    cv.waitKey()
    cv.destroyAllWindows()

    #my_functions.open_in_location(frame_BGR_resized, "corners" + str(c + 1), -445, -190)
    #my_functions.open_in_location(frame_BGR_original[c], "cropped" + str(c + 1), -739, -190)
    #my_functions.classify(frame_BGR_original[c])
    #my_functions.segment_the_image(my_functions.resize_image(frame_BGR_resized,1000),4 )
    #cv.waitKey()
    #cv.destroyAllWindows()
    c = c + 1



