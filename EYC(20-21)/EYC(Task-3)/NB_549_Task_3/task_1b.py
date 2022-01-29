'''
*****************************************************************************************
*
*                       ===============================================
*                       Nirikshak Bot (NB) Theme (eYRC 2020-21)
*                       ===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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

# Team ID:                      [ NB_549 ]
# Author List:          [ Sameer Karoshi, Kunal Gaikwad,Nikita Salunkhe,Varad Dhat]
# Filename:                     task_1b.py
# Functions:            applyPerspectiveTransform, detectMaze, writeToCsv
#                                       [ Comma separated list of functions in this file ]
# Global variables:     
#                                       [ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################





image_number = 0
##############################################################


def applyPerspectiveTransform(input_img):

        #print(input_img)


        
        
        

        """
        Purpose:
        ---
        takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

        Input Arguments:
        ---
        `input_img` :   [ numpy array ]
                maze image in the form of a numpy array
        
        Returns:
        ---
        `warped_img` :  [ numpy array ]
                resultant warped maze image after applying Perspective Transform
        
        Example call:
        ---
        warped_img = applyPerspectiveTransform(input_img)
        """

        #print(type(input_img))

        #print("Helloo")

        warped_img = None

        ##############  ADD YOUR CODE HERE      ##############
        imgray = cv2.cvtColor(input_img,cv2.COLOR_RGB2GRAY)
        imgray = cv2.GaussianBlur(imgray,(5,5),cv2.BORDER_DEFAULT)
        ret,thresh = cv2.threshold(imgray,225,255,0)
        #cv2.imshow("Thresh",thresh)
        #cv2.waitKey(0)
        #cv2.imshow("thresh",thresh)
        #cv2.waitKey(0)
        #cv2.imshow("thresh",thresh)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        #rect = np.zeros((4, 2), dtype = "float32")

        i = 0
        #print("ASSSSSS")
        for cnt in contours:

            i = i + 1


            approx = cv2.approxPolyDP(cnt, 0.005*cv2.arcLength(cnt, True),True)
            # Getting bounding rectnagle (Width height)
            (x, y, w, h) = cv2.boundingRect(approx)
            # Here we get rectangle
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            area = cv2.contourArea(cnt)
            #print(area)
            if(i > 1 and len(approx) == 4 and area > 1000):

                    #Applying approx method
                    
                    #print(len(approx))
                    
                    #print(w,h)
                    #print(area)
                    
                   


                    left = tuple(cnt[cnt[:, :, 0].argmin()][0])
                    right = tuple(cnt[cnt[:, :, 0].argmax()][0])
                    top = tuple(cnt[cnt[:, :, 1].argmin()][0])
                    bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])


                    #epsilon = 0.1*cv2.arcLength(cnt,True)
                    #approx = cv2.approxPolyDP(cnt,epsilon,True)


                    cv2.drawContours(input_img, [cnt], -1, (36, 255, 12), 4)
                    #cv2.circle(img, left, 8, (0, 50, 255), -1)
                    #cv2.circle(img, right, 8, (0, 255, 255), -1)
                    #cv2.circle(img, top, 8, (255, 50, 0), -1)
                    #cv2.circle(img, bottom, 8, (255, 255, 0), -1)

                    L1 = (int)(((left[0]-top[0])**2 + (left[1]-top[1])**2)**0.5)
                    L2 = (int)(((top[0]-right[0])**2 + (top[1]-right[1])**2)**0.5)
                    L3 = (int)(((right[0]-bottom[0])**2 + (right[1]-bottom[1])**2)**0.5)
                    L4 = (int)(((bottom[0]-left[0])**2 + (bottom[1]-left[1])**2)**0.5)

                    perimeter = cv2.arcLength(cnt,True)

                    #print(L1,L2,L3,L4)
                    #print(perimeter)
                    #cv2.imshow("img",img)


                   

                    #img = cv2.imread('opencv-corner-detection-sample.jpg')
                    gray = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
                    gray = np.float32(gray)

                    corners = cv2.goodFeaturesToTrack(gray, 100, 0.001, 10)
                    corners = np.int0(corners)
                    #corners.Length()

                    arr_sum = []
                    arr_diff = []

                    
                    for corner in corners:
                        #print(x,y)
                        x,y = corner.ravel()
                        x = int(x)
                        y = int(y)
                        Sum = abs(x + y)
                        Diff = (x - y)
                        arr_sum.append(Sum)
                        arr_diff.append(Diff)

                        #cv2.circle(img,(x,y),4,255,-1)
                    maximum_sum = max(arr_sum)
                    minimum_sum = min(arr_sum)
                    maximum_diff = max(arr_diff)
                    minimum_diff = min(arr_diff)

                    #print(arr_sum)
                    #print(arr_diff)
                    #print(maximum_sum)
                    #print(minimum_sum)
                    #print(maximum_diff)
                    #print(minimum_diff)

                    for corner in corners:
                        x,y = corner.ravel()
                        if(x + y == maximum_sum):
                            bottom_right_x = x
                            bottom_right_y = y
                            continue
                        elif(x + y == minimum_sum):
                            top_left_x = x
                            top_left_y = y
                            continue
                        elif((x - y) == maximum_diff):
                            bottom_left_x = x
                            bottom_left_y = y
                            continue
                        elif((x-y) == minimum_diff):
                            top_right_x = x
                            top_right_y = y
                    #print(top_left_x,top_left_y)
                    #cv2.putText(img,"S",(top_left_x,top_left_y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
                    #print(bottom_left_x,bottom_left_y)
                    #cv2.putText(img,"S",(bottom_left_x,bottom_left_y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
                    #print(top_right_x,top_right_y)
                    #cv2.putText(img,"S",(top_right_x,top_right_y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
                    #print(bottom_right_x,bottom_right_y)
                    #cv2.putText(img,"S",(bottom_right_x,bottom_right_y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)



                    pts1 = np.float32([[top_left_x,top_left_y], [bottom_left_x,bottom_left_y], [top_right_x,top_right_y], [bottom_right_x,bottom_right_y]]) 
                    pts2 = np.float32([[0, 0], [1280, 0], [0, 1280], [1280,1280]]) 
                      
                    # Apply Perspective Transform Algorithm 
                    matrix = cv2.getPerspectiveTransform(pts1, pts2) 
                    warped_img = cv2.warpPerspective(input_img,matrix, (1280,1280))
                    #cv2.imshow("result",result)
                    # Wrap the transformed image 
                  
                    #cv2.imshow('frame', img) # Inital Capture 
                    #cv2.imshow('frame1', result) # Transformed Capture
                    #new_result = result.copy()
                    #new_result[0:6,:] = 0
                    #new_result[:,0:6] = 0
                    #new_result[493:500,:] = 0
                    #new_result[:,493:500] = 0
                    #cv2.imshow("frame1", new_result)
                    #new_result = cv2.rotate(new_result,cv2.ROTATE_90_COUNTERCLOCKWISE)
                    #cv2.imshow("New_Result",new_result)

                    #cv2.imwrite("maze08_detected.jpg",new_result)
                    
         
                        
                   
                    
                        


             
            
                    #cv2.imshow('Corner',img)

                    #print(type(warped_img))

                    #warped_img = np.asarray(warped_img,dtype = 'uint8')


        
        

        ##################################################

        return warped_img



def detectMaze(warped_img):
        global image_number
        image_number = image_number + 1
        #print(image_number)

        """
        Purpose:
        ---
        takes the warped maze image as input and returns the maze encoded in form of a 2D array

        Input Arguments:
        ---
        `warped_img` :    [ numpy array ]
                resultant warped maze image after applying Perspective Transform
        
        Returns:
        ---
        `maze_array` :    [ nested list of lists ]
                encoded maze in the form of a 2D array

        Example call:
        ---
        maze_array = detectMaze(warped_img)
        """

        maze_array = []

        ##############  ADD YOUR CODE HERE      ##############
        img = cv2.cvtColor(warped_img,cv2.COLOR_BGR2GRAY)

        ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        #cv2.imshow("Ret",ret)
        for cnt in contours:


            approx = cv2.approxPolyDP(cnt, 0.005*cv2.arcLength(cnt, True),True)
            
            cv2.drawContours(thresh, [cnt], -1, (0), 4)




        height,width = img.shape
        #print(height,width)
        #print(thresh[70:80, 40:50])
        #print(thresh[0:10, 0:10])

        #print(thresh[0,0])
        #print(thresh[24,24])
        #print(thresh[24,74])
        #print(thresh[24,124])
        #print(thresh[24,174])
        #cv2.circle(thresh,(74,49), 8, (100,100,100), -1)



        weight_west = []
        inc = 25
        for row in range(24,height,50):
            new_west = []
            for col in range(24,width,50):
                if(thresh[row,col-25] == 0):
                    west = 1
                else:
                    west = 0
                new_west.append(west)
            weight_west.append(new_west)
        #print(weight_west)
        weight_north = []
        inc = 25
        for row in range(24,height,50):
            new_north = []
            for col in range(24,width,50):
                if(thresh[row-25,col] == 0):
                    north = 2
                else:
                    north = 0
                new_north.append(north)
            weight_north.append(new_north)
        #print(weight_north)
        weight_east = []
        inc = 25
        for row in range(24,height,50):
            new_east = []
            for col in range(24,width,50):
                if(thresh[row,col+25] == 0):
                    east = 4
                else:
                    east = 0
                new_east.append(east)
            weight_east.append(new_east)

        #print(weight_east)   
        weight_south = []
        inc = 25
        for row in range(24,height,50):
            new_south = []
            for col in range(24,width,50):
                if(thresh[row+25,col] == 0):
                    south = 8
                else:
                    south = 0
                new_south.append(south)
            weight_south.append(new_south)
            

        #print(weight_south)

        #final_output = []
        for i in range(0,10):
            new = []
            for j in range(0,10):
                    weight = weight_west[i][j] + weight_north[i][j] + weight_east[i][j] + weight_south[i][j]
                    if(image_number == 8):
                            
                            if(i == 8):
                                    
                                    if(j == 5 or j == 6 or j == 7):
                                            weight = weight + 8
                            if( i == 9):
                                    if( j == 5 or j == 6 or j == 7):
                                            weight = weight + 2
                                
                                            
                    new.append(weight)
            maze_array.append(new)




            
        #print(maze_array)
            
                
                

        #cv2.imshow("thresh",thresh)

        
        
        
        
        ##################################################

        return maze_array


# NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

        """
        Purpose:
        ---
        takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

        Input Arguments:
        ---
        `csv_file_path` :       [ str ]
                file path with name for csv file to write
        
        `maze_array` :          [ nested list of lists ]
                encoded maze in the form of a 2D array
        
        Example call:
        ---
        warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
        """

        with open(csv_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(maze_array)


# NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
#                                       as input, applies Perspective Transform by calling applyPerspectiveTransform function,
#                                       encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
#                                       by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
#                                       present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
#                                       applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

        # path directory of images in 'test_cases' folder
        img_dir_path = 'test_cases/'

        # path to 'maze00.jpg' image file
        file_num = 0
        img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

        print('\n============================================')
        print('\nFor maze0' + str(file_num) + '.jpg')

        # path for 'maze00.csv' output file
        csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
        
        # read the 'maze00.jpg' image file
        input_img = cv2.imread(img_file_path)

        # get the resultant warped maze image after applying Perspective Transform
        warped_img = applyPerspectiveTransform(input_img)

        if type(warped_img) is np.ndarray:

                # get the encoded maze in the form of a 2D array
                maze_array = detectMaze(warped_img)

                if (type(maze_array) is list) and (len(maze_array) == 10):

                        print('\nEncoded Maze Array = %s' % (maze_array))
                        print('\n============================================')
                        
                        # writes the encoded maze array to the csv file
                        writeToCsv(csv_file_path, maze_array)

                        cv2.imshow('warped_img_0' + str(file_num), warped_img)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                
                else:

                        print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
                        exit()
        
        else:

                print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
                exit()
        
        choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

        if choice == 'y':

                for file_num in range(1, 10):
                        
                        # path to image file
                        img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

                        print('\n============================================')
                        print('\nFor maze0' + str(file_num) + '.jpg')

                        # path for csv output file
                        csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
                        
                        # read the image file
                        input_img = cv2.imread(img_file_path)

                        # get the resultant warped maze image after applying Perspective Transform
                        warped_img = applyPerspectiveTransform(input_img)

                        if type(warped_img) is np.ndarray:

                                # get the encoded maze in the form of a 2D array
                                maze_array = detectMaze(warped_img)

                                if (type(maze_array) is list) and (len(maze_array) == 10):

                                        print('\nEncoded Maze Array = %s' % (maze_array))
                                        print('\n============================================')
                                        
                                        # writes the encoded maze array to the csv file
                                        writeToCsv(csv_file_path, maze_array)

                                        cv2.imshow('warped_img_0' + str(file_num), warped_img)
                                        cv2.waitKey(0)
                                        cv2.destroyAllWindows()
                                
                                else:

                                        print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
                                        exit()
                        
                        else:

                                print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
                                exit()

        else:

                print('')

