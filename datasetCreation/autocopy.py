from PIL import ImageGrab
import os
from configparser import ConfigParser
from time import sleep

def clipboardGrab(img):
    while True:
        sleep(0.25)
        newImg = ImageGrab.grabclipboard()
        if newImg != img:
            return newImg

config = ConfigParser()
config.read('config.ini')
DIR = config.get('settings', 'directory')
DIRList = []

for faction in ['NATO', 'PACT']:
    if faction == 'NATO':
        countries = ['United States', 'France', 'United Kingdom', 'FRG', 'Canada', 'Denmark', 'Norway', 'Sweden']
    else:
        countries = ['Soviet Union', 'GDR', 'Poland', 'Czechoslovakia']
    for country in countries:
        for tank in range(int(input("Number of tanks for " + country + ": "))):
            tankName = input("Tank model: ")
            directory = DIR + '/' + faction + '/' + country + '/' + tankName
            DIRList.append(directory)
            try:
                os.makedirs(directory)
            except:
                pass
            img = ImageGrab.grabclipboard()
            numOfTanks = int(input("Number of images: "))
            for image in range(numOfTanks):
                img = clipboardGrab(img)
                img.save(directory+"/"+tankName+"_"+str(image)+".png", 'PNG')
                print("Image " + str(image+1) + "/" + str(numOfTanks) + " saved")