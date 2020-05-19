import os
import cv2 as cv
import numpy as np

def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt
#my functions

def open_in_location(img,winname,x,y):
    cv.namedWindow(winname)        # Create a named window
    cv.moveWindow(winname, x,y)  # Move it to (40,30)
    if (int(img.shape[1])<=0) or (int(img.shape[0])<=0):
        print("error: no size")
    else:
        #print("shape",img.shape[1],img.shape[0])
        cv.imshow(winname, img)

def resize_image(img,scale_percent):
    #print('Original Dimensions : ' + str(img_num), img.shape)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    interpolation = cv.INTER_AREA
    img = cv.resize(img, dim, interpolation)
    #print('Original Dimensions : ' + str(img_num), img.shape)
    return img

#funcitons from the internet

def load_images_from_source(folder,num_of_imgs):
    images = []
    i=0
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename),1)
        if img is not None:
            images.append(img)
        if i==num_of_imgs:
            break
        i=i+1
    return images

def get_contour_max_area(contours):
    area=0
    max_area=0
    second_max=0
    count=0
    second_counter  =0
    for c in range(len(contours)):
        area=cv.contourArea(contours[c])
        if area>max_area:
            #print("area", area)
            second_counter=count
            second_max=max_area
            max_area=area
            count=c
            #print(count)
    max=[count,max_area,second_counter,second_max]
    return max

def make_suqare_from_corners(square):
    smallest_x=square.item(0)
    smallest_y=square.item(1)
    max_x=square.item(0)
    max_y=square.item(1)
    for i in range(0,((len(square)*2)-1),2):
        x=square.item(i)
        y=square.item(i+1)
        if x< smallest_x:
            smallest_x=x
        if y< smallest_y:
            smallest_y=y
        if x>max_x:
            max_x=x
        if y>max_y:
            max_y=y

    p1 = [smallest_x, smallest_y]
    p2 = [max_x     , smallest_y]
    p3 = [smallest_x, max_y     ]
    p4 = [max_x     , max_y     ]

    square_points=[p1,p2,p3,p4]
    return  square_points

def hough_square_parallel_only(lines):
    x_parallel_lines=[0]
    y_parallel_lines=[0]

    c=0

    for i in range(0,((len(lines)*4)-1),4):
        x1=lines.item(i)
        y1=lines.item(i+1)
        x2 = lines.item(i+2)
        y2 = lines.item(i+3)
        line=[x1,y1,x2,y2]
        if x1==x2:
            y_parallel_lines.append(line)
        if y1==y2:
            x_parallel_lines.append(line)
        c=c+1

    print("x's are",x_parallel_lines)
    print("y's are",y_parallel_lines)
    max_x = 0
    max_y = 0

    min_y=x_parallel_lines[1][0]
    min_x=y_parallel_lines[1][0]

    for j in range(1,len(x_parallel_lines),1):
        #print(j)
        x_temp1 = x_parallel_lines[j][0]
        x_temp2 = x_parallel_lines[j][2]

        #print(" x1_temp=",x_temp1," x2_temp=",x_temp2)

        if x_temp1<min_x:
            min_x=x_temp1
        if x_temp1>max_x:
            max_x=x_temp1
        if x_temp2 < min_x:
            min_x = x_temp2
        if x_temp2 > max_x:
            max_x = x_temp2
    #print(" x_max=", max_x, " x_min=", min_x)

    for k in range(1, len(y_parallel_lines), 1):
        #print(k)
        y_temp1 = y_parallel_lines[k][1]
        y_temp2 = y_parallel_lines[k][3]

        #print(" y1_temp=", y_temp1, " y2_temp=", y_temp2)

        if y_temp1 < min_y:
            min_y = y_temp1
        if y_temp1 > max_y:
            max_y = y_temp1
        if y_temp2 < min_y:
            min_y = y_temp2
        if y_temp2 > max_y:
            max_y = y_temp2
    #print(" y_max=", max_y, " y_min=", min_y)

    coordinates=[min_x,min_y,max_x,max_y]
    #print("coordinates",coordinates)
    return coordinates


def hough_square_absolute_maximum(lines):

    min_x = lines.item(0)
    min_y = lines.item(1)
    max_x = 0
    max_y = 0

    for i in range(0, ((len(lines) * 4) - 1), 4):
        x1 = lines.item(i)
        y1 = lines.item(i + 1)
        x2 = lines.item(i + 2)
        y2 = lines.item(i + 3)

        #print(" x1",x1," x2",x2," y1",y1," y2",y2)

        if x1 < min_x:
            min_x = x1
        if x1 > max_x:
            max_x = x1
        if x2 < min_x:
            min_x = x2
        if x2 > max_x:
            max_x = x2
        if y1 < min_y:
            min_y = y1
        if y1 > max_y:
            max_y = y1
        if y2 < min_y:
            min_y = y2
        if y2 > max_y:
            max_y = y2


    coordinates = [min_x, min_y, max_x, max_y]
    #print("coordinates",coordinates)
    return coordinates

def find_large_corners(corners):
    max

    for i in range(0,((len(corners)*2)-1),2):
        x=corners.item(i)
        y=corners.item(i+1)
        if x< smallest_x:
            smallest_x=x
        if y< smallest_y:
            smallest_y=y
        if x>max_x:
            max_x=x
        if y>max_y:
            max_y=y



def segment_the_image(img, g_tolerance):
    coun=counter()
    squares=[None]*64
    width=img.shape[0]
    lenght=img.shape[1]
    int1=((width / 8))
    int2=((lenght / 8))
    #print("w , l =",int1,int2)
    #print("w= ",width,"l= ",lenght)
    colums = [0, 1 , 2 ,3,4,5,6,7]

    line_location_c = 0
    last_line_location_c = 0
    for i in range(8):
        tolerance=int(((i+1)*0.5))
        line_location_c=line_location_c+(width/8)
        if i==0:
            colums[i] = img[0:lenght, int(last_line_location_c):int(line_location_c) + tolerance]
        else:
            colums[i]=img[0:lenght,int(last_line_location_c)-tolerance:int(line_location_c )+ tolerance]
            #open_in_location(colums[i],"row "+str(i),-913+(50*i),232)
        last_line_location_c = line_location_c
        
        line_location=0
        last_line_location=0
        for j in range(8):
            tolerance = int(((j + 1) * 0.5))
            line_location=line_location+(lenght / 8)
            square_number=(8*i)+j
            #print("L L , s L ",int(line_location), (last_line_location))
            colum = colums[i]
            if j == 0:
                squares[square_number] = colum[int(last_line_location) : int(line_location) +tolerance ,0:width]
            if j > 3:
                if j==7:
                    squares[square_number] = colum[int(last_line_location)+8: int(line_location) + tolerance+10, 0:width]
                else:
                    squares[square_number] = colum[int(last_line_location)+8: int(line_location) + tolerance+2, 0:width]
            else:
                squares[square_number] = colum[int(last_line_location)+ tolerance : int(line_location) + tolerance ,0:width]
            last_line_location=line_location
            #open_in_location(squares[square_number], "row " + str(i)+" square"+str(j), -1358 + (70 * i), -185 + (70 * j))
            file_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\squares'
            if  np.sum(squares[square_number]) == 0:
                  continue
            cv.imwrite(file_path + "/suqare_" + str(coun)+"_"+str(i) + "_" + str(j) + ".PNG", squares[square_number])
    #return  squares





def crop_image(img, corners):
    square_points=make_suqare_from_corners(corners)
    min_x=square_points[0][0]
    min_y=square_points[0][1]
    max_x=square_points[3][0]
    max_y=square_points[3][1]

    cropped_img=img[min_y:max_y,min_x:max_x]
    return cropped_img


def classify(img):
    squares=segment_the_image(img,4)
    king_white_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_king'
    king_black_path = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_king'

    queen_white_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_queen'
    queen_black_path = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_queen'

    bishop_white_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_bishop'
    bishop_black_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_bishop'

    knight_white_path = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_knight'
    knight_black_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_knight'

    rook_white_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_rook'
    rook_black_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_rook'

    pawn_white_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_pawn'
    pawn_black_path=r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_pawn'

    empty_black_path = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\black_empty'
    empty_white_path = r'D:\learning\Semesters\Semester 8\Image_Processing\Project\Data_set\white_empty'

    for i in range(64):
        cv.destroyAllWindows()
        img=squares[i]

        image_num=counter()

        open_in_location(resize_image(img,300),"img",-851,-53)
        cv.waitKey(10)
        classification = input("what piece is this")



        if classification=="wk":
            print("White King")
            cv.imwrite(king_white_path+"/white_king_"+str(image_num)+"_"+str(i)+".PNG",squares[i])
            continue
        if classification=="bk":
            print("Black King")
            cv.imwrite(king_black_path+"/black_king_"+str(image_num)+"_"+str(i)+".PNG",squares[i])
            continue
        if classification=="wq":
            print("White queen")
            cv.imwrite(queen_white_path+"/white_queen_"+str(image_num)+"_"+str(i)+".PNG",squares[i])
            continue
        if classification=="bk":
            print("Black queen")
            cv.imwrite(queen_black_path+"/black_queen_"+str(image_num)+"_"+str(i)+".PNG",squares[i])
            continue
        if classification == "wb":
            print("White bishop")
            cv.imwrite(bishop_white_path + "/white_bishop_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "bb":
            print("Black bishop")
            cv.imwrite(bishop_black_path + "/black_bishop_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "wkn":
            print("White knight")
            cv.imwrite(knight_white_path + "/white_knight_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "bkn":
            print("Black knight")
            cv.imwrite(knight_black_path + "/black_knight_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "wr":
            print("White rook")
            cv.imwrite(rook_white_path + "/white_rook_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "br":
            print("Black rook")
            cv.imwrite(rook_black_path + "/black_rook_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "wp":
            print("White pawn")
            cv.imwrite(pawn_white_path + "/white_pawn_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "bp":
            print("Black pawn")
            cv.imwrite(pawn_black_path + "/black_pawn_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "we":
            print("White empty")
            cv.imwrite(empty_white_path + "/white_empty_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        if classification == "be":
            print("Black empty")
            cv.imwrite(empty_black_path + "/black_empty_" + str(image_num) + "_" + str(i) + ".PNG", squares[i])
            continue
        


