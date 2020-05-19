import cv2 as cv
import numpy as np
# My fucntions
import my_functions


upper_TH_level=180
lower_TH_level=150
number_of_images_in_source = 10
source = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels_3'
directory = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\all_cropped'
frame_BGR_original = my_functions.load_images_from_source(source, number_of_images_in_source - 1)


for c in range(number_of_images_in_source):

    frame_BGR_resized = my_functions.resize_image(frame_BGR_original[c], 10)
    frame_BGR_resized_2=frame_BGR_resized

    frame_GRAY = cv.cvtColor(frame_BGR_resized, cv.COLOR_BGR2GRAY)
    frame_canny= cv.Canny(frame_GRAY, lower_TH_level, upper_TH_level)

    lines = cv.HoughLinesP(frame_canny, 1, np.pi / 90, 80, minLineLength=100, maxLineGap=25)
    if lines is None:
        print("error, image has no lines")
        continue

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(frame_BGR_resized_2, (x1, y1), (x2, y2), (0, 255, 0), 2)

    Hough_points = my_functions.hough_square_absolute_maximum(lines)
    frame_BGR_Cropped = frame_BGR_resized[Hough_points[1]:Hough_points[3], Hough_points[0]:Hough_points[2]]



    # Displaying images except the original before resizing
    my_functions.open_in_location(frame_BGR_resized, "Original Frame Scaled", 0, 10)
    my_functions.open_in_location(frame_canny, "Canny Edge", 400, 10)
    my_functions.open_in_location(frame_BGR_resized_2, "Hough Lines", 800, 10)
    my_functions.open_in_location(frame_BGR_Cropped, "Original Frame Cropped", 1200, 10)

    cv.waitKey()
    cv.destroyAllWindows()


