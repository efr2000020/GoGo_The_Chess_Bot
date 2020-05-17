import cv2 as cv
import numpy as np
import pause

#My fucntions
import my_functions


directory=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Chess_board_sampels'
imges= my_functions.load_images_from_source(directory,2)


for i in range(len(imges)):

    print("Chess_image_"+str(i+1))

    org =my_functions.resize_image(imges[i],10)
    org_2 = org
    img=cv.cvtColor(org,cv.COLOR_BGR2GRAY)
    my_functions.open_in_location(img,"Chess_image_"+str(i+1),-1347,-165)

    canny= cv.Canny(img, 80, 150)
    #canny_2=canny
    blur = cv.GaussianBlur(img, (5, 5), 3)
    my_functions.open_in_location(blur,'Gaussian Blur '+str(i+1),-905,-165)


    thrsh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY , 11,2)
    #_, img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(thrsh, mode = cv.RETR_TREE, method = cv.CHAIN_APPROX_NONE)

    max = (my_functions.get_contour_max_area(contours))[0]
    if max==0:
        continue

    #second_max=(my_functions.get_contour_max_area(contours))[2]
    contoured_square=cv.approxPolyDP(contours[max], 0.05 * cv.arcLength(contours[max], True), True)
    points=my_functions.make_suqare_from_corners(contoured_square)

    #cv.drawContours(org, contours[max], -1, (255,0, 0), 3)
    square=cv.drawContours(org_2,contoured_square, -1, (255,0, 0), 4)
    #  cv.drawContours(org_2, hull, -1, (0,0,255), 5)

    '''
    pts_src = np.array([[76  ,56], [318 , 43],[316 , 42],[320 ,260]])
    pts_dst = np.array([[0.0, 0.0], [x, 0.0], [x, y], [0.0, y]])
    h, status = cv.findHomography(pts_src, pts_dst)
    '''
    p1=points[0]
    p2=points[1]
    p3=points[2]
    p4=points[3]

    lines = cv.HoughLinesP(thrsh, 1, np.pi / 90, 220, minLineLength=200, maxLineGap=8)
    if lines is None:
        print("error, image has no lines")
        continue

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(org_2, (x1, y1), (x2, y2), (0, 255, 0), 2)
    hough_points=my_functions.hough_square_absolute_maximum(lines)
    print("hough",hough_points)
    cropped=org_2[hough_points[1]:hough_points[3],hough_points[0]:hough_points[2]]
    
    #print("points ",points)
    width = int(cropped.shape[1] )
    height = int(cropped.shape[0])
    blur_cropped= blur[p1[1]:p3[1],p1[0]:p2[0]]
    thrsh_cropped=cv.adaptiveThreshold(blur_cropped, 255, 1, 1, 11,8)
    print("width= ",width,"hight",height)
    canny_cropped = cv.Canny(cropped, 150, 300)

    contours, hierarchy = cv.findContours(thrsh_cropped, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

    max = (my_functions.get_contour_max_area(contours))[0]
    if max == 0:
        continue

    contoured_square = cv.approxPolyDP(contours[max], 0.05 * cv.arcLength(contours[max], True), True)
    points = my_functions.make_suqare_from_corners(contoured_square)[0]

    # second_max=(my_functions.get_contour_max_area(contours))[2]
     '''
    corners = cv.goodFeaturesToTrack(org_2, 100, 0.01, 10)

    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv.circle(cropped, (x, y), 3, [255, 255, 0], -1)


    contoured_square = cv.approxPolyDP(contours[max], 0.05 * cv.arcLength(contours[max], True), True)
    points = my_functions.make_suqare_from_corners(contoured_square)
    square=cv.drawContours(cropped,contoured_square, -1, (255,0, 0), 1)

    my_functions.open_in_location(thrsh,'Thresholding'+str(i+1),-462,-165)
    my_functions.open_in_location(cropped, "Squared" + str(i + 1), -1347, 182)
    my_functions.open_in_location(canny_cropped, "canny Cropped" + str(i + 1), -905, 182)

    my_functions.open_in_location(cropped, "corners" + str(i + 1), -426, 182)
     '''

    cv.waitKey()
    cv.destroyAllWindows()
