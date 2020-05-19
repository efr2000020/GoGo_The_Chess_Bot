import cv2 as cv
import numpy as np
# My fucntions
import my_functions


THRESHOLDING_window=11
number_of_images_in_source = 5
source = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels_2'
directory = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\all_cropped'
frame_BGR_original = my_functions.load_images_from_source(source, number_of_images_in_source - 1)


for c in range(number_of_images_in_source):

    frame_BGR_resized = my_functions.resize_image(frame_BGR_original[c], 10)

    frame_GRAY = cv.cvtColor(frame_BGR_resized, cv.COLOR_BGR2GRAY)
    frame_GRAY_blured = cv.GaussianBlur(frame_GRAY, (5, 5), 0)
    frame_THRESHOLDED = cv.adaptiveThreshold(frame_GRAY_blured, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv.THRESH_BINARY_INV, THRESHOLDING_window, 2)

    contours, hierarchy = cv.findContours(frame_THRESHOLDED, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

    largest_contour_index = my_functions.get_contour_max_area(contours)[0]

    # only print if interested
    # print(largest_contour_index)

    if largest_contour_index == 0:
        continue

    largest_contoured_polygon = cv.approxPolyDP(contours[largest_contour_index],
                                                0.05 * cv.arcLength(contours[largest_contour_index], True), True)

    frame_BGR_cropped = my_functions.crop_image(frame_BGR_resized, largest_contoured_polygon)

    # Displaying images except the original before resizing
    my_functions.open_in_location(frame_BGR_resized, "Original Frame Scaled", 0, 10)
    my_functions.open_in_location(frame_GRAY_blured, "Gray Filtered Frame", 400, 10)
    my_functions.open_in_location(frame_THRESHOLDED, "Thresholded Frame", 800, 10)
    my_functions.open_in_location(frame_BGR_cropped, "Original Frame Cropped", 1200, 10)

    cv.waitKey()
    cv.destroyAllWindows()


