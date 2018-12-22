import numpy as np 
import matplotlib.pyplot as plt 
import cv2

def show(image, title=None, figsize=(16,16)):
	plt.figure(figsize=figsize)
	plt.axis('off')
	plt.imshow(image)
	if(title):
		plt.title(title)
	plt.show()