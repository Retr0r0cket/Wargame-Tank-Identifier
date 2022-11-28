from PIL import ImageGrab
import os
from configparser import ConfigParser

def clipboardGrab(img):
    while True:
        newImg = ImageGrab.grabclipboard()
        if newImg != img:
            return newImg

config = ConfigParser()
config.read('config.ini')

DIR = config.get('settings', 'directory')

for faction in ['NATO', 'PACT']:
    if faction == 'NATO':
        countries = ['United States', 'France', 'United Kingdom', 'FRG', 'Canada', 'Denmark', 'Norway', 'Sweden']
    else:
        countries = ['Soviet Union', 'GDR', 'Poland', 'Czechoslovakia']
    for country in countries:
        for tank in range(int(input("Number of tanks for " + country + ": "))):
            tankName = input("Tank model: ")
            try:
                os.makedirs('/{DIR}/{faction}/{country}/{tankName}')
            except:
                pass

            img = ImageGrab.grabclipboard()
            for image in range(int(input("Number of images: "))):
                img = clipboardGrab(img)
                img.save('{DIR}/{faction}/{country}/{tankName}')