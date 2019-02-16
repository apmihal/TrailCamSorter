from PIL import Image
import os
import time
import psutil
camera_loc = "1st Pines"

startPath = './newtest/'

targetPath = './' + camera_loc

if not os.path.exists(targetPath):
        os.makedirs(targetPath)

for picture in os.listdir(startPath):
    im = Image.open('./newtest/' + picture)
    im.show()
    response = input("Keep image y or n: ")
    if response == 'y':
        currentLoc = os.path.join(startPath, picture)
        targetLoc = os.path.join(targetPath, picture)
        os.rename(currentLoc, targetLoc)
        print('Target: ' + targetLoc)
    for proc in psutil.process_iter():
        #print(proc.name())
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()    
        
    
    
        
        

