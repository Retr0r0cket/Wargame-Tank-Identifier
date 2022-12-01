import os
import cv2
from configparser import ConfigParser
    
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

config = ConfigParser()
config.read('config.ini')
rootDIR = config.get('settings', 'directory')
subDIRs = fast_scandir(rootDIR)

bad_list=[]
for subDIR in subDIRs:
    file_list=os.listdir(subDIR) # create list of files in class directory
    for f in file_list: # iterate through the files
        fpath=os.path.join (subDIR,f)
        if os.path.isfile(fpath):
            index=f.rfind('.') # find index of period infilename
            ext=f[index+1:] # get the files extension
            if ext not in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
                # print(f'file {fpath}  has an invalid extension {ext}')
                bad_list.append(fpath)                    
            else:
                try:
                    img=cv2.imread(fpath)
                    size=img.shape
                except:
                    # print(f'file {fpath} is not a valid image file ')
                    bad_list.append(fpath)             
for image in bad_list:
    os.remove(image) 

minLength = min(len(os.listdir(subDIRs)))
for directory in subDIRs:
    filesList = os.listdir(directory)
    if len(filesList) > minLength:
        for file in filesList[directory][minLength:]:
            os.remove(directory + '/' + file)
        
for directory in subDIRs:
    print(len(os.listdir(directory)))