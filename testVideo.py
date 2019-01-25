from faceRecon import reconFaces, saveCroppedFaces

#!/usr/bin/env python
import cv2 #BROKEN FOR PYTHON3 working in Python2

""" Croppes faces from video given from input path and stores it"""
def main():
  
  print('\n\tVideo has to be between " " and be".mp4"')
  VideoPath = input("\tType Path to video: ")

  video = cv2.VideoCapture(VideoPath)
  success, image = video.read()
  count = 0
  while success:
  	cv2.imwrite('frame%d.jpg' % count, image)
  	framePath = ('frame%d.jpg' % count)
  	faces, photo = reconFaces(framePath)
  	saveCroppedFaces(faces,photo)

  	success, image = video.read()
  	count += 1
  	print(count)

  print("\n")

if __name__== "__main__":
  main()




