import cv2 as cv
import numpy as np
import cv2 as cv
import numpy as np
# My fucntions
import my_functions

camera=cv.VideoCapture(1)



while True:
    ret, frame_BGR_original=camera.read()
    frame_BGR_resized = my_functions.resize_image(frame_BGR_original, 100)
    frame_BGR_resized_2=frame_BGR_resized
    #my_functions.open_in_location(frame_BGR_resized, "Original Frame Scaled", 0, 10)


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


    my_functions.open_in_location(frame_BGR_resized_2, "Shi Tomasi Corners", 00, 10)
    my_functions.open_in_location(frame_BGR_cropped, "Original Frame Cropped", 800, 10)

    key=cv.waitKey(1) & 0xff
    if key == ord('q'):
        break


camera.release()
cv.destroyAllWindows()






