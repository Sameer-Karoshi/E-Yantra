###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv




########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    
    image1 = cv2.cvtColor(ip_image,cv2.COLOR_BGR2HSV)

    lower_green = np.array([36,25,25])
    upper_green = np.array([70,255,255])
    mask1 = cv2.inRange(image1,lower_green,upper_green)
    #cv2.imshow("Mask1",mask1)                #first we masked green colour means that one green dot
    cv2.imwrite("Mask1.png",mask1)             #we saved that masked image
    img = cv2.imread('Mask1.png',0)
    _,img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
    h, w = img.shape[:2]
    contours0, hierarchy = cv2.findContours(img.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)  #By using contours we find the centre/centroid of the masked dot(green dot)
    moments = [cv2.moments(cnt) for cnt in contours0]
    centroids1 = [(int(round(m['m10']/m['m00'])),int(round(m['m01']/m['m00']))) for m in moments] #when we print centroids we can get centroid of an that dot in the form of list
    print(centroids1[0])                   #printing of centroid is done here


    for c in centroids1:
            cv2.circle(img,c,5,(0,0,0))
    #cv2.imshow("image",img)
    0XFF & cv2.waitKey()
    cv2.destroyAllWindows()

    lower_red = np.array([0,100,100])
    upper_red = np.array([20,255,255])
    mask2 = cv2.inRange(image1,lower_red,upper_red)
    #cv2.imshow("Mask2",mask2)      #and here we have masked red coloured dot
    cv2.imwrite("Mask2.png",mask2)  #and we have saved that masked image
    img1 = cv2.imread('Mask2.png',0)       #Here we read that image in gray scale
    _,img1 = cv2.threshold(img1,0,255,cv2.THRESH_OTSU)
    h, w = img1.shape[:2]                   #using this we can get height and width of an image
    contours0, hierarchy = cv2.findContours(img1.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    moments = [cv2.moments(cnt) for cnt in contours0]
    centroids2 = [(int(round(m['m10']/m['m00'])),int(round(m['m01']/m['m00']))) for m in moments] #so and here also we will find the red masked dot
    #print(centroids2)
    #print(centroids2[0])     
    try:
        os.remove("Mask1.png")
        os.remove("Mask2.png")
    except: pass                        #so here we dont want to save permanatly that two masked images so we have deleted these two masked images

    for c in centroids2:
            cv2.circle(img1,c,5,(0,0,0))
    #cv2.imshow("image1",img1)
    0XFF & cv2.waitKey()
    cv2.destroyAllWindows()
    centroids2.remove((511,511))      #when the red coloured masking is done using contours we can get the co ordinates of an center of an red dot,right now we dont want the centre coordinates
    centroids2.remove((512,512))       #so here we removed that centres coordinats
   # print(centroids2[0])
            


    height1, width1 = image1.shape[:2]
    Height1 = height1//2;        #here we calculated the centre of an image
    Width1 = width1//2;
    M1 = (Height1-centroids1[0][0])/(Width1-centroids1[0][1])  # here we we calculated slope of line which passing through centre and that  green dot
    print(M1)
    M2 = (Height1-centroids2[0][0])/(Width1-centroids2[0][1])    #here we have calculated slope of an send line which passes through red dot
    print(M2)
    angle1 = math.atan(abs((M1 - M2)/(1 + M1*M2)))   #finaly we have calculated slope of that two lines,by using these two slopes we can find the angle between these two point
    angle1 = math.degrees(angle1)
    if(M1<0 and M2<0):
       angle1 = round(angle1,2)
       print(angle1)
       return angle1
    else:
       angle1  = 180 - angle1
       angle1 = round(angle1,2)
       print(angle1)
       return angle1


    
    
    #angle = 0.00
    ## Your Code goes here
    ###########################
    cv2.imshow("window", ip_image)
    cv2.waitKey(0);
    #return angle




    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name , str(A)])
        ## incrementing counter variable
        i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        #writer.writerow(['Image Name','Angle'])
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
