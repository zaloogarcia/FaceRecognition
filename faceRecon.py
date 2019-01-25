from PIL import Image
import face_recognition, random

""" 
Returns a list of coordinates where the faces are from a given picture,
and the decoded image
"""
def reconFaces(ImagePath):
	try:
		""" Loads the image from path """
		image = face_recognition.load_image_file(ImagePath)
		""" 
		Locates the faces from image and returns a 4-tuple with the location
		of each one
		"""
		facesCoordinates = face_recognition.face_locations(image)
		print('\tImage contains ', len(facesCoordinates), ' faces\n')
		return(facesCoordinates, image)
	except:
		print('Incorrect Path to image: ', ImagePath)

""" 
Crops faces from a given image (already loaded) 
and a set of coordinates
 """
def saveCroppedFaces(facesCoordinates, image):
	try:
		for face in facesCoordinates:
			# Print the location of each face in this image
			top, right, bottom, left = face
			print("\tSaved face located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

			# You can access the actual face itself like this:
			faceImage = image[top:bottom, left:right]
			pilImage = Image.fromarray(faceImage)
			pilImageName = "faces"+str(random.randint(1,2000))+'.jpg'
			pilImage.save(pilImageName)
	except:
		print("Error saving the cropped faces")

