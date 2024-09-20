import os
import numpy as np
import cv2

root_rgb = '/home/camsense/yao/my_yolo/yolov5/runs/detect/exp2'
root_gray = '/home/camsense/yao/my_yolo/yolov5/runs/detect/exp'

sum =0

for img in os.listdir(root_rgb):
    gray_path = os.path.join(root_gray,img)
    rgb_path = os.path.join(root_rgb,img)
    imrgb = cv2.imread(rgb_path)
    imgray = cv2.imread(gray_path)

    org = (50, 200)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 255, 0)  # BGR格式，白色
    thickness = 2

    cv2.putText(imrgb, "rgb", org, fontFace, fontScale, color, thickness)

    cv2.putText(imgray, 'gray', org, fontFace, fontScale, color, thickness)

    cat_img = np.concatenate([imrgb,imgray])

    cv2.imwrite('{}/{}'.format('/home/camsense/yao/my_yolo/yolov5/runs/detect/concat/house1',img),cat_img)
    print(img)
    
    sum += 1
    
    # cv2.imshow('im',im)
    # cv2.waitKey(0)

print(sum)
