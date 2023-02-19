import os 
import shutil

from_dir = "C:/Document_files"
to_dir = "D:/"

list_of_files = os.listdir(from_dir)
#print(list_of_files)


for File in list_of_files:
    name,extension = os.path.splitext(File)

    if extension=='':
       continue

    if extension in ['.txt','.doc','.docx','.pdf']:
       path1 = from_dir+'/'+File
       path2 = to_dir + '/' + "Document_files"
       path3 = to_dir + '/' + "Document_files" + '/' + File


       if os.path.exists(path2):
            print("Moving..." + File + '.....')
            shutil.move(path1, path3)

       else:    
            os. makedirs (path2)
            print("Moving" + File + '.....')
            shutil.move(path1, path3)