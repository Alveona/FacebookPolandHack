import cv2 
import os 
import math
import numpy as np 

def cartoonize_image(img, ksize=5, sketch_mode=False):
    num_repetitions, sigma_color, sigma_space, ds_factor = 10, 5, 7, 4 
    # Convert image to grayscale 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
 
    # Apply median filter to the grayscale image 
    img_gray = cv2.medianBlur(img_gray, 5) #7
 
    # Detect edges in the image and threshold it 
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=ksize) 
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV) 
 
    # 'mask' is the sketch of the image 
    if sketch_mode: 
        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) 
 
    # Resize the image to a smaller size for faster computation 
    img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
 
    # Apply bilateral filter the image multiple times 
    for i in range(num_repetitions): 
        img_small = cv2.bilateralFilter(img_small, ksize, sigma_color, sigma_space) 
 
    img_output = cv2.resize(img_small, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR) 
 
    dst = np.zeros(img_gray.shape) 
 
    # Add the thick boundary lines to the image using 'AND' operator 
    dst = cv2.bitwise_and(img_output, img_output, mask=mask) 
    return dst

def get_images_from_given_seconds(video_path, time, output_path):
    cam = cv2.VideoCapture(video_path)
    fps = math.floor(cam.get(cv2.CAP_PROP_FPS))
    print(fps)
    currentframe = 0
    index = 0
    #output_path = "/rubbish/"
    while(True): 
        ret,frame = cam.read() 
  
        if ret: 
            current = math.floor(currentframe/fps)
            if (current in time):
                name = output_path + str(index) + 'time' + str(current) + '.jpg'
                print ('Creating...' + name) 
                cv2.imwrite(name, cartoonize_image(frame, ksize=5, sketch_mode=False))
                time.remove(current)
                index+=1
            currentframe += 1
        else: 
            break
  
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()