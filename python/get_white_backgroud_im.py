# coding: utf-8
'''
    根据png透明图，获取白底图，使用cv2.add方法
'''
import numpy as np
import cv2 
import sys


#-1表示按照原始数据读取，不会自动转化为rgb
im = cv2.imread(sys.argv[1], -1)
print im.dtype
#分别提取透明度通道和原始图三通道
mask, orgin =im[:,:,3],im[:,:,0:3]

cv2.imwrite('000_mask.jpg', mask)
cv2.imwrite('000_orgin.jpg', orgin)
#cv2.THRESH_BINARY_INV表示大于thresh为0，否则为255
ret, thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV)
thresh = np.tile(thresh.reshape(thresh.shape[0], thresh.shape[1], 1), (1,1,3))

##thresh和orgin都是unint8
#直接相加，会出现溢出的情况，例如加起来等于256，会变成0
#im_white = thresh+orgin
#使用cv2.add，超过255后，会自动截断为255
im_white = cv2.add(thresh,orgin)
#im_white = im_white.astype(np.uint8)
cv2.imwrite('000_white_backround.jpg', im_white)

