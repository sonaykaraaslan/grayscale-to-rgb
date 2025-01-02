# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:26:03 2024

@author: sonay
"""

#%%
import cv2
import time 

start_time = time.time()
# İlk olarak, tek bir resmi yükleyelim
image = cv2.imread('Data/00398v.jpg', 0)

# Resmin yüksekliğini ve genişliğini alalım
height, width = image.shape

# Üç parçaya bölelim. (her biri aynı boyut)
p_height = height // 3

# Her bir parçayı ayıralım
part1 = image[0:p_height, :]
part2 = image[p_height:2*p_height, :]
part3 = image[2*p_height:3*p_height, :]


# Parçalara ayırmış olduğumuz gri resmimizi birleştirelim.
image = cv2.merge((part1, part2, part3))

# Renkli resmimizi kaydediyoruz : 
cv2.imwrite('yeni_resim.jpg', image)


cv2.imshow('yeni_resim', image)
cv2.waitKey(0)
end_time = time.time()
total_time = end_time-start_time

print(total_time)