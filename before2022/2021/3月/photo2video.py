import os
import cv2
import glob


#size = (1200,720)
imgs_dir = './pinew10000/'
video_path = './pi10000.mp4'
img_list = sorted(glob.glob(os.path.join(imgs_dir,"*.png")),key=os.path.getmtime)
#for i in len(img_list)
print(len(img_list))
fps = 60

img = cv2.imread('./pinew10000/1.png')
imgInfo = img.shape
print(img.shape)
size = (imgInfo[1],imgInfo[0])
print(size)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
videoWriter = cv2.VideoWriter(video_path,fourcc,fps,size)
#video = cv2.VideoWriter('result.avi',fourcc,fps,size)
#video = cv2.VideoWriter('pi.avi',fourcc,fps,size,True)
#path = './pi_1to1000/'
#file_list = os.listdir(path)
#out_num = len(file_list)
for index,name in enumerate(img_list):
    frame = cv2.resize(cv2.imread(name),size)
    videoWriter.write(frame)
videoWriter.release()
print("end")
