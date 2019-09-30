import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract

from PIL import Image
from pytesseract import image_to_string

# You have to download and install tesseract-ocr, the os I am using is windows 10, and the path depends on where you install it.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def main():
# 	# Use the attached camera to capture images
# 	# 0 stands for the first one
# 	cap = cv2.VideoCapture(0)	

# 	if cap.isOpened():
# 		ret, frame = cap.read()
# 		print(ret)
# 		print(frame)
# 	else:
# 		ret = False

# 	img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# 	# img = Image.open('image.jpg')
# 	# text = pytesseract.image_to_string(img1)
# 	text = pytesseract.image_to_string(Image.fromarray(img1))
# 	print(text)
# 	print("-------------------")

# 	plt.imshow(img1)
# 	plt.title('Color Image RGB')
# 	plt.xticks([])
# 	plt.yticks([])
# 	plt.show()


# 	cap.release()

# if __name__ == "__main__":
# 	main()

def main():
    # Use the attached camera to capture images
    # 0 stands for the first one
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # img1 = img1.convert('1') # new added
        text = pytesseract.image_to_string(Image.fromarray(img1))
        cv2.imshow('frame', img1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return None
        print("Extracted Text: ", text)
    cap.release()

if __name__ == "__main__":
 	main()