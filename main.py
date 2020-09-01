import cv2
import os

mainfolder='images'
myFolders=os.listdir(mainfolder)
print(myFolders)

for folder in myFolders:
    path=mainfolder+'/'+folder
    #print(path)
    image=[]
    myList=os.listdir(path)
    #print(myList)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg=cv2.imread(f'{path}/{imgN}')
        #curImg=cv2.resize(curImg,(0,0),None,0.2,0.2)
        image.append(curImg)

    stitcher=cv2.Stitcher.create()
    (status,result)=stitcher.stitch(image)
    if (status==cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imshow(folder,result)

    else:
        print('Panorama Generation Unsuccessfull')
    #print(len(image))

cv2.waitKey(1)