'''
*****************************************************************************************
*
*                       ===============================================
*                       Nirikshak Bot (NB) Theme (eYRC 2020-21)
*                       ===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:                      [NB_549]
# Author List:          [Sameer Karoshi,Nikita Salunkhe,Kunal Gaikwad,Varad Dhat]
# Filename:                     task_1a_part1.py
# Functions:            scan_image
#                                       [ Comma separated list of functions in this file ]
# Global variables:     shapes , list_1
#                                       [ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}
j = 0
list_1 = []
################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def scan_image(img_file_path):
    

    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :           [ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    #cv2.imshow("Img",img_file_path)
    #cv2.imwrite("Ball.png",img_file_path)
    #cv2.waitKey(0)
    
    

    global shapes
    global j

    shapes = {}


    global list_1

    list_1 = []
    

    ##############      ADD YOUR CODE HERE      ##############
    # Reading image
    #img = cv2.imread(img_file_path)
    # Convering to gray
    gray_image = cv2.cvtColor(img_file_path,cv2.COLOR_BGR2GRAY)
    #Defining threshold
    _, threshold = cv2.threshold(gray_image,200,255,cv2.THRESH_BINARY)
    #cv2.imshow("Threshold",threshold)
    #cv2.waitKey(0)
    # Finding contours values
    contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Getting image's height and width in pixels
    height,width =  gray_image.shape
    #print(height)
    #print(width)

    #Defining i = 0 as we have to draw contours it draws one extra rectangle to the border of the image

    approx_list = []
    LIST = []
    i = 0
    k = 0
    #print(len(contours))
    for cnt in contours:


        #print(len(contours))



        #perimeter = cv2.arcLength(cnt,True)
        #print("Perimeter :" ,perimeter)

    
        i = i + 1
        #Applying approx method
        approx = cv2.approxPolyDP(cnt, 0.005*cv2.arcLength(cnt, True),True)
        #print(len(approx))

        

        if(len(approx)>13 and len(approx) < 32):
            approx_list.append(len(approx))
            #print(len(approx))

        #print(len(approx))
    
        # Getting bounding rectnagle (Width height)
        (x, y, w, h) = cv2.boundingRect(approx)
        #print("Approx",len(approx))
    

    
        # Here we get rectangle
        cv2.rectangle(img_file_path,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.imshow('cutted contour',colored_image[y:y+h,x:x+w])
        # printing average colour inside contours
        #print('Average color (BGR): ',np.array(cv2.mean(colored_image[y:y+h,x:x+w])).astype(np.uint8))

        # Calculating colour inside the contours
        '''colour = None
        colour_of_shape = np.array(cv2.mean(img_file_path[y:y+h,x:x+w])).astype(np.uint8)
        #print(colour_of_shape)
        if(colour_of_shape[0] > colour_of_shape[1]):
            if(colour_of_shape[0] > colour_of_shape[2]):
                colour = "blue"
        elif(colour_of_shape[1] > colour_of_shape[2]):
            colour = "green"
        else:
            colour = "red" '''

       

        # Calculatingaspect ratio
        ar = w / float(h)

        # Draw contors
        cv2.drawContours(gray_image, [cnt],0,(0),5)
        #img[0:20,:] = 255
        #img[:,0:20] = 255
        #img[:,width-20:width] = 255
        #img[height-20:height,:] = 255

        # Calculating centroid
        M = cv2.moments(cnt)
        #print(M['m00'])

        

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #print(cx)
        #print(cy)
        colour = None

        pixel_val = img_file_path[cy,cx]
        #print(pixel_val)
        if(pixel_val[0] == 255):
            colour = "blue"
        elif(pixel_val[1] == 255):
            colour = "green"
        elif(pixel_val[2] == 255):
            colour = "red"



        #intensity = colored_image[cx,cy]
        #print("Intensity:",intensity)

        
        
        # Calculating detected shapes area
        area = cv2.contourArea(cnt)
        #print(area)

        #print(len(approx))

        #x1=int(cv2.GetSpatialMoment(moments1,1,0)/area)
        #y1=int(cv2.GetSpatialMoment(moments1,0,1)/area)
        #cv2.Circle(gray_image,(x1,y1),2,(0,255,0),20)

        gray_image = cv2.circle(gray_image,(cx,cy),1,(255,255,255),2)
        #cv2.imwrite("Centre_" + str(j) + ".png",gray_image)
        cv2.waitKey(0)

        j = j + 1

        #leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
        #rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
        #topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
        #bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])


   


        # if else conditions if len(approx) is 4 then it's 4 sided shape if 3 then triangle like that 


          
        if(i > 1):
            if(len(approx) == 4):

                #Defining extreme points for four sided shapes like top_left,bottom_right,top_right,bottom_left
                
                left = tuple(cnt[cnt[:, :, 0].argmin()][0])
                right = tuple(cnt[cnt[:, :, 0].argmax()][0])
                top = tuple(cnt[cnt[:, :, 1].argmin()][0])
                bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])


                # Draw contours and draw circles on extreme points


                cv2.drawContours(gray_image, [cnt], -1, (36, 255, 12), 2)
                cv2.circle(gray_image, left, 8, (0, 50, 255), -1)
                cv2.circle(gray_image, right, 8, (0, 255, 255), -1)
                cv2.circle(gray_image, top, 8, (255, 50, 0), -1)
                cv2.circle(gray_image, bottom, 8, (255, 255, 0), -1)

                # Calculating length between extreme points so we get lengths of edges of that shapes

                L1 = (int)(((left[0]-top[0])**2 + (left[1]-top[1])**2)**0.5)
                L2 = (int)(((top[0]-right[0])**2 + (top[1]-right[1])**2)**0.5)
                L3 = (int)(((right[0]-bottom[0])**2 + (right[1]-bottom[1])**2)**0.5)
                L4 = (int)(((bottom[0]-left[0])**2 + (bottom[1]-left[1])**2)**0.5)


                #print("width",w)
                #print("height",h)
                #print(L1,L2,L3,L4)
                #print(slope1,slope2,slope3,slope4)

                if (ar >= 0.95 and ar <= 1.05):
                    #print("square")
                    #intensity = colored_image[cx+20,cy]
                    #print("Square Int:",intensity)
                    #print("Squ")
                    #print(w)
                    #print(h)
                    #print("Peri",perimeter)
                    shapes.update(Square =[colour,area,cx,cy])
                    #print(shapes)
                elif(w != h and ((left[0]-top[0]) != 0 or 1 or -1) and (L1 != L2 != L3 != L4)):
                    #print("rectangle")
                    #print("REc")
                    #print(w)
                    #print(h)
                    #print("Peri",perimeter)
                    shapes.update(Quadrilateral =[colour,area,cx,cy])
                    #print(shapes)
                    #print("Left",left)
                    #print("Right",right)
                    #print("top",top)
                    #print("Bottom",bottom)
                    #cv2.imshow("CNT",cnt)
                    #print("Lenghts")
                    #print(L1,L2,L3,L4)
                    #print("slopes")
                    #print(slope1,slope2,slope3,slope4)


                
                elif(((left[0]-top[0])and(right[0]-bottom[0]))!= 0):
                    slope1 = round((left[1]-top[1])/(left[0]-top[0]),1)
                    slope2 = round((top[1]-right[1])/(top[0]-right[0]),1)
                    slope3 = round((right[1]-bottom[1])/(right[0]-bottom[0]),1)
                    slope4 = round((bottom[1]-left[1])/(bottom[0]-left[0]),1)

                    #angle1 = np.arctan(slope1)
                    #print(angle1)
                
                    

                    #print(L1,L2,L3,L4)
                    #print(slope1,slope2,slope3,slope4)

                    if(((L1 == L2 == L3 == L4)) or (slope1 == slope3 and slope2 == slope4)):
                        shapes.update(Rhombus =[colour,area,cx,cy])
                    elif((L1 == L3) and (L2 == L4) and (slope1 == slope3) and (slope2 == slope4)):
                        shapes.update(Parallelogram =[colour,area,cx,cy])
                    elif(((L1 != L3) and (L2 != L4))):
                         shapes.update(Trapezium =[colour,area,cx,cy])
                    else:
                        shapes.update(Quadrilateral =[colour,area,cx,cy])




        #Counting number of circles :

        
                        
                


        
        if(len(approx) == 3):
            #print("triangle")
            shapes.update(Triangle =[colour,area,cx,cy])
            #print(shapes)
            #print("Tri")
            #print(w)
            #print(h)
            #print("Peri",perimeter)

                 
        if(len(approx) == 5):
            #print("Pentagon")
            shapes.update(Pentagon =[colour,area,cx,cy])
            #print("Pen")
            #print(w)
            #print(h)
            #print("Peri",perimeter)
            #print(shapes)
        if(len(approx) == 6 or len(approx) == 7 or len(approx) == 8):
            #print("Pentagon")
            shapes.update(Hexagon =[colour,area,cx,cy])
            #print("Hex")
            #print(w)
            #print(h)
            #print("Peri",perimeter)
            #print(shapes)
        
        if(len(approx) == 16 or len(approx) == 15 or (len(approx) < 32 and len(approx) > 14) ):
            #print("Circle")
            #intensity = colored_image[cx,cy+20]
            #print("Circle Int:",intensity)




        

           

            if(len(contours)==2):
                FinalList = []
                FinalList.append(colour)
                FinalList.append(cx)
                FinalList.append(cy)

                #LIST.append(FinalList)

                #LIST.sort()

                shapes.update({'Circle':FinalList})
                # print(shapes)

            else:
                FinalList = []
                FinalList.append(colour)
                FinalList.append(cx)
                FinalList.append(cy)

                LIST.append(FinalList)

                LIST.sort()

                shapes.update({'Circle':LIST})
                #print(shapes)

            
            


                





            
                    
                    
                
                
                
                

            '''list_new = []
            list1 = []
            list2 = []
            
            if(len(approx_list) == 1):
                
                list1.append(colour)
                list1.append(cx)
                list1.append(cy)
                list_new.append(list1)
                
                #shapes.update(Circle =[colour,cx,cy])

            if(len(approx_list) > 1):
                
                list2.append(colour)
                list2.append(cx)
                list2.append(cy)
                list_new.append(list2)
                #shapes['Circle'].extend([[colour,cx,cy]])

            
            #list_new.append(list1)
            #list_new.append(list2)

            list_new.sort()

            shapes.update({'Circle':list_new})
            '''
            
            
            #print("Cir")
            #print(w)
            #print(h)
            #print("Peri",perimeter)
            #print(shapes)


        #Sorting of elements
        #sort_orders = {}
        

        
        

    #print(shapes)

        ##################################################
    #sort_orders = sorted(shapes.items(),key = lambda x:x[1][1],reverse = True)
    #shapes = dict()
    return shapes


# NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
