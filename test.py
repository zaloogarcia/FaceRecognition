from faceRecon import reconFaces, saveCroppedFaces

""" Croppes faces from image given from input path """
def main():
  
  print('\n\tImage has to be ".jpg"')
  ImagePath = input("\tType Path to image: ")
  facesLocation, image = reconFaces(ImagePath)
  saveCroppedFaces(facesLocation, image)
  print("\n")

if __name__== "__main__":
  main()




