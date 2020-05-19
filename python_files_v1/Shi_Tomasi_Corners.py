import cv2 as cv
import numpy as np
import cv2 as cv
import numpy as np
# My fucntions
import my_functions


number_of_images_in_source = 10
source = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels_3'
directory = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\all_cropped'
frame_BGR_original = my_functions.load_images_from_source(source, number_of_images_in_source - 1)


for c in range(number_of_images_in_source):

    frame_BGR_resized = my_functions.resize_image(frame_BGR_original[c], 10)
    frame_BGR_resized_2=frame_BGR_resized
    my_functions.open_in_location(frame_BGR_resized, "Original Frame Scaled", 0, 10)

    frame_GRAY = cv.cvtColor(frame_BGR_resized, cv.COLOR_BGR2GRAY)
    frame_GRAY_blured=cv.GaussianBlur(frame_GRAY,(5,5),0)

    GRAY_corners = cv.goodFeaturesToTrack(frame_GRAY, 100, 0.4, 5)
    corners_array = np.int0(GRAY_corners)


    #Display the corners found int he image

    for i in corners_array:
        x, y = i.ravel()
        cv.circle(frame_BGR_resized_2, (x, y), 3, [255, 255, 0], -1)



    #frame_GRAY_cropped = my_functions.crop_image(frame_GRAY, corners_array)
    frame_BGR_cropped= my_functions.crop_image(frame_BGR_resized,corners_array)


    my_functions.open_in_location(frame_BGR_resized_2, "Shi Tomasi Corners", 400, 10)
    my_functions.open_in_location(frame_BGR_cropped, "Original Frame Cropped", 800, 10)

    cv.waitKey()
    cv.destroyAllWindows()







