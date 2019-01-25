from faceRecon import reconFaces, saveCroppedFaces
from multiprocessing import Process, cpu_count

def bothFunctionsInOne(ImagePath):
	facesLocation, image = reconFaces(ImagePath)
	saveCroppedFaces(facesLocation, image)

""" Croppes faces from 4 images given from input path at the same time"""
def main():
  
  print('\n\tImage has to be ".jpg" computer has',cpu_count(),'cores')
  ImagePath1 = input("\tType Path to the 1st image: ")
  ImagePath2 = input("\tType Path to the 2nd image: ")
  ImagePath3 = input("\tType Path to the 3rd image: ")
  ImagePath4 = input("\tType Path to the 4th image: ")
  
  # bothFunctionsInOne(ImagePath1)
  # bothFunctionsInOne(ImagePath2)
  # bothFunctionsInOne(ImagePath3)
  # bothFunctionsInOne(ImagePath4)
  
  process1 = Process(target=bothFunctionsInOne, args=(ImagePath1,))
  process2 = Process(target=bothFunctionsInOne, args=(ImagePath2,))
  process3 = Process(target=bothFunctionsInOne, args=(ImagePath3,))
  process4 = Process(target=bothFunctionsInOne, args=(ImagePath4,))
  
  process1.start()
  process2.start()
  process3.start()
  process4.start()
  
  print("\n")

if __name__== "__main__":
  main()




