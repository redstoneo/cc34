import os 
import shutil
from_dir="C:/Users/Gerber/Downloads/C102_assets-main"
to_dir="C:/Users/Gerber/Downloads/C102_assets-main/C102_assets-main"

listoffiles=os.listdir(from_dir)
print(listoffiles)

for file in listoffiles:
    name,extension=os.path.splitext(file)
    #print(name)
    #print(extension)

    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file
        #print(path1)
        #print(path3)

        if os.path.exists(path2):
            print("Moving " + file + ".....")

            # Move from path1 ---> path3
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving " + file + ".....")
            shutil.move(path1, path3)