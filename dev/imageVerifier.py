import sys
import os
import cv2
    
# source: https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory\
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

if len(sys.argv) < 2:
    DIR = './Images'
else:
    DIR = sys.argv[1]
    
subDIRs = fast_scandir(DIR)
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