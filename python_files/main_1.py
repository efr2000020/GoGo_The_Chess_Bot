import cv2 as cv
import numpy as np
import pause

#My fucntions
import my_functions


directory=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels_2'
imges= my_functions.load_images_from_source(directory,50)


for i in range(len(imges)):

    print("Chess_image_"+str(i+1))

    org =my_functions.resize_image(imges[i],10)
    org_2 = org
    img=cv.cvtColor(org,cv.COLOR_BGR2GRAY)
    my_functions.open_in_location(img,"Chess_image_"+str(i+1),-1347,-165)

    canny= cv.Canny(img, 80, 150)
    #canny_2=canny
    blur = cv.GaussianBlur(img, (5, 5), 3)
    thrsh = cv.adaptiveThreshold(blur, 255, 1, 1, 11,2)
    '''
    lines = cv.HoughLinesP(thrsh, 1, np.pi / 90, 220, minLineLength=200, maxLineGap=8)
    if lines is None:
        print("error, image has no lines")
        continue

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(org_2, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    hough_points = my_functions.hough_square_absolute_maximum(lines)
    print("hough", hough_points)
    cropped = org_2[hough_points[1]:hough_points[3], hough_points[0]:hough_points[2]]
    '''
    corners = cv.goodFeaturesToTrack(img, 100, .4, 5)

    corners = np.int0(corners)
    print("make square",my_functions.make_suqare_from_corners(corners))
    p1x = my_functions.make_suqare_from_corners(corners)[0][0]
    p1y = my_functions.make_suqare_from_corners(corners)[0][1]
    p2x = my_functions.make_suqare_from_corners(corners)[3][0]
    p2y = my_functions.make_suqare_from_corners(corners)[3][1]

    print("the cut corndrs are ",p1x,p1y,p2x,p2y)
    cornered=org_2[p1y:p2y,p1x:p2x]
    for i in corners:
        x, y = i.ravel()
        cv.circle(img, (x, y), 3, [255, 255, 0], -1)
    my_functions.open_in_location(img, "corners" + str(i + 1), -498, -157)

    my_functions.open_in_location(cornered, "cornerd" + str(i + 1), -1347, 182)
    #my_functions.open_in_location(thrsh,'thresh  '+str(i+1),-905,-165)

    my_functions.segment_the_image(cornered, 0)
    cv.waitKey()
    cv.destroyAllWindows()


