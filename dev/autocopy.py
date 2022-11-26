from PIL import ImageGrab
import subprocess
import os

def clipboardGrab(img):
    while True:
        newImg = ImageGrab.grabclipboard()
        if newImg != img:
            return newImg

for faction in ['NATO', 'PACT']:
    if faction == 'NATO':
        countries = ['United States', 'France', 'United Kingdom', 'FRG', 'Canada', 'Denmark', 'Norway', 'Sweden']
    else:
        countries = ['Soviet Union', 'GDR', 'Poland', 'Czechoslovakia']
    for country in countries:
        for tank in range(int(input("Number of tanks for " + country + ": "))):
            tankName = input("Tank model: ")
            #source: https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal
            try:
                os.makedirs('./Images/' + faction + '/' + country + '/' + tankName)
            except:
                pass
            # source: https://stackoverflow.com/questions/7045264/how-do-i-read-a-jpg-or-png-from-the-windows-clipboard-in-python-and-vice-versa
            img = ImageGrab.grabclipboard()
            for image in range(int(input("Number of images: "))):
                img = clipboardGrab(img)
                # source: https://www.geeksforgeeks.org/python-pil-image-save-method/
                img.save('../Images/' + faction + '/' + country + '/' + tankName)