import os
import cv2

IMAGE_SIZE = 20



def read_image(path):
	image = cv2.imread(path)
	return image



def resize_image(image):
	image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
	return image



def traverse_dir(path):
	images = []
	labels = []	
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith("jpg") or file.endswith("png"):
				#print(os.path.join(root, file))
				#print(os.path.relpath(root, path))
				image = read_image(os.path.join(root, file))
				image = image_proc(image)
				images.append(image)
				labels.append(os.path.relpath(root, path))
				labs, code = transcode(labels)
	return images, labs, code



def image_proc(image):
	# step 1.gray
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# step 2.mediumBlur
	#image = cv2.medianBlur(image,5)
	# step 3.ADAPTIVE_THRESH_GAUSSIAN
	#image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)	
	# step 4.get ROI

	# step 5.resize
	image = resize_image(image)
	# step 6.convert numpy array
	return image


def transcode(arr):
	labs = []
	code = []
	for ele in arr:
		try:
			idx = code.index(ele)			
		except:
			idx = len(code)
			code.insert(idx, ele)
		labs.append(idx)
	return labs, code